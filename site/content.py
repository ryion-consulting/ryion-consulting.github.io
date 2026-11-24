"""The words and pictures for the home page and the three product pages.

`build.py` renders them; the longer pages (guides, FAQs, support and privacy)
are HTML fragments in `site/pages/`. Every claim was checked against the
app's source, and buttons and settings are named exactly as the app shows
them. In paths, `{L}` is the app's folder as seen from the page being built
("" on the app's own pages, "BillCompass/" from the home page) and `{A}` is
its assets folder.
"""

PRINCIPLES = [
    ("Accounts", "None"),
    ("Ads", "None"),
    ("Analytics", "None"),
    ("Third-party code", "None"),
    ("Your data", "On your device, and in your own iCloud"),
]

HOME = dict(
    title="Ryion — apps for iPhone, iPad and Mac",
    desc="Small, private apps for iPhone, iPad and Mac: Bill Compass, Whereabouts Compass and Cinematic Teleprompter. No accounts, no ads, no analytics.",
    h1=["Small apps that", "keep to themselves"],
    lead="Each one does a single job well. No accounts, no ads, no analytics, and your data stays with you.",
)

BILL = dict(
    slug="bill-compass", dir="BillCompass", name="Bill Compass", short="Bill Compass", no="01", hue="coral",
    platforms=["iPhone", "iPad", "Mac"], extra=None,
    blurb="Every bill you owe in one calm list, with reminders before each one is due.",
    title="Bill Compass — never miss a bill again",
    desc="Bill Compass tracks every bill you owe on iPhone, iPad and Mac. No account, no analytics, and it syncs through your own iCloud.",
    h1="Never miss a bill again",
    tagline="Every bill you owe, in one calm list — and a month you can see coming.",
    icon_alt="The Bill Compass app icon",
    ctas=[("How to use it", "{L}guide.html"), ("See every feature", "{L}features.html")],
    nav=[("Features", "{L}features.html"), ("How to Use", "{L}guide.html"), ("Sync", "{L}sync.html"), ("FAQ", "{L}faq.html"), ("Support", "{L}support.html")],
    foot=[("Features", "{L}features.html"), ("How to Use", "{L}guide.html"), ("iCloud Sync", "{L}sync.html"), ("FAQ", "{L}faq.html"), ("Support", "{L}support.html"), ("Privacy", "{L}privacy.html")],
    footline="Bill Compass — for iPhone, iPad and Mac",
    hero=[("{A}screens/iphone-overview.jpg", "The Overview: bills listed soonest first, each with its amount and how many days are left"),
          ("{A}screens/iphone-overview-dark.jpg", "The same Overview in dark mode")],
    hero_dark=[("{A}screens/iphone-overview-dark.jpg", "The Overview in dark mode: bills listed soonest first, each with its amount and how many days are left"),
               ("{A}screens/iphone-calendar.jpg", "The Calendar: the month laid out by date, with the bills due listed below")],
    facts=[("Add each bill once", "Name, amount, due date and how often it repeats."),
           ("Let it remind you", "A notification before each bill falls due."),
           ("Touch and hold to pay", "Record the payment and the bill rolls on to its next date.")],
    sections=[
        dict(kind="three", id="habits", label="Start", title="Three habits, and you are done", items=[
            ("Add each bill once", "Name, amount, due date and how often it repeats. Bill Compass works out every date after that."),
            ("Let it remind you", "A notification before each bill falls due, as early as you like — the day of, or up to two weeks ahead."),
            ("Touch and hold to pay", "Record the payment and the bill rolls on to its next date. Automatic payments record themselves."),
        ], after='<a href="{L}guide.html">Read the full How to Use guide →</a>'),
        dict(kind="features", id="features", label="Features", title="What it does", items=[
            ("Overview", "Everything still owed, grouped by when it falls due, under a chart of the next 30 days. As a timeline, a list, a grid, or a wall of paper notes.", "{L}features.html#overview"),
            ("Calendar", "The month laid out by date, so a heavy week is visible before it arrives.", "{L}features.html#calendar"),
            ("Reports", "What the next 30, 60 and 90 days cost, what each category takes over a year, and what you have paid so far.", "{L}features.html#reports"),
            ("History", "Every payment you have recorded, grouped by month, including part payments and skipped cycles.", "{L}features.html#history"),
            ("Tags", "Group bills your own way — Essentials, Household, Family — and see what each group costs.", "{L}features.html#tags"),
            ("Reminders", "A notification before a bill is due, with the lead time set per bill, and Record Payment and Skip right on it.", "{L}features.html#reminders"),
        ]),
        dict(kind="gallery", label="Screens", title="A month you can see coming", items=[
            ("{A}screens/iphone-calendar.jpg", "The Calendar: the month laid out by date, with the bills due listed below", "Calendar"),
            ("{A}screens/iphone-reports.jpg", "Reports: the next 30, 60 and 90 days, and a yearly projection by category", "Reports"),
            ("{A}screens/iphone-history.jpg", "History: payments grouped by month, each marked paid in full or as a partial payment", "History"),
            ("{A}screens/iphone-tags.jpg", "Tags: each group of bills with what it costs per year", "Tags"),
        ]),
        dict(kind="features", id="nudge", label="Reports you can trust", title="Nothing slips past",
             lead="Reports are only as good as the payments recorded in them, so Bill Compass asks about the ones that were missed.",
             items=[
                ("Paid? Not recorded yet", "A bill a few days past due with no payment recorded says so, rather than calling itself overdue.", None),
                ("Record Past Bills", "A banner on the Overview and in Reports opens one list of them: record a payment for each, or skip a cycle you didn't pay.", None),
                ("Asked the day after", "If a bill still isn't recorded the day after it's due, a reminder asks whether you paid it.", None),
                ("Wrap Up each month", "On the 1st, one reminder lists anything last month left unrecorded.", None),
             ]),
        dict(kind="spread", label="iPad and Mac", title="Room to spread out on iPad and Mac",
             lead="A sidebar with your tags in it, the details of a bill beside the list, and a choice of layouts — a timeline, a list, a grid, or a board of paper notes.",
             after='<a href="{L}features.html#layouts">More about layouts →</a>',
             figures=[("{A}screens/mac-overview.jpg", "Bill Compass on a Mac: bills grouped by when they fall due in two lanes, with the details of Rent open beside them", "On the Mac: the timeline, with Bill Details", 1400, 875),
                      ("{A}screens/ipad-stickie.jpg", "Bill Compass on iPad, with bills laid out as paper notes and tags in the sidebar", "On iPad: a board of paper notes", 1400, 1050)]),
        dict(kind="pledge", id="sync", label="Sync and privacy", title="It syncs, and it stays yours", pledges=[
            ("Privacy", "Bill Compass has no account, no server of ours, and no analytics. Your bills live on your device and sync through <b>your own iCloud</b>, which we cannot read. Nothing is collected, and nothing is sold.", "green"),
            ("One-time purchase", "<b>Lifetime iCloud Sync — $7.99.</b> Bill Compass works fully on a single device. Keeping the same bills on your iPhone, iPad and Mac is the one thing that costs, and it is bought once — not a subscription. It unlocks on every device signed in to the same Apple Account.", "hue"),
        ], lead="Add a bill on your phone and it is on your Mac. Appearance stays per device on purpose — a Mac on a desk and a phone in bed are entitled to different answers.",
           after='<a href="{L}sync.html">How iCloud sync works</a> · <a href="{L}privacy.html">Read the full privacy policy</a>'),
    ],
)

