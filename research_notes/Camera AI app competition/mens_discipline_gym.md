# Men's self-improvement apps: discipline + gym/fitness AI (research as of 2026-10-14)

Context: solo dev in Serbia, target ~$20k/month from an iOS subscription app, grown with faceless TikTok/Shorts.

**How to read the numbers:** Almost all revenue figures come from search snippets: founder self-reports, TrustMRR (Stripe/RevenueCat-verified but self-listed), Appfigures/ScreensDesign/AppGoblin modeled estimates, and press. Primary pages (TrustMRR, Starter Story, vc.ru, Substack) could not be fetched directly from this environment because of DNS blocks. Treat every number as an ESTIMATE unless it is marked otherwise. ScreensDesign's "$Xk revenue" label is ambiguous; it is probably a monthly Appfigures-style estimate.

---

## 1. Discipline / habit / quit apps

| App | What | Pricing | Rating | Revenue / scale (source, confidence) | Launch |
|---|---|---|---|---|---|
| **QUITTR** (Alex Slater UK + Connor McLaren US, both early 20s) | Quit-porn: streak, panic button, journal, community, lessons | Monthly $9.99, annual $19.99, lifetime $49.99 (Recurdash; other prices have been seen over time) | ~4.5-4.75 | Founder LinkedIn: "$500K MRR, $2M revenue in 8 months, bootstrapped". X, Jun 2025: "$500K in a month". X, Sep 2025: "first million dollar month" (unverified, may be gross). InfoMoney/The Sun: ~$500k/mo, 1M+ downloads in 120 countries, ~150k DAU. German press: 100k+ paying subs. Seraleev post (via vc.ru): ~$35k/day on peak days. Starter Story: ~$6M/yr. MEDIUM confidence on the ~$250-500k/mo order of magnitude | Built in ~10 days. App ID 6532588521 suggests mid-2024 launch. $140k in first 3 months (BoringCashCow) |
| **Brainbuddy** | Quit porn, older incumbent (app id 726780077, about 2013) | Paid premium after onboarding; regional tiers $12.99-$99.99 | n/a | ScreensDesign ~$50k/mo; AppGoblin <$10k/mo, 88k MAU. LOW confidence | 2013 |
| **Relay** (BYU founders, YC S22) | Group-based recovery from porn/lust: anonymous small groups, therapist lessons | Paid (moved off free when engagement dropped) | n/a | Funding ~$19M per aggregator, unreliable. Revenue unknown | ~2021 |
| **Rewire Companion** | Habit/quit companion | n/a | n/a | No data found | older |
| **I Am Sober** | Sobriety counter for any addiction | $4.99/mo, $49.99/yr | 4.9 | ScreensDesign "$200k" (likely monthly), AppGoblin $10k+/mo, 735k MAU. LOW confidence | 2013 |
| **75 Hard (official, 1st Phorm/Andy Frisella)** | Challenge tracker | Free/IAP | 4.5 | ScreensDesign $50-65k (likely monthly). Many clones (Forge 75, Transform 75) at $1.99/wk or $9.99 lifetime. LOW | ~2022 |
| **Opal** | Screen-time blocker (Screen Time API) | Pro subscription | 4.7 | Lazyweb: 2024 revenue $4.8M. Opal itself (late 2024): 100k+ Pro subscribers, DAU 100k->500k. MEDIUM | 2020 |
| **one sec** (Frederik Riedel) | Friction before opening apps | Subscription | high | No $ figure. Growth roughly doubled monthly once he ran Instagram ads (RevenueCat interview). Academic partnerships (Max Planck, Stanford) | 2021 |
| **Monk mode / dopamine detox apps** (Monk: Screen Time Control, Dopamine Detox, "Control Dopamine") | Blockers with a monk-mode pitch | various | n/a | TrustMRR shows tiny numbers ($50 total, $107 in 30d). Commodity: blockers alone don't win | 2024-26 |
| **quitcorn** (TrustMRR) | Quittr clone | n/a | n/a | ~$1.2k/mo. Shows that clones of the leader stall | 2025 |

