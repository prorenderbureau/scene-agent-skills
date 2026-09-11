# Testing

## Portable runtime and bundle

```sh
python -m pip install -e ".[dev,camera,bim,mcp]"
python -m pytest -q
python -m pip wheel . --no-deps --wheel-dir dist
```

Tests cover valid/invalid plans, independent wall volume after IFC openings, IFC EXPRESS validation, SI units, hierarchy, stable wall IDs, elevated storey placement, synthetic camera recovery, held-out landmark failures, false image extensions, package hashes/collisions, path confinement, actual MCP handshake/tool calls, installation conflicts and Markdown links.

Optional dependencies missing from an environment cause the related tests to skip. Report skips rather than claiming full coverage. CI includes Windows/Linux Python 3.11/3.12 core/camera/MCP jobs and an IFC job on Linux. A workflow file is not evidence that a run passed; inspect the actual run.

## Native 3ds Max / Corona fixture

This test is only for a new isolated `3dsmaxbatch.exe` process with an empty scene. It never belongs inside an interactive user project. The script rejects a non-empty scene and requires an explicit environment flag. It creates original wall/slab geometry, materials, lights and cameras, saves a technical fixture and renders a small PNG.

Prepare input files inside repository `outputs/native-input` using the CLI: `max-plan` from the courtyard example, `camera-fit` from the camera example, then `max-camera`. Use filenames `plan.ms`, `camera.json`, `camera.ms`.

Create a small launcher MAXScript containing `python.ExecuteFile @"ABSOLUTE_PATH_TO_REPOSITORY/tools/native_max_smoke.py"`. In the batch process environment set `SCENE_AGENT_ISOLATED_BATCH=1` and `SCENE_AGENT_NATIVE_OUTPUT` to a new output directory. Launch the installed `3dsmaxbatch.exe` with the launcher filename and `-log` output path. Keep the worker hidden/background where supported; do not attach it to an existing user process.

Read `native-report.json`, decode `fixture.png` and inspect its contents. Check host/plugin versions and camera landmark reprojection. The fixture intentionally uses low sampling and clay geometry; it proves native execution, not photoreal quality. LightMix configuration and preservation are tested; the preview render disables extra AOV output buffers and is not a full LightMix image-quality benchmark.

## Native Archicad

Not available on the authoring workstation. Follow the import procedure, record native classifications/dimensions and perform a roundtrip IFC. Add a host/version/translator report before claiming this portion is verified.

## Skill routing

`evals/trigger-cases.json` contains positive and negative prompts. Run them in each target agent host and record observed skill choices and resulting artifacts. File/schema validation does not establish model behavior. No automatic multi-model routing evaluation is claimed in this release.
