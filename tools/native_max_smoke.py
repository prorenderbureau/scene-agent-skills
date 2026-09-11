"""Run only via 3dsmaxbatch.exe in a fresh scene; see docs/testing.md.

No third-party models/textures are used. Output is a technical fixture, not a beauty benchmark.
"""
from pathlib import Path
import os
import json
import time
import math
from pymxs import runtime as rt

ROOT=Path(__file__).resolve().parents[1]
if os.environ.get('SCENE_AGENT_ISOLATED_BATCH')!='1' or len(rt.objects)!=0:
    raise RuntimeError('This smoke test requires an explicitly isolated, empty batch process.')
OUT=Path(os.environ['SCENE_AGENT_NATIVE_OUTPUT'])
OUT.mkdir(parents=True,exist_ok=False)
report={'state':'running','max_version':str(rt.maxVersion()),'checks':[]}
def record(name,ok,detail=None):
    report['checks'].append({'name':name,'passed':bool(ok),'detail':detail})
    (OUT/'native-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if not ok:raise AssertionError(name)
try:
    rt.units.SystemType=rt.Name('Centimeters');rt.units.SystemScale=1.0
    rt.fileIn(str(ROOT/'skills/scene-toolkit/scripts/scene_agent/templates/corona_tools.ms'))
    rt.saUseCorona()
    renderer=rt.renderers.current
    report['renderer_class']=str(rt.classOf(renderer))
    record('preview quality',rt.saQuality(rt.Name('preview')).progressive_passLimit==16)
    record('review quality',rt.saQuality(rt.Name('review')).progressive_passLimit==64)
    record('final quality',rt.saQuality(rt.Name('final')).progressive_passLimit==160)
    rt.saQuality(rt.Name('preview'))
    material=rt.saPhysical('SA | Test stone',rt.Color(170,165,155),roughness=.7)
    record('physical roughness mode',material.roughnessMode==0 and abs(material.baseRoughness-.7)<1e-5)
    glass=rt.saGlass('SA | Test glass')
    record('thick glass',glass.refractionAmount==1 and not glass.useThinMode)
    rt.saDisplacement(material,rt.Noise(),-.2,.5)
    record('millimetre displacement conversion',abs(material.displacementMaximum-.05)<1e-6)
    rt.fileIn(str(ROOT/'outputs/native-input/plan.ms'))
    record('plan geometry',len(rt.geometry)>4)
    audits=rt.saMeshAudit(rt.Array(*list(rt.geometry)))
    record('wall cells closed and mapped',all(a[3]==0 and a[4] for a in audits),len(audits))
    # Camera fit transfer is tested against the numeric solution without inventing a render match.
    rt.fileIn(str(ROOT/'outputs/native-input/camera.ms'))
    camera_solution=json.loads((ROOT/'outputs/native-input/camera.json').read_text())
    matched=rt.getNodeByName('SA | Matched camera')
    record('camera FOV transfer',abs(matched.fov-camera_solution['horizontal_fov_degrees'])<1e-4)
    record('camera position transfer',all(abs(matched.pos[i]-camera_solution['position_m'][i]*100)<1e-3 for i in range(3)))
    record('camera uses explicit free pose and FOV',not matched.targeted and matched.fovSource==0)
    landmarks=json.loads((ROOT/'examples/camera/landmarks.json').read_text())
    errors=[]
    focal=landmarks['image_size'][0]/(2*math.tan(math.radians(matched.fov)/2))
    for world,pixel in zip(landmarks['world_points'],landmarks['image_points']):
        local=rt.Point3(*[v*100 for v in world])*rt.inverse(matched.transform)
        uv=[landmarks['image_size'][0]/2+local.x/(-local.z)*focal,
            landmarks['image_size'][1]/2-local.y/(-local.z)*focal]
        errors.append(math.dist(uv,pixel))
    record('host camera landmark reprojection',max(errors)<.01,{'max_error_px':max(errors)})
    # Concrete lighting/render proof using a separate fixture camera.
    cam=rt.CoronaCam(name='SA | Fixture overview');cam.targeted=False;cam.fovSource=0;cam.autoVerticalTilt=False;cam.verticalShift=0;cam.enableDof=False;cam.pos=rt.Point3(1250,-1350,1000)
    rt.saAim(cam,rt.Point3(400,300,90));cam.fov=48
    light=rt.saAreaLight('SA | Test key',rt.Point3(400,-200,800),rt.Point3(400,250,0),8,6,intensity=3,kelvin=4500)
    mgr=rt.maxOps.GetCurRenderElementMgr()
    previous=rt.CShading_LightSelect();previous.elementName='User existing element';mgr.AddRenderElement(previous)
    rt.saLightMix(rt.Array(rt.Array('Fixture',rt.Array(light))))
    record('LightMix preserves existing element',str(mgr.GetRenderElement(0).elementName)=='User existing element' and mgr.NumRenderElements()==4)
    try:
        rt.saLightMix(rt.Array())
        duplicate_blocked=False
    except Exception:duplicate_blocked=True
    record('duplicate LightMix blocked',duplicate_blocked)
    rt.backgroundColor=rt.Color(32,37,45)
    rt.renderWidth=320;rt.renderHeight=240;rt.renderPixelAspect=1.0
    renderer.progressive_passLimit=8;renderer.adaptivity_targetError=0
    rt.viewport.setCamera(cam)
    rt.saveMaxFile(str(OUT/'fixture.max'),quiet=True)
    mgr.SetElementsActive(False)
    started=time.time()
    bmp=rt.render(camera=cam,outputfile=str(OUT/'fixture.png'),vfb=False)
    rt.close(bmp)
    record('native Corona render written',(OUT/'fixture.png').exists(),{'seconds':round(time.time()-started,2)})
    report['state']='passed'
except Exception as exc:
    report['state']='failed';report['error']=str(exc)
    raise
finally:
    (OUT/'native-report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
