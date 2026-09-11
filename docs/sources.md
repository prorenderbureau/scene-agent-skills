# Primary documentation

Reviewed on **2026-09-11**. The guides are original practical synthesis, not copies of vendor manuals. API surfaces and installation formats can change; probe the installed version and update verification evidence.

| Source | Used for |
|---|---|
| [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | SKILL.md structure and `.agents/skills` discovery |
| [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Tool-enabled model context; no hardcoded API dependency |
| [Claude Code plugins reference](https://code.claude.com/docs/en/plugins-reference) | `.claude-plugin` manifest and shared root skill layout |
| [Claude Code plugins](https://code.claude.com/docs/en/plugins) | Local plugin loading and namespaced invocation |
| [Claude plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) | Repository marketplace distribution |
| [Chaos: Corona MAXScript](https://docs-chaos.atlassian.net/wiki/spaces/CRMAX/pages/124394405/MAXScript) | Native scripting approach; actual property support tested in host |
| [Chaos: Corona Physical Material](https://docs-chaos.atlassian.net/wiki/spaces/CRMAX/pages/124758873) | Physical material workflow and parameter interpretation |
| [Graphisoft Archicad Python API](https://archicadapi.graphisoft.com/archicadPythonPackage/archicad.html) | Official connection/query API and inventory boundary |
| [Graphisoft IFC import model filtering](https://help.graphisoft.com/AC/28/INT/_AC28_Help/121_IFC/121_IFC-25.htm) | Translator/import filtering considerations |
| [IfcOpenShell wall representation API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/geometry/add_wall_representation/index.html) | SI wall representation and IFC geometry |
| [Official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | Local stdio server/client; versioned SDK boundary |
| [MCP Python SDK v1 documentation](https://py.sdk.modelcontextprotocol.io/v1/) | Supported v1 interface used by this release |

The exact successful runtime versions are in [verification.md](verification.md). Native Archicad results are not inferred from the existence of its documentation. Material ranges and visual acceptance criteria are authoring heuristics and should be refined using real project measurements.