WHERE = dict(
    slug="whereabouts-compass", dir="WhereaboutsCompass", name="Whereabouts Compass", short="Whereabouts", no="02", hue="terra",
    platforms=["iPhone", "iPad"], extra="Free",
    blurb="Which countries you were in, and on exactly which dates, ready for immigration and tax forms.",
    title="Whereabouts Compass — travel history and day count",
    desc="Whereabouts Compass keeps a dated record of every country you visit, rebuilds past trips from your photos, and exports it when an immigration or tax form asks. Free, with no account and no analytics.",
    h1="Which countries, and exactly when?",
    tagline="Your travel history, kept quietly in the background and ready when a form asks for it.",
    icon_alt="The Whereabouts Compass app icon",
    ctas=[("How to use it", "#how"), ("Privacy", "{L}privacy.html")],
    nav=[("How to Use", "#how"), ("Good to Know", "#limits"), ("FAQ", "#faq"), ("Support", "{L}support.html"), ("Privacy", "{L}privacy.html")],
    foot=[("How to Use", "#how"), ("FAQ", "#faq"), ("Support", "{L}support.html"), ("Privacy", "{L}privacy.html"), ("Contact", "mailto:ryionconsulting@gmail.com")],
    footline="Whereabouts Compass, for iPhone and iPad",
    hero=[("{A}screens/now.jpg", "The Now screen: a map with a flag on South Korea, the city Seoul, and days there so far, above the three most recent trips"),
          ("{A}screens/trips.jpg", "The Trips screen: trips grouped by year, each with its flag, dates and number of days")],
    hero_dark=[("{A}screens/now-dark.jpg", "The Now screen in dark mode: a map with a flag on South Korea, the city Seoul, and days there so far, above the three most recent trips"),
               ("{A}screens/trips.jpg", "The Trips screen: trips grouped by year, each with its flag, dates and number of days")],
    facts=[("Useful on day one", "Rebuild years of past trips from the dates and places stored in your photos."),
           ("Silent after that", "No check-ins, no notifications, and no continuous GPS."),
           ("Ready to export", "A PDF to attach, a CSV for a spreadsheet, or one trip per line to paste into a web form.")],
    sections=[
        dict(kind="features", label="Why", title="Built for the five-year question",
             lead="Visa, green card, citizenship and tax forms ask where you were, and on which dates, for years back. Nobody can answer that from memory. Whereabouts Compass keeps the answer for you.",
             items=[
                ("Useful on day one", "Rebuild years of past trips from the dates and places stored in your photos, in minutes and with no network.", None),
                ("Silent after that", "It logs the country and city you are in. No check-ins, no notifications, and no continuous GPS.", None),
                ("Counts that match the form", "Arrival and departure days both count, so 3 to 10 May is 8 days, in the local time of the place you were.", None),
                ("Ready to export", "A PDF to attach, a CSV for a spreadsheet, or one trip per line to paste into a web form.", None),
             ]),
        dict(kind="steps", id="how", label="How to use it", title="How to use it", items=[
            "<b>Set it up once.</b> The first launch explains how it works, then asks for your location. Allow it while using the app. When the banner on <b>Now</b> asks, choose <b>Allow Always</b>. Without Always, days when the app is closed are not recorded.",
            "<b>Fill in the past from your photos.</b> Open <span class=\"path\">Settings → Import from Photos</span>. It reads only the date and place stored with each photo, never the picture. When it finishes, choose <b>Review Detected Trips</b> and <b>Confirm</b>, edit or delete each one.",
            "<b>Then let it run.</b> <b>Now</b> shows the country and city you are in and how many days you have been there. <b>Trips</b> lists every trip away from home, grouped by year.",
            "<b>Check and correct.</b> Open a trip to see its places and a map. An amber <b>?</b> marks an estimated date. Pick the real date and the trip stays exactly as you set it. Missed one? Use <b>Add a Trip</b> on the Trips screen.",
            "<b>Count the days.</b> <b>Countries</b> shows the total days, trips, first and last visit, and the last 12 months for each country. Set a date range at the top to match your form.",
            "<b>Export when a form asks.</b> Open <span class=\"path\">Settings → Export Travel History</span>, choose a range (Last 5 years, Last 10 years, Last 12 months, Since a date or Custom range), then <b>PDF</b>, <b>CSV</b> or <b>Copy as Text</b>.",
        ], figure=("{A}screens/photo-import.jpg", "The Import from Photos screen, explaining that only the date and place of each photo are read")),
        dict(kind="gallery", label="Screens", title=None, items=[
            ("{A}screens/trip-detail.jpg", "Trip detail: dates you can edit, the cities visited and a small map", "Trip detail: dates, places and a map"),
            ("{A}screens/countries.jpg", "The Countries screen: each country with its total days and trips", "Countries: totals for any date range"),
            ("{A}screens/export.jpg", "The Export screen: a date range, what is included, a preview, and PDF and CSV buttons", "Export: PDF, CSV or plain text"),
        ]),
        dict(kind="fields", label="Settings", title="Settings worth knowing", items=[
            ("Home country", "Trips at home are left out of the main list and the exports. It is set from your first location, and you can change it."),
            ("How days are counted", "<b>Count arrival and departure days</b> is on by default. You can also ignore trips shorter than a number of hours, if your form does. Every export states the rules it used."),
            ("Sync with iCloud", "On by default, so your iPhone and iPad agree. It syncs through your own private iCloud, and a change takes effect the next time the app opens."),
            ("Backup", "<span class=\"path\">Export Travel History → Full Backup and Restore</span> saves everything to one file and brings it back on another device. Restoring only adds what is missing, so it is safe to run twice."),
            ("Deleted Trips", "Brings back a trip you deleted."),
            ("How It Works", "The first-launch explanation, for when you skipped past it."),
        ]),
        dict(kind="list", id="limits", label="Good to know", title="Good to know", items=[
            "<b>It needs Always location.</b> Without it, days when the app is closed show up as gaps.",
            "<b>It notices stops, not every mile.</b> A country you only drive or fly through without stopping may not appear.",
            "<b>Crossing dates can be estimates.</b> When readings are sparse, the border date is marked with an amber <b>?</b>. Check those before you export.",
            "<b>Borders are accurate to about a kilometre.</b> Right at a border, a reading can land next door. Vatican City counts as Italy.",
            "<b>Open water is not a country.</b> A cruise shows as a gap between ports.",
            "<b>Layovers are not detected yet.</b> A stop at an airport can appear as a short trip. Delete it, or set a minimum trip length.",
            "<b>Photos fill in only what they saw.</b> Imported trips stay estimates until you confirm them.",
            "<b>It is a record, not advice.</b> It counts days from your own data. It does not decide tax residency or visa eligibility.",
        ]),
        dict(kind="pledge", label="Privacy", title=None, pledges=[
            ("Privacy", "No account, no ads, no analytics and no third-party code. On the App Store its privacy label reads <b>Data Not Collected</b>. The country is worked out on your phone from built-in maps. The only network requests go to Apple Maps, to name a city and to draw the map on a trip's page. <a href=\"{L}privacy.html\">Read the privacy policy</a>.", "green"),
        ]),
        dict(kind="faq", id="faq", label="Questions", title="Questions", items=[
            ("Does it drain the battery?", "No. It uses the same low-power visit and significant-location services iOS uses itself, based on cell and Wi-Fi. It never turns on continuous GPS."),
            ("Can I use it if I just installed it?", "Yes. That is what the photo import is for. Run it from <span class=\"path\">Settings → Import from Photos</span>, then confirm the trips it finds."),
            ("Can I give it access to only some photos?", "Yes. Limited Access works. Choose <b>Share More Photos</b> on the import screen to add more later."),
            ("A trip has the wrong dates", "Open it and pick the right dates. Any edit confirms the trip, so the app never changes it again."),
            ("How do I move to a new phone?", "With iCloud sync on, your history arrives by itself. Without it, make a backup from <span class=\"path\">Export Travel History → Full Backup and Restore</span> and restore it on the new phone."),
            ("How do I delete everything?", "<span class=\"path\">Settings → Privacy → Erase All Data</span>. With iCloud sync on, it is erased from your other devices too."),
        ]),
    ],
)

