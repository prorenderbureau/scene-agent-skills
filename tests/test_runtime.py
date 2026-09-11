import copy
import json
from pathlib import Path
import pytest
from scene_agent.core import read_json, catalogue, recipe, confined, DATA
from scene_agent.plan import validate_plan, calibrate
from scene_agent.maxscript import wall_cells, generate_plan, generate_preset, ms_string
from scene_agent.assets import inspect_image, manifest, package
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]

@pytest.fixture
def plan():return read_json(ROOT/'examples/courtyard/plan.json')

def test_catalogue():
    styles=catalogue('styles')
    Draft202012Validator(catalogue('styles.schema')).validate(styles)
    assert len({s['id'] for s in styles})==16
    for s in styles:
        assert recipe(s['id'])['execution']=='recipe-only'
    with pytest.raises(ValueError):recipe('unknown')

def test_plan_and_scale(plan):
    assert validate_plan(plan)['valid']
    assert calibrate([10,20],[210,20],8)['metres_per_pixel']==.04
    with pytest.raises(ValueError):calibrate([0,0],[0,0],1)
    with pytest.raises(ValueError):calibrate([0,0],[1,0],float('nan'))

@pytest.mark.parametrize('problem',['units','duplicate','outside','overlap','height','zero-wall','negative','unknown'])
def test_reject_bad_plans(plan,problem):
    w=plan['storeys'][0]['walls'][0]
    if problem=='units':plan['units']='mm'
    if problem=='duplicate':w['id']='floor'
    if problem=='outside':w['openings'][0]['offset']=7.5
    if problem=='overlap':w['openings'][1]['offset']=1.2
    if problem=='height':w['openings'][0]['height']=8
    if problem=='zero-wall':w['end']=w['start']
    if problem=='negative':w['thickness']=-1
    if problem=='unknown':w['magic_auto_wall']=True
    assert not validate_plan(plan)['valid']

def test_wall_cells_actual_volume(plan):
    w=plan['storeys'][0]['walls'][0]
    assert sum((b-a)*(d-c)*w['thickness'] for a,b,c,d in wall_cells(w))==pytest.approx(3.61)

def test_no_overwrite_and_no_reset(plan,tmp_path):
    path=tmp_path/'plan.ms'
    generate_plan(plan,path)
    s=path.read_text()
    assert 'resetMaxFile' not in s and 'saveMaxFile' not in s
    with pytest.raises(FileExistsError):generate_plan(plan,path)
    with pytest.raises(ValueError):generate_preset(tmp_path/'x.ms','bad')
    assert ms_string('a"\\b\nc')=='"a\\"\\\\b\\nc"'

def test_image_header_not_extension(tmp_path):
    from PIL import Image
    p=tmp_path/'pretend.png';Image.new('RGB',(17,11),'grey').save(p,format='JPEG')
    r=inspect_image(p)
    assert r['format']=='JPEG' and not r['extension_matches'] and r['size']==[17,11]
    p.write_bytes(b'not an image')
    with pytest.raises(OSError):inspect_image(p)

def test_asset_package_and_collision(tmp_path):
    import zipfile
    root=tmp_path/'source';root.mkdir();(root/'a').mkdir();(root/'b').mkdir()
    (root/'a/wood.png').write_bytes(b'one');(root/'b/wood.png').write_bytes(b'two')
    assert 'wood.png' in manifest(root)['ambiguous_basenames']
    with pytest.raises(ValueError):package(root,root/'bad.zip')
    result=package(root,tmp_path/'good.zip')
    assert result['file_count']==2
    with zipfile.ZipFile(tmp_path/'good.zip') as z:
        assert z.read('a/wood.png')==b'one'
        assert len(json.loads(z.read('scene-agent-manifest.json'))['files'])==2
    with pytest.raises(FileExistsError):package(root,tmp_path/'good.zip')
    with pytest.raises(ValueError):confined(root,'../escape')

def test_nan_json_rejected(tmp_path):
    p=tmp_path/'bad.json';p.write_text('{"x":NaN}')
    with pytest.raises(ValueError):read_json(p)
