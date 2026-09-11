# Installation

## 1. Get the repository and local tools

```sh
git clone https://github.com/prorenderbureau/scene-agent-skills.git
cd scene-agent-skills
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```sh
# macOS / Linux
source .venv/bin/activate
```

If PowerShell activation is restricted, call `.\.venv\Scripts\python.exe` and `.\.venv\Scripts\scene-agent.exe` directly; no machine-wide execution-policy change is necessary.

```sh
python -m pip install -e ".[camera,bim,mcp]"
scene-agent --help
```

Minimal tools: `python -m pip install -e .`. Extras: `camera` adds NumPy/SciPy; `bim` adds IfcOpenShell 0.8.5; `mcp` adds the supported 1.x MCP SDK line (`<2`). The MCP SDK now has a separate 2.x API; this release deliberately pins its tested v1 interface. Development adds `.[dev]`.

Install this project from the Git checkout with `python -m pip install -e ".[camera,bim,mcp]"` as shown above. This is the distribution route for Scene Agent Skills.

## 2A. Codex project skills

```sh
python tools/install_skills.py --agent codex --project /absolute/path/to/project --dry-run
python tools/install_skills.py --agent codex --project /absolute/path/to/project
```

Use an existing project folder; on Windows, for example `--project "C:\Projects\Villa"`. Start Codex in that project and invoke `$scene-toolkit` or a specific skill. Codex discovers project skills under `.agents/skills`. Restart/rescan the host if the new skills do not appear.

The repository also ships a `.codex-plugin/plugin.json` manifest for compatible Codex plugin distribution. The project-copy route does not require modifying a personal marketplace or global configuration. User-wide installation is a separate explicit choice; this installer intentionally targets one project.

## 2B. Claude Code plugin

For a local checkout:

```sh
claude --plugin-dir /absolute/path/to/scene-agent-skills
```

For GitHub marketplace installation, inside Claude Code:

```text
/plugin marketplace add prorenderbureau/scene-agent-skills
/plugin install scene-agent-skills@scene-agent-skills
```

Invoke `/scene-agent-skills:scene-toolkit` or another namespaced skill. The repository includes `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`; skills remain at root `skills/`.

Alternatively install project skills with `--agent claude`; use the project's normal skill invocation, without the plugin namespace. Choose either the plugin or project-copy route to avoid duplicate discovery. Install the Python CLI dependencies and the native programs required by your workflow separately.

## 3. Native programs

3ds Max is required to execute MAXScript; Corona is required for Corona classes and rendering. The portable Python tools can run on Windows, macOS or Linux with supported dependency wheels. Archicad needs its own installation and suitable IFC translator. The read-only bridge additionally requires the official `archicad` Python package.

Select your model in the agent host. The skills support tool-enabled Codex/Astra and Claude Code workflows without embedding an API key or forcing a particular model version. ChatGPT and Claude web interfaces have different file/tool integration capabilities; copying a skill into chat is not equivalent to native plugin installation.

## Updating

Update the Git checkout and Python environment, then run the installer in dry-run mode. Identical skills are skipped. If installed files differ, the installer stops before copying anything; back up local edits and merge deliberately. There is no automatic destructive updater or global uninstall script.
