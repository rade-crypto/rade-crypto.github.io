# Two niches for men: hair-loss tracker vs. trading-card scanner (as of 14 Oct 2026)

> **Method note:** WebFetch failed with DNS errors, so I couldn't open App Store pages, BetaKit, or the Collectr PDF directly. Everything below comes from search-result snippets: App Store listings, trackers (AppGoblin, screensdesign, App Pricing Lab, chrome-stats, TrustMRR), press and forums.
> - Ratings are tracker snapshots and may lag the live store.
> - **Every third-party revenue figure is a modeled estimate (E)** unless marked **(V)** for verified (e.g. RevenueCat/Stripe on TrustMRR) or **(C)** for company-claimed.
> - Estimators can be off by 2x or more in either direction. screensdesign in particular has disagreed with other trackers on the same app (see skin_scan.md).

Goal: a solo developer in Serbia, about $20k/month, with a camera → AI result → paywall subscription app, grown with faceless TikTok/Shorts.

---

## A) Men's hair-loss / hairline progress tracker

### Competitor table

| App | What it does | Rating (snapshot) | Pricing | Revenue / traction signal | Ownership / funding | Source |
|---|---|---|---|---|---|---|
| **MyHair AI** (id1505274518) | Scalp photos → density, "hair score" from 22 data points, routine, clinic finder | n/a | Subscription | **(C) >1,000 paying subs, 200k accounts, 300k+ photos analysed (Nov 2025).** Implied MRR is roughly $8–15k if subs are $8–15/mo (my inference) | Founders Cyriac Lefort (serial founder) and Tilen Babnik. Covered by TechCrunch. Funding size not found | [TechCrunch](https://techcrunch.com/2025/11/26/are-you-balding-theres-an-ai-for-that/), [eWeek](https://www.eweek.com/fr/news/news-ai-tools-spot-early-balding/), [App Store](https://apps.apple.com/app/id1505274518) |
| **Hairloss AI / Hair Loss AI therapy & scanner** (id6563141135) | Norwood scan + "therapy" plan | 4.4 ★, 236 ratings | Subscription | Claims "1M+ hairlines scanned" (marketing copy) | AMR Holding B.V. (NL) | [App Store](https://apps.apple.com/us/app/hair-loss-ai-therapy-scanner/id6563141135) |
| **Recede.io** (id6733220008) | AI Norwood rating, predicts hair loss | 4.0 ★, 89 ratings | Hard paywall before results | Complaints: results paywalled with no preview, long questionnaire before paying, subscription glitches | Recede LLC | [chrome-stats](https://chrome-stats.com/d/id6733220008) |
| **Norwood – Hair Tracker** (id6786227378, 2026) | 4-angle scan → Norwood stage | n/a | Weekly / monthly / annual | — | Indie, 2026 | [App Store](https://apps.apple.com/app/id6786227378) |
| **Follicle** (id6759066308, Mar 2026) | Tracker, claims to be "#1" | 0 ratings | Sub | — | Indie | [AppGoblin](https://appgoblin.info/apps/6759066308) |
| **Folicle** (Peerlist build log) | Tracker built on Expo, Supabase, RevenueCat and Gemini | — | Free tier with analysis quotas | Developer: per-photo AI calls added up fast | Solo developer, about 6 months to build | [Peerlist](https://peerlist.io/leothedev/project/folicle) |
| **Rooty – Save Your Hair** (id6761381733) | Tracker + plan | 3 ratings | $29.99/yr, 7-day trial | — | Indie, 2026 | [appshunter](https://appshunter.io/ios/rooty-save-your-hair/id6761381733) |
| **Repousse** (id6781779855), **DermaRoot** (id6759264189), **HairBuddy** (id6751080627), **Hairly** (id6754949306), **HairHero** (id6748265052), **Hair Snap**, **Hair Health: AI Scan**, **Track Hair** (id6740919537), **Peloz: Minoxidil Tracker** (id6768477868, Jun 2026), **HairCode** (KR) | Clone pattern: guided photos → density/Norwood score → plan, with product scanner or reminders | Mostly <50 ratings | Weekly/annual subs; HairHero paywalls results | None found | 2025–2026 indies | [DermaRoot](https://apps.apple.com/app/id6759264189), [HairBuddy](https://apps.apple.com/app/id6751080627), [Repousse](https://apps.apple.com/app/id6781779855), [Hairly](https://apps.apple.com/us/app/-/id6754949306), [HairHero](https://apps.apple.com/us/app/ai-hair-scanner-hairhero/id6748265052), [Peloz](https://mwm.ai/apps/peloz-minoxidil-e-cabelo/6768477868) |
| **HairMax** (TrustMRR) | iOS hair analysis + tracking | — | Sub | **(V) about $30 in its first 3 days, 3 active subs. Listed for sale at about $5k** | Indie, tracked since Mar 2026 | [TrustMRR](https://trustmrr.com/startup/hairmax) |
| **TrichoMetrics** | Web beta, density/Norwood from standard photos | — | — | Beta. Posted on the Tressless forum asking for feedback | Indie | [Tressless](https://community.tressless.com/t/i-built-an-ai-tool-to-track-hair-loss-with-metrics-beta-looking-for-critical-feedback/5560) |
| **MyHairCounts** | Density counting kit + app | — | — | — | Awareable Technologies (Houston) | [InnovationMap](https://houston.innovationmap.com/myhaircounts-gordon-little-kenny-robinson-2657316675.html) |
| **Traya** (India) | Hair-loss D2C brand app | 4.5 ★ (aggregator) | Free (sells product) | (E) <$10k/mo in-app, about 214k MAU (AppGoblin). The app is a funnel for the D2C business | Traya Health | [AppGoblin](https://appgoblin.info/apps/1662943113) |
| **Hims: Telehealth for Men** (id1455690574) | Telehealth. Hair-loss intake uses hairline photos | **4.8 ★, ~82.8k ratings (Mar 2026)** | Pay per Rx (finasteride/minoxidil) | Public company. Acquired ZAVA (2025), YourBio (Dec 2025) and Eucalyptus (closed Jun 2026) | NYSE: HIMS | [App Pricing Lab](https://apppricinglab.com/app/apple/1455690574), [Healthline](https://www.healthline.com/health/hims-hair-review), [Eucalyptus close](https://www.standard-journal.com/ap/business/hims-hers-completes-acquisition-of-eucalyptus-advancing-its-position-as-the-world-s-largest-consumer/article_94b6bef4-a447-51df-89af-19f562b78666.html) |
| **Ro, Keeps** | Telehealth Rx | Not found | Rx subs | Neither has a dedicated tracking app with an AI score (not found in search) | Private | [BlackHealth Ro review](https://www.blackhealth.org/reviews/roman-review/) |
| Adjacent: **Hair AI: Hairstyle Filter** | Hairstyle try-on (image generation) | — | Sub | (E) about $200k/mo on 60k downloads (AppRank, Aug 2026) | — | see alternative_niches.md |

### Evidence of 2025–2026 entrants making money
- **Weak.** At least 10 new hair trackers launched in 2025–26, most with 0–50 ratings. The only verified revenue is HairMax (tiny).
- The best signal is MyHair AI at about 1,000 paying subscribers (company claim), likely low five figures in MRR at most.
- I found **no indie hair-loss tracker at or above $20k/mo**.
- The money in "men + hair" sits in **Rx telehealth** (Hims) and **hairstyle try-on** (Hair AI, about $200k/mo estimated), not in tracking.
- Demand driver is real: US finasteride prescriptions for men over 25 rose about 200% in 7 years, driven by young men (Epic Research via [AHLA](https://www.americanhairloss.org/booming-demand-us-sees-200-surge-in-finasteride-prescriptions-over-7-years/)).

### Common complaints a better AI could fix
- **Results paywalled with no preview**, plus long questionnaires before the paywall (Recede).
- **Unreliable comparison between months.** Lighting, wet vs. dry hair, hair length and camera angle change the score more than real change does. This is my inference from how these apps capture photos and from community discussion; I couldn't pull Reddit directly. The fix:
  - A ghost overlay that aligns each photo to the previous one.
  - Fixed distance, using the front camera's depth or face landmarks.
  - Lighting normalization.
  - Same-pose crown and temple shots.
  - Deltas shown with confidence bands.
- **Generic "plans" with no tie to a real treatment protocol.** Users want minoxidil/finasteride/dutasteride/microneedling logging, side-effect logs and "dread shed" expectation timelines (the shed is well documented in [Grazia](https://graziadaily.co.uk/beauty-hair/hair/what-is-minoxidil) and [Daily Beast](https://thelooker.thedailybeast.com/18-million-people-watched-my-hair-grow-back/)).
- **Missing shareable output.** A month-by-month time-lapse video export would let the product itself produce TikTok content.

### TikTok / short-video fit
- **Audience is large.** #HairGrowth had about 14B views back in 2023 ([ABC7](https://abc7.com/hair-grow-loss-remedies-treatment/14017740/)). Single minoxidil before/after clips reach 1.8M+ views in 2 days, and one creator reports 18M viewers of a regrowth journey.
- I couldn't retrieve exact current counts for #hairloss or #minoxidil (that needs TikTok Creative Center).
- **Faceless is harder.** The best content is a real person's crown or hairline over time, which shows identity. Workable faceless formats:
  - top-of-head crown shots, which don't show the face
  - animated Norwood charts
  - "What month 1 / 3 / 6 of minoxidil looks like" with UGC from consenting users
  - AI-rendered "your hairline in 5 years" (image generation adds cost and Guideline 1.4.1 claim risk)
- **The tone carries risk.** Fear-based "you're balding" hooks can draw TikTok health-misinformation enforcement.

### Risks
- **Apple 1.4.1 (Safety – Physical Harm).** Health and medical apps get extra scrutiny.
  - Developers report rejections for health recommendations without sources, and requests for regulatory clearance even for apps that call themselves "wellness-only" ([forum 807508](https://developer.apple.com/forums/thread/807508), [678447](https://developer.apple.com/forums/thread/678447), [703502](https://developer.apple.com/forums/thread/703502)).
  - Mitigation:
    - Frame it as a "cosmetic progress journal".
    - Never say "diagnose", "detect alopecia" or "treat".
    - Cite AAD/NIH sources in-app.
    - Show a Norwood "visual similarity" rather than a stage diagnosis.
    - Don't recommend Rx dosages.
    - Point medication logging at "as prescribed by your doctor".
  - Expect at least one rejection cycle.
- **BIPA (Illinois).** It covers face geometry. If the app runs face landmarks or embeddings to align hairline photos, that is arguably a biometric identifier.
  - The 2024 amendment (SB 2979) caps recovery at one per person per collection method. The Seventh Circuit held it retroactive on **1 Apr 2026** (*Clay v. Union Pacific*) ([Covington](https://www.insideprivacy.com/data-privacy/seventh-circuit-holds-that-bipa-amendment-applies-retroactively/)).
  - Exposure is still $1k–$5k **per Illinois user**. The Apple Photos BIPA class (about 6.5M people) shows the plaintiff bar is active ([TechRepublic](https://www.techrepublic.com/article/news-apple-photos-bipa-class-action-appeal/)).
  - Mitigation:
    - Do landmarking on-device with Apple Vision and keep it ephemeral.
    - Never store face templates.
    - Get explicit written consent, publish a retention policy, and allow deletion.
    - Prefer crown/scalp crops.
  - Also relevant: **Washington's My Health My Data Act** (private right of action for consumer health data) and Texas CUBI. These are from my own knowledge and not re-verified in this session.
- **Telehealth incumbents.** Hims has hairline photos from its Rx intake and 82.8k ratings. If it ships an AI tracker it becomes a free, bundled competitor. There is no sign of one yet.
- **Inference cost: low.** One to four photos a month per user. A vision-LLM call at about $0.002–0.01 per analysis, or on-device CoreML segmentation, comes to under $0.05 per user per month. The cost trap is a free tier with unlimited scans (Folicle's lesson).
- **Retention.** Monthly photos keep users coming back, but a hairline changes over months while the payoff moment (the first score) happens on day 1. Annual plans fit this better than weekly.

### Verdict A
**Viable but unproven. No one visibly makes $20k/mo.**
- Competition is a swarm of weak 2025–26 clones plus one funded startup (MyHair AI).
- The ceiling is limited by:
  - a small paying audience (men in their 20s–30s already on minoxidil or finasteride)
  - harder faceless content
  - medical-claim and biometric risk
- Wedge if chosen: a **"Minoxidil / Finasteride 12-Month Journey Cam"** with:
  - ghost-overlay capture for standardized photos
  - crown and temple density deltas with confidence ranges
  - a treatment and side-effect log with shed-phase timeline reassurance
  - an **auto-generated time-lapse video** built to be shared, which feeds TikTok organically
- Charge annual-first (about $39–59/yr). Optional later: affiliate links to telehealth, which require care with Apple and FTC rules.

---

## B) Trading card scanner / valuer (sports, Pokémon, Magic)

### Competitor table

| App | Rating (snapshot) | Pricing | Revenue / traction | Ownership / funding | Source |
|---|---|---|---|---|---|
| **Collectr** (Pokémon/TCG-led, multi-category) | 4.8 ★. Trackers report about 76.6k reviews (one tracker; counts vary by region) | Freemium + Pro (price not found). Bulk scanning gated | **(C) ~10M collectors, 1.1M daily users, 9M+ scans/day, 900M+ items tracked (mid-2026 report).** **(C) "5-figure ARR to 8 figures in six months" (May 2025).** Bootstrapped | Founders previously sold Doorr to Finastra (2020). No VC found. Pokémon is 65% of tracked activity | [Collectr mid-2026 report](https://public.getcollectr.com/public-assets/reports/state-of-the-hobby-2026-mid-year-report.pdf), [BetaKit](https://betakit.com/how-collectr-bootstrapped-a-trading-card-hobby-into-an-eight-figure-business/), [Fintech.ca](https://www.fintech.ca/2025/05/22/collectr-worlds-fastest-growing-collectibles-app/) |
| **Ludex** (sports-first + TCG) | **4.7 ★, ~26.7k ratings iOS (Jul 2026)**; 4.5 ★, ~15.6k on Android | Lite $4.99/mo or $44.99/yr; Ludex $9.99/mo or $89.99/yr; Pro $24.99/mo or $239.99/yr | (E) about $6M/yr (Prospeo, low quality) | Chicago, founded 2021. Raised >$8M from friends and family and convertible debt (not VC). Investors include Brian Urlacher | [App Pricing Lab](https://apppricinglab.com/iap/apple/1616691213), [chrome-stats](https://chrome-stats.com/d/id1616691213), [Built In Chicago](https://www.builtinchicago.org/articles/ludex-raises-8m-ai-trading-cards), [Prospeo](https://prospeo.io/c/ludex-revenue) |
| **CollX** (sports-first + TCG; marketplace) | **4.5 ★, ~37.9k ratings (Mar 2026)** | Pro about $9.99/mo or $99.99/yr (older $49.99/yr SKU); Gold $24.99/mo or $249/yr; free tier capped at 500 scans (2024) | (C) 3M+ users (2025). Revenue estimates conflict (<$1M Dealroom; $438k Bitscale), probably too low. 10% marketplace commission, plus referral revenue from PSA, Whatnot and Fanatics | $5.5M seed (2023) + $10M Series A (Mar 2025, Brand Foundry, 114 Ventures). Owns **Card Dealer Pro** (dealer bulk-scanning tool) | [TechCrunch](https://techcrunch.com/2025/03/07/collx-raises-10m-to-grow-its-card-collection-marketplace), [App Pricing Lab](https://www.apppricinglab.com/app/apple/1581164444), [Dealroom](https://dealroom.co/companies/collx/) |
| **TCGplayer app** | Small regional samples (2.7 ★ DE, 32 reviews) | **Free, no paid tier.** Scanner covers every TCG on the marketplace | Marketplace funnel | TCGplayer Inc. (acquired by eBay in 2022 — my knowledge, not confirmed in snippets). **Closed to new API developers** | [App Store](https://apps.apple.com/us/app/tcgplayer/id1247645833), [docs](https://docs.tcgplayer.com/docs/getting-started) |
| **PSA: Card Scanner & Grading** | — | **Free** | Scanner added Feb 2025, using PSA population data, graded value estimates and eBay sales history. Scan → submit to grading → list on eBay | Collectors (PSA parent) raised $100M at a $4.3B valuation (Sep 2026) | [CLLCT](https://www.cllct.com/sports-collectibles/sports-cards/psa-adds-card-scanner-to-its-app-for-mobile-submissions), [FOS](https://frontofficesports.com/article/collectors-raises-100m-valued-at-4-3b/) |
| **Dex – for TCG Collectors** (id1555489854) | Not found | Free + Dex+ (monthly/yearly) | — | Indie, "unofficial" Pokémon app since 2021 | [App Store](https://apps.apple.com/app/id1555489854) |
| **MTG:** ManaBox (free + premium), Delver Lens (Android, paid price lookups), Dragon Shield MTG Scanner (free) | — | Mostly free | Free scanners dominate MTG | Indie / brand | [Scrytics](https://scrytics.com/blog/best-mtg-card-scanner-app-2026), [MagicUntapped](https://magicuntapped.com/index.php/features/mtg-scanner-dragon-shields-free-to-use-smartphone-app-for-magic-the-gathering-players) |
| **2025–26 clone scanners** (paywall-first) | | | | | |
| — Sports Card Scanner: **SPcard** | — | Sub | **(E) about $100k/mo, 40k installs/mo** (screensdesign, undated) | Studio or indie | [screensdesign](https://screensdesign.com/showcase/sports-card-scanner-spcard) |
| — **StarSnap** Sports Card Scanner | 4.7 ★ | Sub | **(E) about $250k "revenue"** (screensdesign; period unclear) | Next Vision Ltd | [screensdesign](https://screensdesign.com/apps/starsnap-sports-card-scanner/) |
| — **FoilSnap** TCG scanner | Reviews include "0/11 Pokémon correct" | Sub | **(E) about $100k, 85k installs** | — | [screensdesign via search](https://screensdesign.com/apps/acorn-tcg-card-scanner-app/) |
| — **Acorn TCG**; **TCG Card Identifier Value** | 4.8 ★ (Acorn) | Sub | (E) about $45k each (Acorn: 20k installs) | — | same |
| — **Dexi** (PRODIGYAI) | 4.7 ★, ~1k ratings | $5.99–7.99/wk, $8.99/mo, $19.99–29.99/yr | — | Studio (2025 id) | [App Store](https://apps.apple.com/app/id6749697621) |
| — Scout, CardVault, PokeScope (4.3 ★, 36 ratings), Pokex, Scanner TCG AI (Mar 2026), DexScan, Kardexy, PokeHolo, CardVal (solo, on-device) | Small | Weekly/annual; one charges $39.99/yr or $99.99 lifetime | (E) <$10k/mo each (AppGoblin, Scout and CardVault) | Indies | [AppGoblin Scout](https://appgoblin.info/apps/6759388277), [PokeScope](https://apps.apple.com/app/id6739146586) |
| — **RookieDex** | — | — | **(V) $1.4k in 30 days** | Indie | [TrustMRR](https://trustmrr.com/startup/rookiedex-sports-card-scanner) |
| — **PokeScreener** (web price checker) | — | Freemium | (V?) **$130k in 30 days, 115 subs.** The page mixed in other startups' data, so this is unconfirmed | Indie | [TrustMRR](https://trustmrr.com/startup/pokescreener) |
| **AI pre-graders:** CardGrade, PreGradeCards, Card Grader AI, ZeroPop (id6760512726), Gemix, Centering50 (free), GradeMyCard | — | CardGrade $4.99–74.99/mo (credits); PreGradeCards from $0.19/card; Card Grader AI $5.99/mo | (C) CardGrade: 10k+ members (Aug 2026). One micro-app listed with **$1,012 ARR** for sale | Indies | [Daily Tribune PR](https://www.daily-tribune.com/online_features/press_releases/cardgrade-expands-ai-card-pre-screening-with-forensic-capture-collection-tools-and-free-centering-calculator/article_977baa52-15ac-5d23-953b-07f81284391c.html), [PreGradeCards](https://pregradecards.com/for-ai), [Microns](https://www.microns.io/startup-listings/ai-powered-card-grade-prediction-tool) |
| Adjacent 2026 funding | | | | CatchBack Cards (YC W26, $500k; about $13k MRR soon after its Jan 2026 launch), Chance Studios ($3.2M seed, Apr 2026), Packz ($10.7M, Apr 2026). All are digital or physical pack-rip platforms, not scanners | | [Seedtable](https://seedtable.com/companies/catchback-cards/funding-rounds/seed-2026-01), [Caplight](https://www.caplight.com/company/chance), [Preqin](https://www.preqin.com/data/profile/asset/packz--inc-/796315) |

### Market tailwinds
- Collectr reports tracked sales volume up **107% year over year in 2025**, with the first half of 2026 already at about 75% of the 2025 total. Pokémon accounts for 65% of activity.
- First-half 2025 grading: TCG and non-sports cards were 7.2M submissions, 59% of all volume, up 70% year over year (GemRate, via [pregradecards](https://pregradecards.com/blog/pokemon-tcg-pocket-everyday-wonders-record-sales-pre-grade-2026)).
- r/PokemonTCG has about 1.2–1.4M members ([Hive Index](https://thehiveindex.com/communities/r-pokemontcg/)).

### Evidence of 2025–2026 entrants making money
- **Stronger than A.** Several paywall-first clone scanners from 2025–26 show estimated revenue of $45k–$250k, though these come from screensdesign, which has been unreliable before.
- Dexi reached about 1k ratings at $5.99–7.99/week pricing.
- Verified indie numbers are scarce (RookieDex $1.4k in 30 days).
- Collectr's bootstrapped jump to 8-figure ARR proves willingness to pay in Pokémon specifically.

### Common complaints a better AI could fix
- **Wrong variant or parallel.** This is the number one complaint across Ludex, CollX and the clones: "fast at finding the card, terrible at the correct version". Examples: reverse holo vs. holo, 1st edition vs. unlimited, refractor parallels, Japanese vs. English.
  - Mislabelled parallels inflate valuations.
  - One clone got 0 of 11 Pokémon cards right ([onclarity Ludex](https://www.onclarity.com/leaderboard/insight/ludex), [FoilSnap](https://justuseapp.com/en/app/6752642525/foilsnap-tcg-card-scanner/contact)).
- **Prices don't match eBay sold prices.** Apps mix asking prices with sold prices and show one overconfident number. Estimates are both too high and too low.
- Free tiers that are too restrictive, aggressive paywalls, no export, lost accounts or collections (Ludex), missing new sets.
- No **condition-aware** value. Raw near-mint vs. lightly played, and "what would this get as a PSA 9 vs. 10", are rarely shown together.

### TikTok / short-video fit
**Excellent and natively faceless.**
- Formats that work with only hands on screen:
  - hands opening packs, then a scan overlay with a price reveal ("$0.10 → $480")
  - "I scanned my childhood binder"
  - "Would this get a PSA 10?" with a centering grid overlay
- #pokemoncards had about 1.6B views and #pokemon about 10.8B in an older YPulse snapshot ([YPulse](https://www.ypulse.com/?p=63085)). I didn't retrieve current 2026 counts.
- The pack-rip economy (Whatnot, CatchBack, Packz) shows the content loop is still hot in 2026.
- The downside: every competitor uses the same formats, so creative fatigue and copycat ads are high.

### Risks
- **Pricing-data access is the real moat. A solo developer can't easily get it.**
  - TCGplayer API: "no longer granting new API access" ([docs](https://docs.tcgplayer.com/docs/getting-started)).
  - eBay Marketplace Insights (sold prices): limited release, only for developers approved by eBay business units. Valuation and market-research use may conflict with its terms. The old findCompletedItems call is deprecated ([eBay docs](https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html)).
  - PriceCharting API: paid subscription, current prices only, and all data must be purged when you cancel ([PriceCharting](https://www.pricecharting.com/price-guide?f=home)).
  - Pokémon: pokemontcg.io is free (TCGplayer and Cardmarket prices, 20k requests/day with a key), but the team is shifting to Scrydex (paid). PokemonPriceTracker offers a commercial free tier ([cardgrader.ai](https://cardgrader.ai/blog/pokemon-card-api), [PPT](https://www.pokemonpricetracker.com/free-pokemon-card-price-api)).
  - MTG: Scryfall data is free, but I didn't verify its commercial terms here.
  - Scraping eBay or TCGplayer is a terms-of-service risk that could kill the app.
  - **Implication: Pokémon raw prices are cheaply accessible. Sports-card sold comps (the hard part) are not.**
- **Identification accuracy.**
  - Pokémon and MTG have finite, well-catalogued sets with reference images (about 20k+ Pokémon English cards plus Japanese), so embedding search with OCR on set number and collector number gets very high accuracy.
  - Sports cards have tens of thousands of parallels per year, and color and refractor differences are hard to see. That's why Ludex and CollX invest heavily there.
- **Big incumbents.** Collectr has 10M users and an 8-figure ARR. Free scanners exist from TCGplayer, PSA, ManaBox and CollX's free tier.
  - A clone with a paywall up front competes on ASO and ads, not on product. That works (the SPcard/StarSnap estimates) but lives on paid UA or viral luck.
  - Guideline 4.3(a) spam rejections are a risk for yet another "Card Scanner AI".
- **Inference cost: very low** if built properly.
  - On-device CoreML embedding + vector index + OCR costs close to $0 per scan.
  - An LLM-vision fallback or pre-grade costs about $0.002–0.01 per scan.
  - Collectr-like users scan a lot (9M scans/day), so avoid per-scan cloud LLM calls in the main loop.
- **Grading-estimate claims.** Pre-grade results must be framed as estimates. Users will be angry if a predicted 10 comes back as an 8. PreGradeCards claims 89% accuracy within ±1 grade (company claim).

### Verdict B
**Better market, harder moat.**
- Demand, willingness to pay and faceless content fit are all clearly stronger than in A.
- Several 2025–26 paywall clones plausibly clear $20k/mo (estimates).
- But a generic "scan → price" clone sits next to a free Collectr, TCGplayer and PSA, and sports-card pricing data is effectively gated.

---

## Head-to-head

| Factor | A: Hair tracker | B: Card scanner |
|---|---|---|
| Proven demand / willingness to pay in-app | Low (MyHair about 1k subs; no indie at $20k) | High (Collectr 8-figure ARR; Ludex est. $6M/yr; clones est. $45–250k/mo) |
| Competition | Fragmented, weak clones; Hims as a latent threat | Strong incumbents plus many clones |
| Faceless TikTok fit | Medium-low (identity, health-misinformation tone) | Excellent (hands, packs, price reveals) |
| Data / licensing | None needed | Pricing data gated (TCGplayer closed, eBay restricted); Pokémon is fine |
| Regulatory | Apple 1.4.1, BIPA, WA MHMDA | Low (accuracy and claims only) |
| Inference cost | Very low | Very low with on-device ID |
| Retention | Monthly ritual; annual plans | High (collection tracking, new sets, prices) |
| Solo feasibility from Serbia | High | High for Pokémon/MTG; low for sports comps |

## Final verdict: **B (cards) is better, but only as a narrow Pokémon-first wedge, not a generic scanner.**

**Wedge: "Should I grade it?". A Pokémon (later One Piece / Lorcana) raw-card condition and grading-ROI scanner.**
1. Camera scan → identification with on-device embedding search plus OCR of the set number, using **variant-aware** detection (holo / reverse holo / 1st edition / Japanese). This targets the top complaint.
2. AI condition read:
   - centering measured from the borders
   - corner, edge and surface flags from 2–4 guided photos, including a tilted-light photo for scratches
3. Output: "Raw NM ≈ $X · est. PSA 9 ≈ $Y · PSA 10 ≈ $Z → grading fee $N → **expected profit**".
   - Raw prices come from pokemontcg.io / Scrydex / PokemonPriceTracker (licensed).
   - Graded comps come from the PriceCharting API (paid; budget for it).
4. Paywall after the first free result. Annual plan about $39.99, plus a weekly option for impulse buyers. A collection value tracker and new-set alerts drive retention.

**Why this wedge:**
- **Free scanners give raw price only.** PSA's own app had no estimates for ungraded cards at launch.
- **Grading volume is surging** (+70% year over year).
- **"Would this PSA 10?" is a native faceless TikTok format.**
- Pokémon data is legally accessible.
- It avoids the sports-parallel accuracy trap and the BIPA and 1.4.1 issues of hair-loss apps.

**Watch-outs:**
- Existing pre-graders (CardGrade, PreGradeCards, ZeroPop, Gemix) mean the differentiation must be **ID + ROI + collection in one flow**, with good capture UX.
- Validate PriceCharting licensing costs and commercial terms before building.
- Avoid the "AI Card Scanner" naming swarm (Guideline 4.3).

**Runner-up (A):** build it only with a content-led strategy. The wedge is the **12-month minoxidil journey cam with an auto time-lapse export**, framed as strictly cosmetic, with on-device face processing and BIPA-grade consent. The realistic ceiling looks lower ($5–15k/mo is my inference) because there is no evidence any tracker has passed about $15k MRR.

## Gaps
- No live App Store, Sensor Tower or Appfigures access. Collectr's rating count and Pro price, Dex's rating, and Ro/Keeps app data were not found.
- Current TikTok hashtag counts (#hairloss, #minoxidil, #pokemonpulls) were not retrieved. They need TikTok Creative Center.
- The screensdesign revenue figures for the card clones are undated and unverified.
- Reddit/Tressless complaint mining was not possible directly. The hair complaints are partly inferred.
- PriceCharting, Scrydex and Scryfall commercial pricing and terms were not verified.
