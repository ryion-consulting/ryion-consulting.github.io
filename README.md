# RyionSite

The public website for every Ryion app: product pages, how-to guides, and the
privacy policies and support pages App Store Connect requires. It is served
as one static site (GitHub Pages), with one folder per app.

```
build.py                   Writes every page below from site/ (python3 build.py)
site/content.py            Copy for the home page and the three product pages
site/pages/<App>/*.html    Copy for the guides, FAQ, support and privacy pages
almanac.css, almanac.js    The one stylesheet and script every page uses
index.html                 Ryion home                                   (generated)
appstore.html              App Store media, for review on this Mac only (generated)
.nojekyll                  Serve files as they are (no Jekyll), for every folder
BillCompass/               Bill Compass (iPhone, iPad, Mac)
WhereaboutsCompass/        Whereabouts Compass (iPhone, iPad)
CinematicTeleprompter/     Cinematic Teleprompter (iPhone, iPad)
```

Every `.html` page is generated: edit `site/`, then run `python3 build.py`
and commit both. The design is "Almanac": paper and ink, one serif
(Fraunces), hairline rules, and each app in its own colour. Each app folder
holds its pages, `assets/icon.png`, the screenshots in `assets/screens/`
and its App Store media. Links are relative, so the site works at any
address, whether that is `<org>.github.io/RyionSite/`, a `<org>.github.io`
repository, or a custom domain.

The page addresses are fixed: the apps link to their privacy pages
(Cinematic Teleprompter's paywall opens `CinematicTeleprompter/privacy.html`),
and App Store Connect holds the support and privacy URLs.

## Pages per app

| App | Product page | Privacy policy | Also |
| --- | --- | --- | --- |
| Bill Compass | `BillCompass/index.html` | `BillCompass/privacy.html` | features, guide, sync, FAQ, support |
| Whereabouts Compass | `WhereaboutsCompass/index.html` (includes How to Use and FAQ) | `WhereaboutsCompass/privacy.html` | `support.html` |
| Cinematic Teleprompter | `CinematicTeleprompter/index.html` (includes How to Use, Pricing and FAQ) | `CinematicTeleprompter/privacy.html` | `support.html` |

The product pages' copy is in `site/content.py`; every other page's is its
fragment in `site/pages/<App>/`, plain HTML with a title and description
comment at the top.

## App Store media

Each app's `AppStore/` folder holds the screenshots that get uploaded to App
Store Connect:

| Folder | Spec |
| --- | --- |
| `Screenshots/iPhone-6.9/` | 1320 × 2868 PNG, no alpha (6.9" display, accepted for every iPhone size) |
| `Screenshots/iPad-13/` | 2064 × 2752 PNG, no alpha (13" display, accepted for every iPad size); Bill Compass's are landscape, 2752 × 2064 |
| `Screenshots/Mac/` | 2880 × 1800 PNG, no alpha (Bill Compass only) |

Files are numbered in the order they should appear on the App Store (up to 10
screenshots per device size).

The App Preview videos are too large for this repo and live outside it, in
`~/Documents/App Store Artifacts/<App Name>/App Previews/` (`iPhone-6.9.mp4`:
886 × 1920; `iPad-13.mp4`: 1200 × 1600; both 30 fps, H.264 High, silent stereo
AAC 256 kbps, 15–30 s).
The home page's gallery plays them through `_artifacts`, a git-ignored link to
that folder, so they show only when previewing on this Mac. Where the link is
missing, such as on the public site, each video removes itself from the
page. To recreate the link:
`ln -s ~/Documents/"App Store Artifacts" _artifacts`.

They come from Debug builds on the Simulator, never from real data. Whereabouts
Compass uses `-WCDemoData`, and Cinematic Teleprompter uses `-debugSampleLibrary`
with `-debugMockCamera`. The Simulator has no camera, so the recorder's
"camera feed" is an AI-generated photo of a person (made locally with
Z-Image-Turbo, upscaled with SeedVR2; both Apache-2.0, run 8-bit through
mflux so they fit in 16 GB). The portrait is slid down so the face sits below
the script card, and an image-to-image pass paints the background above it.
A scratch, Debug-only patch of the app draws it under the recorder UI, and
gives the sample library scripts that read naturally. For Cinematic,
Vision separates the person from the background and the background is blurred,
and a focus box is drawn on the face. Nobody real appears. An XCUITest drove each app for the
previews while `xcrun simctl io recordVideo` recorded the screen. The
recordings were then cut, scaled to the preview size and re-encoded with
AVFoundation. The status bar is fixed at 9:41 with full signal and battery.
Bill Compass's screenshots come from the app's own screenshot mode
(`-BCScreenshotMode` with `-BCSection`, `-BCInspectBill`, `-billLayout` and
`-BCUnrecorded`, all Debug-only), which seeds a made-up household into a store
of its own. The Mac shots are taken by the app itself
(`-BCSnapshotSize 1440x900 -BCSnapshotDescriptor 3`, on a 2× display), and
their transparent window corners are squared off from the neighbouring pixels.
The iPad must be set to **Full Screen Apps** (Settings → Multitasking &
Gestures); in Windowed Apps mode the status bar shows the app's name and a
resize grip sits in the corner.

`appstore.html` is a review page for all of this media: each screenshot as a
thumbnail linking to the full PNG, and the App Preview videos. It is linked
from the footer only where `_artifacts` (see above) is reachable, so on the
local preview server, not on the public site. `build.py` makes the thumbnails
in `<App>/assets/store/` with `sips` whenever a PNG is newer, and removes
those whose PNG is gone.

## Writing the copy

Every claim on these pages was checked against the app's source rather than
assumed. Menu items, buttons and settings are named exactly as the app shows
them, so a reader can find what a page points to. When an app changes what
it stores, sends or asks permission for, update its privacy page and the date
at the top of it.

## Adding an app

1. Make a folder named after the app, e.g. `NewApp/`, with `assets/icon.png`
   (256 px) and its screenshots in `assets/screens/`.
2. Add it to `APPS` in `site/content.py`, and give it a colour: a `hue-…`
   class in `almanac.css` (light and dark).
3. Add `site/pages/NewApp/privacy.html` and `support.html` (App Store Connect
   asks for a support URL), and list them in `DOC_PAGES` in `build.py`.
4. Run `python3 build.py`.

## Previewing

```
python3 serve.py
```

Then open <http://localhost:8000/>, and <http://localhost:8000/appstore.html>
for the App Store media. `serve.py` is `python3 -m http.server`
plus byte-range support, which Safari needs to play the App Preview videos.
