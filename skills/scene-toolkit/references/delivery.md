# A usable scene handoff

Stage `scene/`, `assets/`, `renders/` and `reports/` with a README describing software versions, units, cameras, render settings, project origin, asset licences and known limitations. Keep native sources plus requested exchange formats. Include a low-resolution preview so recipients can identify the scene without opening heavy software.

The packager creates a ZIP with a SHA-256 manifest. It refuses silent overwrite and source/output recursion. It does not create a native scene, rewrite proprietary file references, infer licences or verify renderer plugins.

## Reopening proof

Copy/extract into a different directory, open the native file, enumerate missing assets, inspect proxies/materials and run a small camera render. Compare it to the delivered preview. Record the tested host, date, output size and remaining missing dependencies. If this could not be done, label portability as unverified.

## Delivery statement

Use four short lists: completed and verified; completed but host-unverified; inferred/substituted; incomplete. Distinguish projected background scenery from editable geometry. Preserve uncertainty about dimensions inferred from pictures. Include the next concrete step needed for any incomplete portion.

For free public distribution, publish only original code/examples and redistributable dependencies. Commercial renderer licences, model subscriptions and third-party assets remain separate. This project is an independent community toolkit, not an endorsement or product of Autodesk, Chaos, Graphisoft, OpenAI or Anthropic.
