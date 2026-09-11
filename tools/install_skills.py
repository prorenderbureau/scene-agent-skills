"""Install the shared bundle into an explicitly selected project, without clobbering skills."""
import argparse
import hashlib
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
IGNORE=shutil.ignore_patterns('__pycache__','*.pyc','*.egg-info')


def contents(folder):
    return {p.relative_to(folder).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts
            and not any(x.endswith('.egg-info') for x in p.parts) and p.suffix!='.pyc'}


def install(project,agent,dry_run=False):
    project=Path(project).expanduser().resolve()
    if not project.is_dir():raise ValueError('Project directory must already exist')
    agents=['codex','claude'] if agent=='both' else [agent]
    if any(a not in ('codex','claude') for a in agents):raise ValueError('Unknown agent')
    jobs=[]
    for a in agents:
        target=project/('.agents' if a=='codex' else '.claude')/'skills'
        if not target.resolve().is_relative_to(project):raise ValueError('Skills destination leaves project through a symlink')
        for source in sorted((ROOT/'skills').iterdir()):
            if not (source/'SKILL.md').is_file():continue
            dest=target/source.name
            if dest.is_symlink():raise ValueError(f'Symlink destination refused: {dest}')
            if dest.exists():
                if not dest.is_dir() or contents(dest)!=contents(source):
                    raise FileExistsError(f'Existing skill differs: {dest}. Back it up and choose how to merge; no files changed.')
            else:jobs.append((source,dest))
    # Conflict preflight completes for both agents before any copying.
    if not dry_run:
        for source,dest in jobs:
            dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copytree(source,dest,ignore=IGNORE)
    return {'project':str(project),'agent':agent,'new_skills':len(jobs),'dry_run':dry_run}


if __name__=='__main__':
    import json
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--project',required=True)
    p.add_argument('--agent',choices=['codex','claude','both'],default='both')
    p.add_argument('--dry-run',action='store_true')
    args=p.parse_args()
    try:print(json.dumps(install(args.project,args.agent,args.dry_run),indent=2))
    except (ValueError,OSError) as e:p.exit(2,str(e)+'\n')
