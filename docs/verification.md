# Verification evidence

Date: **2026-09-11**. Results below describe specific fixtures, not universal reconstruction accuracy.

## Portable tools

Tested locally on Windows with Python 3.12, IfcOpenShell 0.8.5, NumPy 2.5.3, SciPy 1.18.1, Pillow 12.3.0 and MCP SDK 1.30.0. The automated suite covers schema and error paths, real IFC geometry, numerical camera recovery, packaging, installer behavior and a real stdio MCP client session.

The local suite passed **22 tests**. All 20 skills passed the available skill validator; the Codex plugin passed its manifest validator. A wheel was built and installed into a separate directory, where its style data and MAXScript resource were read successfully. Claude Code was not installed on this workstation; its manifest layout follows the official contract and is checked for internal consistency, not claimed as a native Claude CLI validation.

The courtyard south wall has 4.8 m³ gross volume and **3.61 m³ after openings**; the test independently tessellates the IFC wall and checks that volume. IFC units, containment, filling/void relations and elevated placements are checked. This is stronger than merely confirming that an `.ifc` file was written.

The camera test recovers a synthetic known camera and evaluates four held-out points. A deliberately corrupted held-out point fails the independent check while training error remains small. It is not a benchmark on arbitrary photographs.

## Native Corona

Tested in **3ds Max 2024.1**, Corona **15.0.671720**, in an isolated fresh batch process. [Machine-readable report](evidence/native-corona.json).

- All three quality presets applied and were read back.
- Physical material roughness mode and solid glass were checked.
- Signed millimetre displacement bounds converted correctly to scene units.
- Plan blockout created 27 closed, UV-mapped wall/slab cells.
- Camera position/FOV, explicit free-camera/FOV-source mode and host landmark reprojection were checked.
- Maximum host camera reprojection error on the synthetic fixture: approximately **0.000124 px**.
- Existing render elements survived LightMix setup; duplicate SA groups were rejected.
- A real 320 × 240 Corona PNG was produced in approximately 6.9 seconds of measured render-call time.

![Actual native Corona technical fixture](evidence/native-corona-fixture.png)

This low-sample technical render uses original simple geometry, not a commercial asset or a photoreal showcase. LightMix configuration is verified; AOV image quality and large production scenes require additional testing. Other Max/Corona versions are not certified by this fixture.

## Not yet verified

- Native Archicad import, native element editability and PLN/IFC roundtrip.
- Claude/Codex behavioral routing across model versions (manifests and files are validated separately).
- Arbitrary photo reconstruction, automatic raster tracing, production retopology or automated vegetation/furniture synthesis.
- Multi-tenant cloud deployment, render-farm scheduling and third-party asset licence compliance.

For reproduction see [testing.md](testing.md). For implemented versus instructional coverage see [capabilities.md](capabilities.md).
