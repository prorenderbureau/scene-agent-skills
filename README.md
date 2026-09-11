# Scene Agent Skills

**From architectural references to structured, editable and verifiable scene workflows.**

[English](README.md) · [Русский](README.ru.md) · [Start here](docs/installation.md) · [16 styles](docs/style-catalogue.md) · [20 skills](docs/skills.md) · [What is tested](docs/verification.md)

![Scene Agent workflow](docs/assets/workflow.svg)

An independent, MIT-licensed toolkit for architects, visualizers and agent developers using **Codex, including Astra, and Claude Code**. It combines reusable skills with local tools for camera calibration, plan-to-IFC conversion, Corona setup and asset verification.

The goal is a repeatable process with evidence: preserve the architecture, make assumptions visible, use the right amount of geometry, and verify the result in the target application. **Image generation, editable 3D and BIM are different deliverables.** This toolkit keeps them distinct.

## What you get

| Area | Included |
|---|---|
| Agent skills | 20 shared skills, Codex metadata, Claude plugin and project installers |
| Art direction | 16 style recipes with material, lighting, camera, finishing and review guidance |
| Modeling | Low / high / very-high detail profiles with screen-space targets and topology workflows |
| Camera | Numerical 3D/2D landmark fit, independent holdout errors and Corona camera transfer |
| Atmosphere | 8 lighting recipes: daylight, overcast, golden hour, blue hour, night, rain, interior and clay |
| 3ds Max + Corona | Quick MAXScript commands for quality, Physical Materials, glass, displacement, area lights, LightMix and mesh inventory |
| Plan → BIM | Validated JSON → IFC4 walls, slabs, doors, windows and real opening relationships |
| Archicad | IFC import/roundtrip procedure and official Python read-only inventory bridge |
| Delivery | Image decoding checks, relative-path SHA-256 inventory and dependency ZIP packaging |
| Developer tools | Optional six-tool MCP server, tests, CI, original fixtures and platform architecture notes |

## Start in a few commands

Python 3.11+ is required for the executable tools. Skills can be read without installing Python.

```sh
git clone https://github.com/prorenderbureau/scene-agent-skills.git
cd scene-agent-skills
python -m venv .venv
# Activate .venv for your shell; see installation guide.
python -m pip install -e ".[camera,bim,mcp]"
scene-agent styles
scene-agent plan-check examples/courtyard/plan.json
scene-agent ifc examples/courtyard/plan.json --out outputs/courtyard.ifc
scene-agent corona --quality preview --out outputs/corona-preview.ms
```

The IFC command produces a real model. The Corona command produces a script to run in 3ds Max; it does not start a render. The style command lists recipes; it does not call an image model. Existing output files are never silently overwritten.

Install the skill bundle into an **existing project folder**:

```sh
python tools/install_skills.py --agent both --project /path/to/your-project --dry-run
python tools/install_skills.py --agent both --project /path/to/your-project
```

Codex uses `.agents/skills`; Claude uses `.claude/skills`. The installer keeps shared references together, skips identical files and refuses conflicting local edits. [Plugin installation and Windows instructions →](docs/installation.md)

## Use it with an agent

**Codex:**

> Use $scene-toolkit to reconstruct this reference as an editable architectural scene. Use the first image as the hero camera, keep all openings, use high detail, and report measured versus inferred dimensions. Start with a camera blockout and verify a native render before final delivery.

**Claude Code plugin:**

> /scene-agent-skills:scene-plan-to-bim Convert this dimensioned floor plan into a validated plan and IFC. Preserve the scale evidence, create real openings and give me the Archicad import verification steps.

**Style variation:**

> Use the render-style skill to create blue-hour, Japandi and clay-study alternatives. Keep the building geometry and camera fixed. Deliver images, and state which changes are image-only and which exist in the editable scene.

The skills do not depend on a particular model slug. Choose Astra or your preferred supported Claude model in the host. ChatGPT without local tools does not become a DCC controller merely by reading these files; use a tool-enabled host or connect the optional MCP preparation server.

## The 16 styles

**Lighting:** photoreal daylight · blue hour · golden hour · soft overcast · rainy cinematic · architectural night.

**Design:** Scandinavian · Japandi · warm minimalism · tactile brutalism · contemporary Mediterranean · industrial loft · biophilic tropical.

**Presentation:** clay study · watercolor concept · technical axonometric.

Each [style card](docs/style-catalogue.md) explains what changes, what stays locked, useful starting ranges and the common failure to avoid. Watercolor is an illustration workflow, not a hidden Corona shader.

## Working boundaries

This is a **v0.1.0 toolkit**, not a trained universal image-to-3D model or a finished SaaS. Raster plan tracing and scene construction still need an agent/operator and real host access. The IFC adapter supports straight walls, rectangular slabs and rectangular openings. Native Archicad import/PLN roundtrip is documented but unverified on the authoring workstation.

The local camera solver assumes a centred principal point and no lens distortion. It requires a useful initial estimate and non-coplanar landmarks. A single image cannot establish hidden geometry or exact dimensions without additional evidence.

The package includes original technical fixtures, **no commercial models, client photos or promised photoreal asset library**. Renderer licences, model subscriptions and optional third-party assets are separate. See the [capability matrix](docs/capabilities.md) before choosing a workflow.

## Learn and extend

- [Installation and host setup](docs/installation.md)
- [CLI command reference](docs/commands.md)
- [Complete skill index](docs/skills.md)
- [Plan schema and original courtyard example](examples/courtyard/README.md)
- [Camera input and assumptions](skills/scene-toolkit/references/camera.md)
- [Corona quick commands](skills/scene-toolkit/references/corona.md)
- [MCP setup and tool contracts](docs/mcp.md)
- [Testing and reproducible verification](docs/testing.md)
- [Lessons from reconstruction work](docs/lessons-learned.md)
- [Architecture for a future scene platform](docs/platform-architecture.md)
- [Primary documentation sources](docs/sources.md)

Contributions with small, redistributable fixtures are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md). Code, original examples and documentation are available under [MIT](LICENSE); third-party software and assets retain their own licences.

Maintained by [prorenderbureau](https://github.com/prorenderbureau). Independent community project; not affiliated with OpenAI, Anthropic, Autodesk, Chaos or Graphisoft.
