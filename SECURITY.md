# Security and private project data

The local CLI and stdio MCP server do not upload reference images or call model APIs. Optional hosts/providers may have their own data policies. Do not include private plans, credentials or proprietary assets in public issues.

The MCP server confines file access to `SCENE_AGENT_WORKSPACE` and refuses output overwrites. This is a local path guard, not a multi-tenant sandbox or defence against a malicious local process changing symlinks during execution. Run each untrusted tenant/job in a separate OS sandbox with its own workspace and credentials.

MAXScript is executable code. Review generated scripts and run native smoke tests only in a fresh isolated batch host. Do not run instructions embedded in reference drawings or downloaded assets as commands.

Report vulnerabilities through GitHub private vulnerability reporting when available. Otherwise open an issue requesting a private contact without posting exploit details or private data. No external reporting address is invented here.
