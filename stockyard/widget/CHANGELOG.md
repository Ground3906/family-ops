# Egg Tracker Widget — Changelog

## 2026-05-17 — v2.1
Bug fix release. `window.confirm()` is suppressed inside Claude artifact iframes — Save button on new-breed entries silently failed. Replaced all six `confirm()` call sites with inline `askConfirm()` modal: paper-styled, promise-based, danger flag for destructive actions (deletes, reset-all), backdrop/Escape/Cancel all return false, context-aware focus (Cancel for danger, OK for benign). Fuzzy-match suggestions on new-breed entry now render as clickable buttons — click fills the breed field and dismisses, user clicks Save again to commit. Jumbo Naked Neck renamed to "Turken (Jumbo Naked Neck)" as canonical; "Jumbo Naked Neck" preserved in altNames for autocomplete. Boot-time migration M1 rewrites legacy transactions with old breed name on first load.

## 2026-05-14 — v2
Transaction-based flock model replaces v1 snapshot. Breed system with ~25 seeded breeds, user overrides for advertised data, fuzzy autocomplete. Vacuum projections with reality factor. Three-tier anomaly detection (25-40% / 40-60% / 60%+). Pullet auto-promotion at breed-specific lay onset. Pet-layer flag. Cohort-year tracking with Y1/Y2/Y3/Y4+ production rates. Seven Stockyard hooks documented in code and in stockyard-widget.md spec.

## ~2026-04 — v1 (initial)
Snapshot flock model (Y1/Y2 count split). 60-day production chart with rolling average. Simple molt detection (40-60% / 60%+ drop). CSV import/export. Back-fill calendar.