### Quittr growth playbook (from snippets)
- Influencer integrations started at ~4 per month. They tested flat-fee deals and flat fee + per-view CPM deals (vc.ru).
- Organic TikTok/Instagram "day X of no fap" and transformation content. The founder built a personal brand on X ("future Prime Minister", build-in-public revenue posts), which brought press.
- Strong onboarding quiz followed by a hard paywall. Cheap annual plan ($19.99) to maximize conversion.
- Founder later handed over the CEO seat (Substack).
- **Cautionary:** In Jan 2026, 404 Media reported a misconfigured Firebase that exposed data on ~600k users (age, masturbation frequency, feelings), ~100k of them self-identified minors. The researcher had warned them since Sept 2025, and the founders were slow to fix and initially denied it. Big negative press across EU outlets. Lessons: secure Firebase rules, collect minimal sensitive data, and age-gate.

### Cal AI / Umax lineage (same founder cluster: Zach Yadegari, Blake Anderson, Henry Langmack)
- **Cal AI:** ~$8M ARR in Dec 2024, ~$30M in Dec 2025, ~$50M by Mar 2026 (ARR Club, unverified). Acquired by MyFitnessPal (reported Dec 2025 to Mar 2026; price rumored >$100M). Growth came from 250+ creators making native-looking content, then heavy paid Meta/TikTok ads after a plateau at ~$2M/mo.
- **Umax (looksmaxxing):** reported $100k in Dec, then ~$200k MRR by early January (Chinese secondary source, year unclear, likely 2024). RizzGPT ~$200k/mo (Whop blog).

---

## 2. Gym / fitness AI apps

| App | What | Revenue / scale (confidence) | Notes |
|---|---|---|---|
| **Cal AI** | Photo calorie tracker | ~$50M ARR (Mar 2026), acquired by MFP | Category leader; photo-calorie is **saturated** (hundreds of clones, 4.3(b) "saturated category" rejection risk) |
| **Gravl** (Bondi, Australia; bootstrapped) | AI gym workout planner | $150k-$440k/mo (ScreensDesign vs unkoa blog). MEDIUM-LOW | Affiliate program pays creators 40% commission. Launched ~Oct 2023 |
| **Fitbod** | AI workout planner, incumbent | $5-10M/yr (SimilarWeb), ~$750k-1M/mo (ScreensDesign/Adapty). LOW | Mature |
| **Ladder** | Coach-led strength "teams" | $12M Series A (Dec 2023, 50k+ paying members, 500% growth), $15M Series B + $90M General Catalyst customer-value capital (Nov 2024). Implies large paid-ad-driven revenue | Not solo-dev territory |
| **Future** | Human remote coach (~$150-200/mo) | VC-backed | Different model |
| **GainFrame** (iOS, 2026) | Progress photos plus AI physique score, BF%, FFMI, 12 muscle scores, "future physique" projection; uses Gemini API | TrustMRR snapshot (Jun 21 2026): **MRR ~$269k, 30d revenue $244k, total $9.4M** (verified-provider listing, but $9.4M total seems high for a 2026 app; the TrustMRR entry may cover a larger portfolio). MEDIUM-LOW | **Strongest evidence that AI physique/progress-photo apps are a 2025-26 indie hit** |
| **"Body fat estimator"** (TrustMRR) | Photo BF% tool, free to try | MRR ~$22k, total $95k (Mar 2026) | Shows a small single-feature tool can hit the $20k target |
| **BodyIQ** | Body fat scanner | 18 active subs (Jun 2026), for sale. Pricing $7.99/wk, $12.99, $59.99/yr | Shows most clones fail |
| ScanFit, bodyfatAI, Body Fat Scanner, Bodywhat (male-only beta, 15k users) | Same concept | n/a | **Physique-scan is getting crowded fast in 2026** |
| **Delts** (TrustMRR) | Gym logger; free local features, Gemini AI coach behind paywall | ~0 subs (May 2026) | Loggers are commodity (Hevy, Strong) |
| Acquire.com 3D body scan app | Body change tracking | $58.7k/yr revenue, asking $70k | |

**Saturated:** photo calorie tracking (Cal AI clones), generic AI workout planners (Fitbod, Gravl, dozens of others), set loggers (Hevy/Strong), 75 Hard clones, plain screen-time blockers, generic quit-porn clones.
**Still working but crowding:** AI physique scan / progress photos (GainFrame shows the ceiling; many 2026 entrants at ~0).

---

## 3. Gaps

