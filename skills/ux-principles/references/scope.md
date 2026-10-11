# Coverage contract — 1.0.0

This release is a broad web/product UX reasoning and review kit. “Complete” means the named inventories below are covered, not that every idea ever called a UX rule has been collected. UX has no single closed, universally authoritative list. New research and platform guidance require maintenance.

| Inventory | Included | Depth |
| --- | ---: | --- |
| Laws of UX collection | 30 | Original explanation, application, misuse, example and check |
| Laws of UX article routes | 8 | Reading map and original exercise |
| Nielsen heuristics | 10/10 | Original task-specific application and check |
| WCAG 2.2 active criteria | 86/86 | ID, title, A/AA/AAA level, original test prompt and exact normative route |
| ARIA APG patterns | 30/30 at review date | Original keyboard/semantics review prompt and implementation route |
| Practical workflows | 30 | Action, states, caveat, verification and source |

WCAG breakdown: 31 A, 24 AA, 31 AAA. An AA target includes 55 criteria; this is an inventory count, not 55 automatically applicable requirements on every page. The full standard remains authoritative.

The workflows cover forms and identity inputs; review and commitment; completion; accounts and authentication; navigation and search; progressive disclosure and interaction cues; saving and unavailable states; destructive actions; long tasks; support; responsive layout; language and RTL; data presentation; motion; performance; meaningful choice; research; AI uncertainty and reusable design rules.

## Comparing the two supplied sites

[UX Design Institute's article](https://www.uxdesigninstitute.com/blog/laws-of-ux/) is Emily Stevens's overview, dated 30 April 2024. Its 21 named laws are all present in this package's 30-law inventory. It provides a second explanation, not 21 additional distinct rules. The comparison is recorded in [source comparison](source-comparison.json). The article's “all 21” is its editorial scope, not the entirety of UX.

## Outside this release's claim

Native iOS/Android platform specifications, games/XR, industrial and safety-critical interfaces, detailed service operations, a complete research-methods textbook, all empirical psychology, and country-specific legal compliance are not fully catalogued. Apply relevant specialist or platform guidance when a project needs them. The AI workflow is introductory and does not reproduce all HAX guidelines. GOV.UK patterns are source examples; UK wording or service assumptions are not universal defaults.

There is no component implementation library, visual brand pack, hosted AI service or MCP server in this release. It is a self-contained agent skill, portable JSON knowledge collection and local reference browser. A project can combine it with its own design language.

## Maintenance

Every record has a source URL and review date. Before answering a latest-version question or making an exact standards claim, recheck the primary source. Add dated revisions, preserve IDs where possible, and test changed rules. When an inventory changes, update its manifest count and coverage evidence together; do not silently claim continued completeness.
