# Lessons from architectural reconstruction

These lessons inform the skills and tests. They are engineering observations, not claims that v0.1.0 solves every item automatically.

| Failure | Why it happens | Better procedure | Implemented evidence/control |
|---|---|---|---|
| Detailed model, wrong composition | Camera fitted too late | Match shell/landmarks before detail | Camera skill + numerical fit/holdout |
| Numeric camera correct, native view wrong | Host target/FOV-source mode overrides intent | Explicit free camera and FOV source; reproject in host | Native camera regression |
| Multiple images disagree | References show different design variants | Hero priority and contradiction ledger | Reference workflow |
| Textures exist but fail to render | Wrong extension/container or loader support | Decode by content; test native load | Image-header test; native load remains host task |
| Enormous surface craters | Height range interpreted in wrong units | Millimetre bounds and neutral-map calibration | Native displacement unit check |
| Shiny concrete / matte metal | Roughness/glossiness confusion | Declare roughness mode and inspect neutral crop | Corona material helper |
| Curtains render too dark | Thin/solid material and shell assumptions conflict | Pick one consistent transmission strategy | Material guide |
| Expensive heavy-scene conversions | Asset conversion repeated across thousands of nodes | Prepare one asset in a small scene before merge | Asset workflow |
| Slow save/load despite tolerable triangles | Too many independent scene nodes | Instances, proxies and measured load-time budgets | Modeling/landscape guidance |
| Green blobs instead of foliage | Uniform material and crown repetition | Species detail, transmission, density and scale variation | Landscape workflow |
| Stairs under an uncut slab | Hero framing hides spatial defects | Plan/section review and real voids | Spatial audit guidance; IFC void geometry tested |
| Wrong texture after relinking | Duplicate basenames | Relative paths and content hashes | Manifest ambiguity report |
| Claimed BIM is only mesh geometry | Type/void/containment missing | Semantic IFC hierarchy and opening relationships | IFC schema/geometry tests |
| IFC looks right but imports as Morph | Translator mapping differs | Check native type/editability and roundtrip | Archicad procedure; host proof pending |
| Render cap described as convergence | Pass limit reached before noise target | Record actual stopping condition and crops | Explicit quality preset limits |
| Background makes accuracy look better | Source image projected behind model | Separate composition and geometry evaluation | Review rubric |
| MCP says success without a render | Tool prepared a script, did not run host | Distinguish prepared/running/rendered/verified | Tool return scope + capability matrix |
| User work lost during a helper run | Unconditional scene reset | Additive production scripts; isolated empty smoke host | No-reset generator test |

Future improvements should be judged against these failure cases with small reproducible fixtures. Extra prompt length alone does not fix them.