CINE = dict(
    slug="cinematic-teleprompter", dir="CinematicTeleprompter", name="Cinematic Teleprompter", short="Teleprompter", no="03", hue="gold",
    platforms=["iPhone", "iPad"], extra=None,
    blurb="Read your script beside the lens while you record in Normal or Cinematic mode.",
    title="Cinematic Teleprompter — read your script, record in Cinematic mode",
    desc="A teleprompter for iPhone and iPad. Your script scrolls beside the camera while you record in Normal or Cinematic mode, and it can follow your voice. Try it free for 7 days, then choose a plan or buy it once.",
    h1="Write it. Read it. Record it.",
    tagline="Your script scrolls right beside the lens while you film yourself, in Normal or Cinematic mode.",
    icon_alt="The Cinematic Teleprompter app icon: a golden clapperboard with lines of script on it",
    ctas=[("How to use it", "#how"), ("7 days free", "#pricing")],
    nav=[("How to Use", "#how"), ("Pricing", "#pricing"), ("FAQ", "#faq"), ("Support", "{L}support.html"), ("Privacy", "{L}privacy.html")],
    foot=[("How to Use", "#how"), ("Pricing", "#pricing"), ("FAQ", "#faq"), ("Support", "{L}support.html"), ("Privacy", "{L}privacy.html"), ("Contact", "mailto:ryionconsulting@gmail.com")],
    footline="Cinematic Teleprompter, for iPhone and iPad",
    hero=[("{A}screens/recorder.jpg", "The recorder mid-take: the script scrolls in a dark card at the top of the screen, near the camera, with a woman framed below it, the take's timer above and the stop button below"),
          ("{A}screens/cinematic.jpg", "The recorder in Cinematic mode: the background behind the woman is softly blurred, a yellow box marks her face, and the Cinematic button is lit")],
    facts=[("Eye contact, naturally", "The script sits in a band at the edge nearest the camera."),
           ("Cinematic mode", "Shallow depth of field with focus you can move, on iPhones that support it."),
           ("Follows your voice", "Voice-Follow scrolls as you speak, waits when you pause and catches up if you skip a line.")],
    sections=[
        dict(kind="features", label="Features", title="What it does", items=[
            ("Eye contact, naturally", "The script sits in a band at the edge nearest the camera, so you look almost straight into the lens while you read.", None),
            ("Cinematic mode", "Shallow depth of field with focus you can move, on iPhones that support it. The clips stay editable in Photos.", None),
            ("Follows your voice", "Voice-Follow scrolls as you speak, waits when you pause and catches up if you skip a line.", None),
            ("Real camera controls", "Front or rear camera, lens buttons, zoom, focus, exposure, resolution, frame rate, stabilization and a grid.", None),
            ("Takes are never lost", "Every recording stays in the app's Takes list until you delete it, even if you never saved it.", None),
            ("Scripts on every device", "Scripts sync between your iPhone and iPad through your own iCloud.", None),
            ("Built for iPhone Duo", "Filming someone with the rear camera? Unfold iPhone Duo and the script also shows on the outer display, facing them.", None),
            ("In five languages", "English, Korean, Japanese, Simplified Chinese and Canadian French, and each script can have its own speech language.", None),
        ]),
        dict(kind="spread", label="iPad", title=None, lead=None, after=None,
             figures=[("{A}screens/ipad-recorder.jpg", "The recorder on iPad: the script runs across the top of the screen above a man at his desk", "On iPad, the script runs across the top of the screen.", 1100, 1466)]),
        dict(kind="steps", id="how", label="How to use it", title="How to use it", items=[
            "<b>Start your free trial.</b> The first launch shows the plans. Tap <b>Start Free Trial</b> to try everything free for 7 days with the Yearly plan, or choose the Monthly plan or <b>Lifetime Unlock</b> instead.",
            "<b>Add a script.</b> Tap <b>New Script</b> and type or paste, or <b>Import</b> a .txt or .rtf file. The editor shows the word count and how long the script takes to read.",
            "<b>Open the recorder.</b> Tap <b>Record</b> on a script. Allow the camera and microphone the first time.",
            "<b>Set up the shot.</b> Flip between the front and rear camera, choose <b>Normal</b> or <b>Cinematic</b>, pick a lens, and pinch to zoom. Tap the picture to focus.",
            "<b>Rehearse if you like.</b> <b>Rehearse</b> runs the script without recording, so you can check the speed.",
            "<b>Record.</b> Tap the record button. After the countdown the script starts scrolling. While you record you can pause the scroll, go <b>Back a Few Lines</b> or change the speed.",
            "<b>Review and save.</b> When you stop, the take plays back. Choose <b>Photos</b> or <b>Files</b> to save it, <b>Share</b> to send it, or <b>Retake</b> to go again.",
        ], tip="<b>Tip:</b> takes you don't save stay under <b>Takes</b>, so you can come back to them later. Deleting a take there never deletes the copies you saved to Photos or Files.",
           figure=("{A}screens/script-overlay.jpg", "Script Overlay, open over the recorder: Speed, Voice and Timed scrolling, words per minute, countdown and font size")),
        dict(kind="prose", label="The script", title="Make the script work for you", blocks=[
            ("h3", "Three ways to scroll"),
            ("fields", [
                ("Constant Speed", "Scrolls at the words-per-minute you set. Use <b>Faster</b> and <b>Slower</b> to adjust it on the fly."),
                ("Voice-Follow", "Listens as you read and keeps your place. Each script can have its own language: tap the globe under the script. Speech is recognized on your device."),
                ("Timed", "Fits the whole script into a length you choose, with <b>Longer</b> and <b>Shorter</b>."),
            ]),
            ("h3", "Script Overlay"),
            ("p", "In the recorder, tap <b>AA</b> to open <b>Script Overlay</b>. There you can choose how the script scrolls, set the countdown, change the text size, colour and band position, show a <b>Reading Line</b> and <b>Fade Words Already Read</b>. For teleprompter glass, turn on <b>Mirror Horizontally</b> or <b>Flip Vertically</b>."),
            ("h3", "Cinematic controls"),
            ("p", "In Cinematic mode, a slider sets the simulated aperture. Tap a person or object to move the focus to it, and touch and hold to keep focus locked on them. Cinematic availability depends on the device and camera. If it isn't available, the switch says so. Most iPads don't offer it."),
            ("h3", "Prompt Only"),
            ("p", "Tap <b>Prompt Only</b> in the script editor to scroll the script full screen without the camera, for reading on a stage or a call."),
        ]),
        dict(kind="gallery", label="Screens", title=None, items=[
            ("{A}screens/library.jpg", "The Scripts list: five sample scripts, each with a short preview", "Your scripts"),
            ("{A}screens/editor.jpg", "The script editor: the script text, with the word count, language and reading time along the bottom", "Editor: words, language, reading time"),
            ("{A}screens/script-overlay.jpg", "Script Overlay, open over the recorder: Speed, Voice and Timed scrolling, words per minute, countdown and font size", "Script Overlay: scrolling and text"),
            ("{A}screens/prompt-only.jpg", "Prompt Only: the script in large white text on black, with playback controls at the bottom and no camera", "Prompt Only: no camera"),
        ]),
        dict(kind="pricing", id="pricing", label="Pricing", title="Pricing",
             stamp="7-day free trial, then a plan or a one-time unlock",
             text="Start the free trial with the <b>Yearly</b> plan and everything is unlocked for 7 days; the app can remind you 2 days before it ends. After that, keep the Yearly plan, switch to <b>Monthly</b>, or buy <b>Lifetime Unlock</b> once, with no subscription. Any of them unlocks the app on all your iPhones and iPads signed in with the same Apple Account. Prices are shown in the app.",
             cols=[("Always free", ["Writing, importing and editing scripts", "Prompt Only mode", "Watching, saving and sharing takes you already recorded", "iCloud sync of your scripts"]),
                   ("Needs a plan or Lifetime Unlock", ["Recording new takes, Normal and Cinematic", "Voice-Follow scrolling"])],
             after="You never lose access to your videos. On a new device, use <span class=\"path\">Settings → Restore Purchases</span>. To change or cancel a plan, use <span class=\"path\">Settings → Manage Subscription</span>."),
        dict(kind="faq", id="faq", label="Questions", title="Questions", items=[
            ("Why is Cinematic greyed out?", "The camera you are using doesn't support it. Cinematic is checked for each device and camera, and is not available on most iPads. If you switch to a camera without it, the app goes back to Normal by itself. <span class=\"path\">Settings → Device Capabilities</span> shows which cameras support it."),
            ("Do Cinematic videos stay editable?", "Yes. Saved to Photos, a Cinematic take can still be edited there, including moving the focus and changing the depth effect. Cinematic takes are always saved as HEVC so this keeps working."),
            ("My videos won't play on an older device", "Turn on <span class=\"path\">Settings → Use H.264</span>. The files are larger but play almost anywhere. Cinematic takes always use HEVC."),
            ("My front-camera video is mirrored, or isn't", "The preview is mirrored like a mirror, but saved videos are not, unless you turn on <span class=\"path\">Settings → Mirror Saved Video</span>."),
            ("Do my videos sync between devices?", "Scripts and shared preferences do. Videos are too large, so they stay on the device that recorded them. Save them to Photos or Files to move them."),
            ("Is my voice sent anywhere?", "No. Voice-Follow uses speech recognition on your device. See the <a href=\"{L}privacy.html\">privacy policy</a>."),
        ]),
    ],
)

APPS = [BILL, WHERE, CINE]
