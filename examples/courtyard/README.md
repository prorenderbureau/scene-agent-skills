# Courtyard fixture

An original, deliberately small 8 × 6 m rectangular plan for exercising the pipeline. It is not a real property, construction design or photorealistic showcase.

Walls are oriented reference-line segments. Their material extends to the **left** of each segment by its thickness. Storey elevation is the finished top of the slab; walls start there. The floor occupies the entire 8 × 6 m rectangle. Reference-line corners overlap deliberately; production junction cleanup is a separate step.

The south wall contains a 1 × 2.2 m door opening and a 2.5 × 1.5 m window at sill 0.8 m. Gross wall volume is 4.8 m³; net after openings is **3.61 m³**. This is independently checked by tessellation in the tests. Two more windows/doors are not inferred: the file explicitly contains **one door and two windows total**.

Run `scene-agent plan-check examples/courtyard/plan.json`, then `scene-agent ifc examples/courtyard/plan.json --out outputs/courtyard.ifc`. The IFC includes semantic simplified infills. `scene-agent max-plan ...` creates wall cells/slab only and intentionally leaves the openings empty.
