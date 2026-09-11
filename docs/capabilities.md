# Tools and workflows

Use this guide to choose the right component and prepare its inputs. **Executable tools** perform the operations listed below. **Authoring workflows** guide an agent or operator working in connected software. **Platform design** describes the architecture for a future service.

| Capability | Included component | How to use it |
|---|---|---|
| Shared Codex/Claude skills | 20 SKILL.md files and two plugin manifests | Install in the host; use the supplied prompts to check skill selection |
| 16 style recipes | Structured catalogue and art-direction cards | Apply the recipe with a connected image tool or native scene editor |
| Three modeling levels | Detail profiles and modeling/audit workflows | Model or retopologize in the target application using screen-space targets |
| Raw plan tracing / OCR | Agent/operator workflow | Use an available tracing or OCR tool and check dimensions before export |
| Plan validation and scale calibration | Executable Python | Validate the schema, scale and wall/opening bounds; review scene intersections separately |
| Plan-to-IFC4 | Executable Python | Supply straight walls, rectangular slabs/openings and storeys; receive semantic IFC with simplified infills |
| Plan-to-Max blockout | Executable generator | Create independent closed wall/slab cells, then refine joins and topology in Max |
| Camera solve | Executable Python | Supply non-coplanar 3D/2D landmarks and an initial estimate; uses a centered principal point and zero distortion |
| Corona camera transfer | Executable generator | Apply camera transform/FOV, then compare landmark projections in Max |
| Corona quality/material/light helpers | Executable MAXScript | Run in 3ds Max with Corona; see the [recorded versions](verification.md) |
| LightMix setup | Executable MAXScript | Select light groups; preserve existing AOVs and reject duplicate group names |
| Mesh topology inventory | Executable MAXScript | Inspect evaluated counts, open edges and UVs; use native tools for collision and manifold checks |
| Grass/foliage/furniture | Detailed authoring workflows | Create or supply project assets, then place, scatter and review them in the scene |
| Archicad inventory | Read-only official Python bridge | Connect to a running Archicad project and query element counts |
| IFC import into Archicad / PLN | Native application procedure | Select an IFC translator, import, inspect native types and save/roundtrip the model |
| Asset decoding and packaging | Executable Python | Stage assets, inspect encoding and create a ZIP; enumerate/relink native scene dependencies in the host |
| MCP | Six executable local stdio tools | Connect a compatible client for preparation and file operations; execute native work in the target application |
| Render-farm scheduler / web app | Platform design document | Use the proposed worker and job contracts when developing your own service |

See [installation](installation.md) for software requirements, [commands](commands.md) for executable interfaces and [test results](verification.md) for the recorded evidence. Contributions should pair changes with reproducible examples and the relevant host checks.
