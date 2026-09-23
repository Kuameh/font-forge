# Pitfalls

Mistakes made (or nearly made) in this repo, and the rule that prevents each. Add one whenever something bites. Newest at the bottom; never delete — mark obsolete instead.

| # | What went wrong | Rule |
|---|---|---|
| 1 | A master drawn at weight 800 was named "Bold", while the designspace also had a Bold *instance* at 700 — two things called Bold at different weights. | Name masters by their real location on the axis (800 = ExtraBold). Masters and instances share one naming scale. |
| 2 | *(Design rule.)* Masters that differ in contour count, point count, point order or start point can't interpolate — fontmake fails, or worse, letters twist mid-axis. | Every glyph has the same structure in every master. Change one master → change all. Check the slider in the specimen from end to end. |
| 3 | *(Design rule.)* A designspace whose default location isn't a master fails to build a variable font. | `default` on each axis must equal some master's location. |
| 4 | *(Design rule.)* Re-running a scaffold script over UFOs that someone has edited wipes their work. | Scaffold scripts run once and aren't committed (ADR-0002). Later global changes are deliberate one-off scripts, reviewed as a diff. |
| 5 | *(Design rule.)* Outline direction: UFO/PostScript outer contours go counter-clockwise, counters (holes) clockwise. Get it wrong and holes fill in or overlap removal eats shapes. | Keep outer = CCW, inner = CW. Editors' "correct direction" command does this. |
| 6 | *(Process rule.)* Editing sources without rebuilding leaves `fonts/` and the specimen lying. | Every source change ships with `make build` output in the same commit (ADR-0004). |
| 7 | *(Process rule.)* Opening `specimen/index.html` directly (file://) shows fallback fonts and looks like a broken build. | Use `make serve`. |
| 8 | A `sample` in `family.toml` used an em dash and a colon the font doesn't have; the specimen silently drew them in Inter. | Build `sample` only from characters in the font's character grid. |
| 9 | *(Process rule.)* Plain `make build` rewrites every family's binaries even when their sources didn't change (builds aren't byte-reproducible yet), which makes noisy diffs. | Rebuild only what you changed: `make build FAMILY=<Dir>`. Revert untouched families' `fonts/` before committing. |
