from pathlib import Path
import importlib.util
import json
import re
import pytest
yaml=pytest.importorskip('yaml')
ROOT=Path(__file__).resolve().parents[1]

def test_skills_and_local_links():
    skills=list((ROOT/'skills').glob('*/SKILL.md'))
    assert len(skills)==20
    for p in skills:
        raw=p.read_text(encoding='utf-8')
        front=yaml.safe_load(raw.split('---',2)[1])
        assert front['name']==p.parent.name and len(front['description'])>40
        ui=yaml.safe_load((p.parent/'agents/openai.yaml').read_text())['interface']
        assert 25<=len(ui['short_description'])<=64
        assert '$'+p.parent.name in ui['default_prompt']
    for p in ROOT.rglob('*.md'):
        if any(x in p.parts for x in ('outputs','.git','.venv')):continue
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):continue
            path=link.split('#')[0].strip('<>')
            assert (p.parent/path).exists(),f'{p.relative_to(ROOT)} → {link}'

def test_manifest_consistency():
    codex=json.loads((ROOT/'.codex-plugin/plugin.json').read_text())
    claude=json.loads((ROOT/'.claude-plugin/plugin.json').read_text())
    assert codex['name']==claude['name']=='scene-agent-skills'
    assert codex['version']==claude['version']=='0.1.0'
    assert (ROOT/codex['skills']).is_dir()
    m=json.loads((ROOT/'.claude-plugin/marketplace.json').read_text())
    assert m['plugins'][0]['source']=='./'

def test_installer_idempotent_and_preserves_edits(tmp_path):
    spec=importlib.util.spec_from_file_location('installer',ROOT/'tools/install_skills.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    assert mod.install(tmp_path,'both',True)['new_skills']==40
    assert not (tmp_path/'.agents').exists()
    assert mod.install(tmp_path,'both')['new_skills']==40
    assert mod.install(tmp_path,'both')['new_skills']==0
    p=tmp_path/'.agents/skills/scene-toolkit/SKILL.md';p.write_text('user edits')
    with pytest.raises(FileExistsError):mod.install(tmp_path,'both')
    assert p.read_text()=='user edits'
