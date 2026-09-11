# Working on Scene Agent Skills

Keep `skills/` canonical and shared between Codex and Claude. Essential workflow instructions belong in each SKILL.md or its bundled references, not only this repository file.

Preserve the user's requested deliverable. An image, editable DCC scene and semantic BIM model are different outputs. Discover available tools and report executed results separately from generated instructions. Do not invent renderer or Archicad API properties. Probe/version-test native adapters.

Run `python -m pytest -q` after runtime changes. Optional IFC/camera/MCP tests skip when their dependencies are absent; report skips. Native Max testing is isolated and optional, never run the smoke fixture inside an existing user scene. Native Archicad import remains unverified until a documented host test is contributed.

Use original, redistributable fixtures. Do not add customer references, commercial models, credentials or personal machine paths. Keep source units, scale assumptions and geometry limitations explicit. Update English documentation and Russian guidance for user-facing workflow changes.
