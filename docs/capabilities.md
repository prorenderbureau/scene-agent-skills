# Capability matrix

| Capability | Implemented in 0.1.0 | Boundary / evidence |
|---|---|---|
| Shared Codex/Claude skills | Yes: 20 SKILL.md files and two plugin manifests | Format validation; model routing needs host evaluation |
| 16 style recipes | Yes: structured catalogue and cards | Art direction; no built-in image generator |
| Three modeling levels | Yes: profiles + modeling/audit workflows | No universal automatic retopology |
| Raw plan tracing / OCR | Agent/manual workflow | No bundled raster detector or OCR service |
| Plan validation and scale calibration | Executable Python | Schema + local wall/opening bounds; not all scene collisions |
| Plan-to-IFC4 | Executable Python | Straight walls, rectangular slabs/openings, simplified infills |
| Plan-to-Max blockout | Executable generator + native smoke | Independent closed cells; not connected production topology |
| Camera solve | Executable Python | Fixed principal point/no distortion; local initial estimate required |
| Corona camera transfer | Executable generator | Host transform/FOV and landmark reprojection checks |
| Corona quality/material/light helpers | Executable MAXScript | Tested host/version in verification report |
| LightMix setup | Executable MAXScript | Existing AOV preservation and duplicate protection; no automatic rig classification |
| Mesh topology inventory | Executable MAXScript | Evaluated mesh counts/open edges/UVs, not full collision or manifold certification |
| Grass/foliage/furniture | Detailed authoring workflows | No bundled asset library or automatic botanical/furniture synthesis |
| Archicad inventory | Read-only official Python bridge | Requires host; native runtime not tested here |
| IFC import into Archicad / PLN | Documented workflow | Requires translator and native editability/roundtrip validation |
| Asset decoding and packaging | Executable Python | Native proprietary dependency discovery/relink is a separate host step |
| MCP | Six real local stdio tools | Preparation/file operations only; no remote Max/Archicad control |
| Render-farm scheduler / web app | Design document | Not implemented in this release |

This matrix is intentionally explicit. A workflow can be useful and detailed without being a one-click implementation. Contributions should upgrade a row only when code and reproducible host evidence support the claim.