1. **Christian / traditional men's discipline (faith + gym + quit porn + habits).**
   - Demand evidence: Hallow earned ~$40M net in 2025 (Appfigures), with Lent spikes. Bible Chat (Romanian team) had a $750k net month in Mar 2025, ~$15M annualized, and a $14M Series A. Exodus 90 (Catholic men's 90-day program) charges $90/yr and is rated 4.7. Quittr's audience overlaps heavily with Christian men.
   - Supply: small, mostly new 2025-26 apps with few ratings: Warriors of Christ (devotional + workouts), Sixty Strong (60-day team challenge, free), The Bible For Men, PROJECT 13:22 (Landen Conner, fitness + nutrition + Bible), Vessel (Jul 2026, no ratings), GUARDED: Quit Porn with Christ (90-day + AI companion), The Ordered Life (Catholic men). No clear category leader found, though it is quickly getting populated.
   - Per Appfigures, 46 of 9,000+ Bible apps make >$10k/mo. That makes $10-20k/mo a top-1% outcome, but those 46 are generic Bible apps, not men's discipline.
   - Advantage from Serbia: an Orthodox-friendly variant is possible, but the money is in the US (95%+ of Bible Chat revenue is US).
2. **"Become a man" accountability** (Relay-style small groups and partner check-ins). Network effects aid retention, but cold-start is hard for a solo dev. Better as a feature, such as a "brother" accountability partner.
3. **Money discipline for young men** (no-spend challenges, savings streaks). Existing players: NoBuy (iOS gamified no-spend, no bank link), Plum's no-spend challenge (UK/FR), Qapital/Long Game. No evidence of indie revenue at scale. Bank linking means trust and regulation burden, and the TikTok niche monetizes worse. **Weakest evidence; skip or use as a module.**

---

## 4. Risks

- **App Store:** 4.3(a)/(b) spam/saturated-category rejections hit AI-built clones (calorie, BF scanners, quit-porn clones), so you need clear differentiation in metadata and features. Health claims (BF% accuracy, "cures addiction") should be avoided (guideline 1.4.1). Sexual-wellness topics need a 17+/18+ rating. US state app-store age-verification laws: Texas SB2420 was enjoined Dec 23, 2025; Utah's compliance deadline is May 2026, with enforcement Dec 31, 2026. Developers must handle age-range signals.
- **Bad press:** Looksmaxxing coverage in 2026 (Bark rates the PSL app 1/5; 1News NZ; WJLA "boys as young as 10"; bone-smashing, steroids, eating disorders). Face-rating or "hotness" scores are a reputational trap. The Quittr breach shows how sensitive data around minors becomes a headline.
- **Retention:** RevenueCat 2025 found ~30% of annual subscribers cancel within the first month (cross-category). Health & fitness median trial-to-paid is 39.9% (top decile 68%). 3- and 7-day trials see the highest Day 0-1 cancellation. Streak apps churn when the streak breaks (a Sixty Strong review complaint). Mitigations: annual-first pricing, streak "repair", and a 90-day program with a natural renewal ("next 90").
- **Inference cost:** Low. Gemini 2.5 Flash costs ~$0.30/M input tokens and $2.50/M output (trackers, May 2026). A photo body-fat scan is ~$0.001-0.005, and a daily AI coach chat is cents per user per month. That is negligible against a $30-60/yr sub. The risk is paid-acquisition cost, not inference.
- **Platform/founder:** Faceless TikTok works (carousels/slideshows reach the FYP without followers), but it is a volume game. Most successful apps above (Cal AI, Quittr, Gravl) layered on paid creator deals. Plan for a ~$1-3k/mo creator budget once conversion is proven.

---

## 5. Unit math for $20k/month
- $20k/mo is ~$240k/yr in proceeds. After Apple's 15% (Small Business Program), ~$280k gross per year.
- At $39.99/yr (net ~$34): ~7,000 active annual subs. At 2-4% install-to-paid, that needs **~175k-350k installs/yr** (~15-30k/mo). That is achievable with 2-4 faceless accounts posting daily and a couple of viral hits per month, plus small creator deals.

---

## 6. Verdict: top 2 ideas

### #1: Christian men's 90-day discipline app ("faith + iron + purity")
- **Wedge:** One daily checklist for Gen Z/young Christian men: scripture + prayer (2 min), workout done (simple programs or Health import), purity streak with panic button and verse, a cold shower/no-phone-morning habit, and an AI "brother"/mentor check-in grounded in scripture. 90-day "Forge" cohorts with a renewal loop. Non-denominational first, US-focused. Optionally a later Orthodox/Catholic content pack.
- **Why:** It combines the two proven money pools: quit-porn (Quittr ~$500k/mo) and faith (Hallow ~$40M/yr, Bible Chat ~$750k/mo). Exodus 90 proves men pay $90/yr for a structured 90-day program. Competitors are tiny and new (Warriors of Christ, Sixty Strong, GUARDED, PROJECT 13:22, Vessel, Ordered Life). Text-only AI means near-zero inference cost. Less looksmaxxing and press risk.
- **Content:** "Day 14 of 90 as a Christian man trying to get disciplined" slideshows, verse-over-gym-footage, "things I quit for God" lists, and Lent/New Year/back-to-school spikes (Hallow's Lent pattern is very predictable).
- **Risks:** Authenticity (the audience sniffs out cash-grabs, so the founder's own faith matters), denominational disputes, and sensitive data (copy nothing from Quittr's Firebase mistakes; keep data local where possible, adults 17+).

### #2: AI physique progress tracker for natural lifters (no face rating)
- **Wedge:** Weekly standardized progress photo with guided poses and a ghost overlay. Gives an AI body-fat *range* (honest, not a precise number) and muscle-group feedback, then the AI adjusts calories/protein/program for a 12-week recomp. "Natty" positioning: anti-steroid, anti-looksmaxxing. Adults only.
- **Evidence:** GainFrame TrustMRR snapshot ~$269k MRR (Jun 2026). A simple "Body fat estimator" hit ~$22k MRR. Gravl $150-440k/mo shows lifters pay. Cal AI proves photo-AI + TikTok scales.
- **Competitors:** GainFrame (closest, strong), ScanFit, bodyfatAI, BodyIQ, Body Fat Scanner, Bodywhat, plus Cal AI/MFP. **Crowded in 2026.** Differentiate on the weekly ritual and the transformation timelapse video export, which also fuels TikTok content. Pure scanning is not a wedge.
- **Content:** Timelapse transformations, "AI guessed my body fat", "week 1 vs week 12" — content that partly generates itself from users' exports.
- **Risks:** 4.3(b) saturation rejections, accuracy complaints, body-image press, and Apple's photo/health data scrutiny.

**Pick:** #1 has the clearer gap and lower risk. #2 has stronger proof of revenue but more competition. A combined angle (#1 with a weekly progress-photo check-in) is reasonable, but ship the narrow version first.

**Skip:** generic quit-porn clone, photo calorie tracker, generic AI workout planner, standalone screen-time blocker, looksmaxxing/face rating, money no-spend (weak evidence).

---

## Sources (via search snippets)
- Quittr: linkedin.com/in/alexsllater; x.com/alexsllater; intro.co/AlexSlater; starterstory.com/quittr-breakdown; yumaueno.substack.com/p/the-20-year-old-who-took-an-app-to; vc.ru/growth/1762617; boringcashcow.com interview; infomoney.com.br; nssmag.com; recurdash.com/subscription-pricing/quittr; 404media.co (breach, Jan 2026); ladn.eu
- Cal AI: arr.club/cal-ai/cal-ai-hit-50m-arr; superframeworks.com/case-study/cal-ai; finder.techleap.nl
- Umax/Rizz: whop.com/blog/looksmaxxing-blake-anderson; hub.baai.ac.cn/view/43658
- Gravl: unkoa.com; screensdesign.com/apps/personal-trainer-gravl; dealroom
- Fitbod: similarweb; screensdesign; adapty paywall library
- Ladder: orrick.com (Nov 2024); businesswire (Dec 2023)
- GainFrame: trustmrr.com/startup/gainframe; gainframe.app blog; apps.apple.com/app/id6759252082
- Body fat estimator/BodyIQ/Delts/monk mode: trustmrr.com pages; acquire.com listing
- Opal: lazyweb; community.opal.so keynote; one sec: revenuecat.com blog
- Brainbuddy/I Am Sober/75 Hard: screensdesign, appgoblin, App Store
- Relay: ycombinator.com/companies/relay; utahbusiness.com
- Faith: appfigures.com Hallow Lent insight; appfigures.com/resources/insights/20250418 (Bible Chat); exodus90.com/pricing; App Store listings (Warriors of Christ, Sixty Strong, GUARDED, Bible For Men, Vessel); studio.com/landen; producthunt The Ordered Life
- Risks: bark.us PSL review; 1news.co.nz (Jun 2026); wjla.com; wileyconnect.com (Texas injunction); orrick.com (Utah/Texas); developer.apple.com forums (4.3); revenuecat State of Subscription Apps 2025; pricepertoken.com (Gemini pricing)
