# Review method and reusable outputs

## Scope before scoring

Record the users, goal, environment, critical journeys, supplied artifacts and requested coverage. Use a review register with one row per applicable item: **not inspected / observed issue / tested pass / not applicable with reason / unresolved**. A missing feature or unknown state is not automatically a failure. Do not assign pass because no issue was visible.

For each relevant journey, inspect entry, discovery, input, decision, commitment, confirmation, return and recovery. Choose actual states: first use, empty, partial, loading, success, validation error, server failure, offline, permission denied, expired session and cancellation. Record which were exercised. Adapt the list to the task rather than inventing all states for every component.

## Evidence and priority

Keep the exact page/state/action and observation. Distinguish a heuristic risk from a reproducible defect. Assess task impact and availability of recovery; add frequency only when data supports it. Suggested labels are blocker, major, minor and opportunity, with a reason. Do not turn them into a scientific numerical score.

A review finding can use:

- **Context/evidence:** what was supplied or performed, where and in which state.
- **Rule:** ID, source, authority (principle, heuristic, standard, component, workflow).
- **Impact:** observed outcome or explicitly inferred risk.
- **Change:** concrete behavior, preserving required functionality and project style.
- **Verification:** task, environment, expected observable result and current status.

## Accessibility work

Agree the target version and level. For WCAG 2.2 AA, start from all 55 A+AA records and determine applicability. AAA records are available for an enhanced target; do not silently make them AA obligations. 4.1.1 Parsing is no longer active in 2.2; older-version obligations require separate handling.

Read the normative link, including definitions and exceptions, before interpreting a borderline criterion. The local one-line prompts intentionally do not reproduce every normative condition. The Understanding pages are explanatory, not the normative standard.

Inspect complete pages and processes, including responsive variants and relevant third-party content. Record browsers, input methods and assistive technologies actually used. Combine automated checks with manual keyboard, focus, zoom, reflow, content and assistive-technology testing. A passing automated scan is only evidence for what it checked.

Conformance also depends on full pages, complete processes, accessibility-supported use and non-interference. Read [WCAG conformance requirements](https://www.w3.org/TR/WCAG22/#conformance-reqs) before a claim. A selected-component review does not establish page or site conformance. This package is not a jurisdiction-specific legal assessment.

Common distinctions: 24 CSS pixels with exceptions is the 2.5.8 AA target-size criterion; 44 belongs to 2.5.5 AAA. 2.4.11 AA prohibits complete obscuring of a focused component by author-created content; the no-part-obscured requirement is 2.4.12 AAA. Contrast depends on content type, text size and exceptions. Do not treat every visible border as an essential 3:1 boundary.

For custom widgets, prefer suitable native controls. Read the relevant APG pattern and test its keyboard and assistive-technology behavior. APG examples need testing before production use; optional keyboard interactions and platform differences must not be reported as universal failures.

## Design-system rule template

**Name and scope:** component, task, platform, intended users.

**Default:** observable behavior and content; separate visual tokens from interaction rules.

**States:** entry, focus, selection, pending, success, error, disabled and recovery as applicable.

**Exceptions:** when a different design is justified and what must still work.

**Acceptance check:** realistic task, input method, expected result, evidence location.

**Basis:** source IDs, applicable standard version/level, and which decisions are project preferences.

**Maintenance:** owner, last review, affected components and reason for revision.

## Research and measurement

Choose research according to uncertainty: interviews/contextual observation for needs, task tests for usability, navigation tests for findability, and appropriately designed experiments for causal product changes. Recruit relevant users, including people with disabilities where appropriate. Use non-leading tasks and informed consent. Do not manufacture findings from personas or model roleplay.

Define completion, errors, abandonment and time boundaries before measuring. Separate qualitative insight, descriptive metrics and causal evidence. An improvement hypothesis is not a promised lift. AI-generated critique can prepare a test; it cannot impersonate real participants or establish their preferences.
