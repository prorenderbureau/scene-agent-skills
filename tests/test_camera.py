import pytest
np=pytest.importorskip('numpy')
pytest.importorskip('scipy')
from scene_agent.camera import project,fit_camera
from scene_agent.maxscript import generate_camera

def fixture():
    rng=np.random.default_rng(42)
    points=rng.uniform([-3,-2,0],[3,2,4],(24,3))
    position=[.3,-.2,-8]
    rotation=[.02,-.03,.015]
    pixels,_=project(points,position,rotation,1050,[1200,900])
    return {'image_size':[1200,900],'world_points':points.tolist(),'image_points':pixels.tolist(),
            'initial':{'position':[.1,0,-7.5],'rotvec_world_to_camera':[0,0,0],'focal_px':1000},'holdout_indices':[20,21,22,23]}

def test_recover_known_camera_and_holdout(tmp_path):
    d=fixture();r=fit_camera(d)
    assert r['converged'] and r['holdout_rms_px']<1e-5 and r['training_rms_px']<1e-5
    assert r['position_m']==pytest.approx([.3,-.2,-8],abs=1e-5)
    assert r['focal_px']==pytest.approx(1050,abs=1e-4)
    generate_camera(r,tmp_path/'camera.ms')
    # A wrong unused landmark must show up in holdout, even when the fit is excellent.
    d['image_points'][20][0]+=80
    r=fit_camera(d)
    assert r['training_rms_px']<1e-5 and r['holdout_rms_px']>39

def test_planar_input_rejected():
    d=fixture()
    for p in d['world_points']:p[2]=0
    with pytest.raises(ValueError,match='non-coplanar'):fit_camera(d)
