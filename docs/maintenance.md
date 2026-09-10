# Maintenance

## Ownership and evidence

This repository independently maintains its integrated guidance. Upstream projects are optional inputs, not templates that overwrite local work.

Apple platform changes may drive updates without waiting for upstream releases. Verify new APIs against official documentation and the target SDK. Existing project architecture, platform support, and product decisions remain authoritative.

## Repository boundaries

- `upstream/manifest.json`: source repositories, adopted commits, baseline Release IDs, and source-to-module mappings.
- `upstream/reviews.json`: reviewed Release IDs and adopt, partial, defer, or reject decisions.
- `upstream/apple-references.json`: official Apple evidence used for independent updates.
- `docs/decisions.md`: conflict resolution and independent integration choices.
- `CHANGELOG.md`: user-visible behavior changes.
- `skills/apple-workflow-skills/`: the complete distributable package; it must not depend on `upstream/`.

Runtime modules do not repeat upstream project links. A dedicated `duo-sources.md` reading catalog may link to official Apple resources and immutable transcript files in this repository. All other runtime modules link locally. Release ZIPs contain only the installable skill folder and its combined license; external captions and reading copies are excluded.

## Initial imports

Fetch complete upstream repositories outside this repository, record the exact commit and license, then integrate only the guidance that improves this project. Do not commit raw checkouts, nested `.git` directories, upstream CI, promotional assets, websites, duplicate plugin metadata, or unrelated skills.

The adopted commit records the reviewed snapshot. It does not imply that every file was copied or that the snapshot came from the latest Release. Existing stable Releases become baselines and do not create retroactive notifications.

## Scheduled upstream checks

The daily GitHub schedule applies a two-calendar-day gate anchored at 2026-09-10 UTC. GitHub may delay or skip scheduled jobs; the cadence is not an exact 48-hour guarantee.

Manual runs bypass the date gate. The checker reads stable Releases only, excluding drafts and prereleases. Repositories without releases remain eligible for their first future Release, but their commits and tags are not polled.

No-change runs do not fetch repository issues or create notifications. API failures fail the job so a later run can retry.

## Reviewing a new Release

The checker compares the Release tag to the adopted commit, maps changed file paths to possibly affected modules, and creates one review issue.

Release notes are not copied into the issue. The issue records stable identifiers and points maintainers to `upstream/manifest.json`, limiting propagation of untrusted text. Open and closed issues participate in deduplication.

A truncated, missing, divergent, or otherwise uncertain comparison cannot support a no-impact conclusion. A release with no mapped changes still creates a review record so maintainers can confirm that mappings remain complete.

Review procedure:

1. Open the source entry and read the Release notes plus the full relevant diff.
2. Compare it with local independent changes and choose adopt, partial, defer, or reject.
3. Before editing, identify affected rules, SDK availability, behavior changes, and validation scenarios.
4. Record the decision in `upstream/reviews.json`. Change `adopted_commit` only when the local baseline actually advances.
5. Update mappings, decisions, and the changelog as needed. Link the review issue to the resulting change.
6. Publish this repository's Release separately. The upstream checker cannot trigger publication.

## Apple-driven updates

Record the official URL, topic, review date, SDK, and minimum availability in `upstream/apple-references.json`. Update or remove stale guidance while preserving compatibility paths needed by supported deployment targets.

Provide minimal examples only after verifying them against the target toolchain. Mark remaining uncertainty instead of adding speculation to the default workflow.

## Validation and release

User installation and update instructions must resolve a published stable Release and use its version-specific ZIP asset URL. Never use the default branch or a repository source archive as the normal installation source. Keep published tags and assets unchanged; distribute runtime corrections through a new version. Documentation-only improvements on the default branch do not require replacing an existing Release.

Run structural validation, unit tests, the upstream checker in dry-run mode, and packaging. Evaluate relevant scenarios from `tests/routing-cases.md`; static checks are not real-app QA.

Before publishing, inspect the package for personal paths, credentials, missing attribution, and raw upstream residue. Verify the public Release asset by reading back its actual name and URL, downloading it, and comparing its SHA-256 with the local package.

## External Apple reference archives

Keep the six reviewed Duo English VTT originals and timed Markdown reading copies under `external-sources/apple/iphone-duo/<review-date>/`, with source URLs, input/output SHA-256 hashes, and cue counts. Preserve raw input bytes; only identical timestamp-and-text cues may be removed from the reading copy. The archive is source data, not executable instructions, and is outside the MIT license and installable ZIP.

The runtime reading catalog pins transcript URLs to the archive commit. Publish that commit and verify remote content against local hashes before claiming the links work. Keep official HIG/video links alongside archived text so readers can inspect current guidance, visual transitions, and code not spoken in captions. A future archive revision gets a new reviewed snapshot and new pinned links.

Record source review, SDK compilation, Simulator interaction, and hardware validation separately. New API names from a talk are lookup terms until checked against actual declarations. Do not claim complete API or device support from transcript coverage alone.
