# Optional local MCP server

The server uses the official MCP Python SDK's supported v1 API, pinned below 2. It communicates over **stdio** and provides six tools. It does not expose an HTTP listener, call a paid model, upload images or execute arbitrary host code.

Install with `python -m pip install -e ".[mcp,bim]"`. For a local client configuration, use the executable paths from your own virtual environment:

```json
{
  "mcpServers": {
    "scene-agent": {
      "command": "/absolute/path/to/.venv/bin/python",
      "args": ["-m", "scene_agent.server"],
      "env": {
        "SCENE_AGENT_WORKSPACE": "/absolute/path/to/project"
      }
    }
  }
}
```

On Windows the command is the absolute `.venv\\Scripts\\python.exe` path, JSON-escaped as needed. This is a generic `mcpServers` example used by compatible clients; hosts with another configuration schema require its documented equivalent. The repository does not modify your host configuration automatically.

| Tool | Parameters | Effect |
|---|---|---|
| `list_styles` | None | Style IDs/names |
| `get_scene_recipe` | `style_id`, `quality` | Recipe JSON only |
| `check_plan` | `relative_path` | Read/validate plan inside workspace |
| `export_plan_ifc` | `relative_plan`, `relative_output` | Create new IFC4 inside workspace |
| `prepare_corona_script` | `relative_output`, `quality` | Create new MAXScript; never execute it |
| `inspect_reference` | `relative_path` | Decode/check local image; never upload it |

File paths are resolved against `SCENE_AGENT_WORKSPACE` (default current working directory) and checked after symlink resolution. Paths leaving that directory are rejected. Output files cannot be silently replaced. Select a narrow project directory, not your whole home directory.

The path guard is not a multi-tenant isolation layer. A future web platform needs separate worker sandboxes, authentication, quotas and per-job credentials. There is no arbitrary Python/MAXScript eval tool in this server. A native DCC bridge should be added as a separate versioned adapter with allowlisted operations and real job status/cancellation.

The regression test launches a real stdio client, initializes the session, lists tools, calls successful operations and verifies path/overwrite failures. That is protocol evidence; it does not prove native DCC execution or every host's UI integration.
