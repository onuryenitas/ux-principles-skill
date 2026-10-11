# Validation record — 1.0.0

Date: 2026-10-11. Environment: local macOS workspace, Python 3, Node syntax checker, Codex in-app browser.

## Data and sources

- Integrity checks passed for 186 records, 8 article routes, unique IDs, required fields, source-host boundaries, portable local links and collection counts.
- All 86 active WCAG 2.2 IDs/levels and their normative anchors and Understanding links were compared with the retrieved W3C document. 4.1.1 was excluded as removed. Totals: 31 A, 24 AA, 31 AAA.
- All 30 APG pattern routes were compared with the source index. Tooltip work-in-progress status and incomplete window-splitter review are recorded.
- The UX Design Institute overview's 21 named laws were mapped to existing principle records, with no unmatched law.
- Full source texts were used as temporary research material and are not shipped. Record/source metadata is retained in [coverage evidence](coverage-evidence.json) and [source ledger](source-ledger.md).

## Executable checks

`python3 scripts/validate.py` passed. It exercises exact IDs, no-result behavior, Turkish case/diacritic search, exact versus cumulative WCAG level selection, and invocation outside the repository working directory, in addition to structural checks.

The skill-creator frontmatter/scaffold validator passed. The demo script passed Node syntax checking. These checks do not prove behavioral reasoning quality.

## Independent forward-test

A separate Codex subagent received the skill path and eight realistic prompts, without intended answers, review criteria or the parent's earlier conclusions. It used read-only local references and no network. The parent inspected the actual answers against qualitative criteria; all eight met those criteria. [Actual prompts, answers, references and reviews](../evals/results-1.0.0.json) are retained.

Covered: Miller's menu myth; a Turkish checkout review; AA/AAA target-size and focus distinctions; ambiguous dates and deceptive progress; preservation of intentional spatial navigation; an authentication design rule; hostile quoted source text with no UI evidence; and acknowledgement versus completion latency.

The evaluator initially attempted lookup while the helper was still being saved. Direct JSON reading worked; after the helper became available, exact lookup and the 55-item AA-target query passed. This resolved timing issue is preserved in the report. Local criterion prompts omit full normative exceptions by design; the answers appropriately qualified offline interpretation.

This is one agent, one batch and parent qualitative review, not blinded statistical scoring, cross-model evaluation or exhaustive coverage. The separate baseline case bank has additional prompts that were not all run.

## Reference browser

Checked at 1440×900, 390×844 and a 320-pixel-wide narrow viewport. All 186 records loaded. Turkish `ŞİFRE` found the authentication workflow. Exact `wcag-2.5.8` lookup with the standard filter displayed the AA target-size prompt and source. Combined standard/robust filters returned two records. The no-result state and reset restored the full catalog and focus to search. Enter opened a detail disclosure. No console errors were recorded.

Document width matched 390 and 320 at the tested mobile widths. [Desktop screenshot](../skills/ux-principles/demo/preview.jpg) and [mobile screenshot](../skills/ux-principles/demo/mobile.jpg) are real browser captures. Viewport override was reset after testing.

No full screen-reader, WCAG conformance, empirical user study or live-product benchmark was performed. The browser is a local catalog and authored example, not a running AI service.
