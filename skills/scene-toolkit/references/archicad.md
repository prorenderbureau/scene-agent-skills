# Archicad handoff and verification

Use the official Graphisoft IFC import mechanism with a translator appropriate to the target Archicad version and intended native element mapping. The standard Python connection is not assumed to expose arbitrary wall creation commands. The bundled `archicad_inventory.py` script calls `ACConnection.connect()` and `GetElementsByType` for a read-only count; it does not import IFC or create walls.

## Import procedure

1. Keep the generated IFC and its source plan/report together. Open a new Archicad project or a separate test copy of the destination.
2. Open/merge the IFC using the target version's supported IFC translator. Record translator name and options, including model filtering and geometry/type conversion.
3. Inspect SI units, project origin, storey names/elevations and building orientation. Measure a known wall length and one opening.
4. Inspect Wall/Slab/Door/Window classification. A visible imported element may be a Morph or Object instead of an editable native building tool element; report that distinction.
5. Verify real wall voids, door/window association, height/sill and slab elevation. Check sections and plan views, not just 3D shading.
6. Save a new PLN if requested. Export a roundtrip IFC and compare counts, dimensions and opening geometry.

## Python inventory

Install Graphisoft's official `archicad` package in an appropriate environment, start a supported Archicad host and open the test project. Run the bundled [inventory script](../scripts/archicad_inventory.py). A missing host is a clear unavailable state; do not synthesize successful counts. Counts alone do not prove native editability or a correct import.

This release's native Archicad import and PLN roundtrip have not been tested on the authoring workstation. IFC schema, units and geometry are tested independently. A future native creation adapter can use a documented Archicad C++ add-on command surface; it needs its own versioned contract and regression fixtures rather than invented Python methods.
