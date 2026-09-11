# Contributing

Contributions should make an architectural task more reliable, measurable or easier to repeat.

1. Describe the user problem, host/version and expected result in an issue or pull request.
2. Add a small original or legally redistributable fixture that reproduces the problem.
3. Implement a bounded change, with capability checks for native APIs and explicit units.
4. Run the relevant tests. Include actual output and distinguish skipped/native-unavailable checks.
5. Update the skill/reference, capability matrix and Russian guidance where needed.

Do not add mandatory model providers, paid asset dependencies or automatic uploads to basic workflows. Optional adapters can declare their dependencies and limits. Shared skills should preserve user intent and avoid unnecessary approval rituals.

For a new style, explain its material/light/camera differences and acceptance criteria. The curated release catalogue intentionally has sixteen styles; propose additions or substitutions before changing its contract/test. For native Archicad work, include version, translator/add-on details, editable native element evidence and roundtrip IFC.

Use `evals/trigger-cases.json` for manual host invocation checks. These cases are not automated proof that a model always chooses the right skill. Report host/model and observed routing when contributing results.

By submitting a contribution, you agree to license your original contribution under the repository's MIT licence. Identify any third-party material and its licence separately.
