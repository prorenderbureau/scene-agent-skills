from pathlib import Path
import pytest
ifcopenshell=pytest.importorskip('ifcopenshell')
from scene_agent.core import read_json
from scene_agent.ifc_export import export_ifc

def test_ifc_semantics_geometry_units_and_reopen(tmp_path):
    import ifcopenshell.geom
    import ifcopenshell.validate
    import ifcopenshell.util.shape
    import ifcopenshell.util.unit
    import ifcopenshell.util.placement
    plan=read_json(Path(__file__).resolve().parents[1]/'examples/courtyard/plan.json')
    output=tmp_path/'demo.ifc'
    result=export_ifc(plan,output)
    assert result['walls']==4 and result['doors']==1 and result['windows']==2
    f=ifcopenshell.open(str(output))
    assert ifcopenshell.util.unit.calculate_unit_scale(f)==1
    assert len(f.by_type('IfcRelVoidsElement'))==3 and len(f.by_type('IfcRelFillsElement'))==3
    logger=ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(f,logger,express_rules=True)
    assert not logger.statements,logger.statements
    settings=ifcopenshell.geom.settings()
    south=next(w for w in f.by_type('IfcWall') if w.Name=='south')
    shape=ifcopenshell.geom.create_shape(settings,south)
    assert ifcopenshell.util.shape.get_volume(shape.geometry)==pytest.approx(3.61,abs=1e-6)
    for e in f.by_type('IfcBuildingElement'):
        assert e.ContainedInStructure
        assert ifcopenshell.geom.create_shape(settings,e).geometry.verts
    export_ifc(plan,tmp_path/'second.ifc')
    f2=ifcopenshell.open(str(tmp_path/'second.ifc'))
    assert {x.Name:x.GlobalId for x in f.by_type('IfcWall')}=={x.Name:x.GlobalId for x in f2.by_type('IfcWall')}
    with pytest.raises(FileExistsError):export_ifc(plan,output)
    # Elevated storey must retain world placement, not double-apply its elevation.
    plan['storeys'][0]['elevation']=3.4
    export_ifc(plan,tmp_path/'upper.ifc')
    upper=ifcopenshell.open(str(tmp_path/'upper.ifc'))
    m=ifcopenshell.util.placement.get_local_placement(upper.by_type('IfcWall')[0].ObjectPlacement)
    assert m[2,3]==pytest.approx(3.4)
