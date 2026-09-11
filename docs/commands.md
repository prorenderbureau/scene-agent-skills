# Local command reference

Run from an activated environment with the repository installed. Commands emit JSON; validation/usage failures return nonzero exit status. All output-producing commands create a new file and refuse overwrite.

| Command | Input | Output / effect |
|---|---|---|
| `scene-agent styles` | None | 16 IDs/names/categories |
| `scene-agent style japandi` | Style ID | Full style record |
| `scene-agent recipe blue-hour --quality high --out recipe.json` | Style, detail profile | Planning recipe; no generation |
| `scene-agent image-check reference.png` | Local image | Encoding, dimensions, decoder result, SHA-256 |
| `scene-agent scale --a 0 0 --b 200 0 --metres 8` | Rectified plan baseline | Metres per pixel |
| `scene-agent plan-check plan.json` | Plan contract | Validity, errors, warnings; exit 2 if invalid |
| `scene-agent ifc plan.json --out model.ifc` | Valid plan | IFC4 with semantic openings/infills |
| `scene-agent max-plan plan.json --out blockout.ms` | Valid plan | Additive wall-cell/slab MAXScript |
| `scene-agent camera-fit landmarks.json --out camera.json` | 3D/2D correspondences | Local fit, residuals, assumptions |
| `scene-agent max-camera camera.json --out camera.ms` | Converged fit | Corona camera transfer script |
| `scene-agent corona --quality review --out review.ms` | preview / review / final | Corona definitions + quality application |
| `scene-agent manifest staging` | Staged directory | Relative paths, sizes, hashes, basename ambiguity |
| `scene-agent package staging --out delivery.zip` | Staged directory | ZIP + internal SHA-256 manifest |
| `scene-agent-mcp` | Workspace environment setting | Local stdio MCP server; see MCP guide |

`recipe --quality` uses `low`, `high`, `very-high`; `corona --quality` uses `preview`, `review`, `final`. Model complexity and renderer sampling are intentionally separate.

The package command must write outside its source directory. It packages exactly what you staged, so review contents and redistribution rights first. Image checks do not rewrite the input. IFC export does not launch Archicad. Camera/Corona scripts do not reset or save your current scene.

See [plan contract](../skills/scene-toolkit/references/bim.md), [camera contract](../skills/scene-toolkit/references/camera.md) and [native quick commands](../skills/scene-toolkit/references/corona.md) for coordinate conventions and host effects.
