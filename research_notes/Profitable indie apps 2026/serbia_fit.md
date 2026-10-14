# Serbia Fit: Constraints and Precedents for a Solo Serbian App/Software Seller (2026)

Research note (2026-10-14): direct page fetches (WebFetch/curl) to polar.sh, docs.lemonsqueezy.com, docs.creem.io, developer.paddle.com, startit.rs, pausalko.rs, indiehackers.com and beancount.io all failed in this environment (DNS/proxy 403). Findings below come from search-result snippets, and several provider country lists were truncated before the "S" entries. Anything marked "background knowledge" is unsourced and has to be verified before it goes into the final report.

## Payment rails from Serbia in 2026 (App Store, Google Play, MoR providers, Stripe/US LLC)

### Takeaway
App store income is the easiest rail. Serbia is a supported territory for both Apple and Google Play merchant accounts, and payouts land in a Serbian business FX account. For web SaaS, Stripe is still not directly available in Serbia. Of the merchant-of-record providers, only Polar is clearly confirmed for Serbian payouts (via Stripe Connect Express). Paddle very likely works (Serbia is not on its sanctions list), while Lemon Squeezy, Creem and Dodo are unconfirmed. Many founders fall back on a US/UK company, which adds tax complexity.

### Cited Findings
- **Apple:** Apple's developer agreement exhibits list Serbia as a territory. For local developers, "Apple does not collect or remit taxes for local developers" (developers are responsible for their own local taxes) — [Apple Exhibits to Schedule 2 and 3](https://developer.apple.com/support/downloads/terms/exhibits/Exhibits-to-Schedule-2-and-3-20250821-Croatian.pdf) (via search snippet)
- Serbia got a localized App Store in 2020. Netokracija covered what that meant for local developers — [Netokracija](https://www.netokracija.rs/app-store-srbija-167732); [Telegraf](https://www.telegraf.rs/hi-tech/mobilni/3182094-dobra-vest-za-mts-korisnike-koji-imaju-apple-uredjaje)
- History: Serbian developers once had trouble registering for the Apple Developer Program because Serbia wasn't in the country list (some reportedly had to pick "international waters"). This is resolved now — [Startit](https://startit.rs/da-bi-razvijali-ios-aplikacije-developeri-iz-srbije-moraju-da-stave-da-su-iz-medunarodnih-voda/)
- **Google Play:** Google added Serbia to the countries whose residents can register merchant accounts (SeeNews report, likely 2019) — [SeeNews](https://seenews.com/news/google-adds-serbia-to-merchant-account-platform-671392). Play Console added RSD local pricing in 2018 — [Android Police](https://www.androidpolice.com/2018/11/30/paid-apps-on-the-play-store-are-available-in-georgia-and-myanmar-local-currency-supported-in-paraguay-and-serbia/). The official table is at [Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/9306917).
- A RevenueCat staff reply (Jan 2024) confirmed that both the Apple App Store and Google Play support Serbian developers — [RevenueCat Community](https://community.revenuecat.com/general-questions-7/rn-payment-3978)
- **Receiving the money:** A paušalac must receive foreign payments into a foreign-currency (devizni) account opened in the business's name at a Serbian bank. The same applies to PayPal-type platforms (business name, not personal). FX can't be withdrawn directly: it has to be converted to RSD and moved to the dinar business account first — [Pausalko](https://pausalko.rs/blog/pausalac-i-devizni-racun-firme-sta-sve-treba-da-znate/); [Pausalko 2026](https://pausalko.rs/blog/kako-pausalac-da-naplati-od-stranih-klijenata-2026/)
- **Stripe:** Serbia is still not on Stripe's supported-countries list (Zenind guide, Sept 2025). The common workaround is a US LLC, or a UK Ltd per Osome and Incorpuk (these are vendor marketing pages) — [Zenind](https://www.zenind.com/help/post/how-to-open-a-stripe-account-in-serbia-with-a-us-llc); [Osome](https://osome.com/uk/blog/open-stripe-business-account-serbia); [Incorpuk](https://incorpuk.com/blog/how-to-open-stripe-account-in-serbia/); [Stripe availability](https://support.stripe.com/questions/stripe-feature-availability-by-country)
- **Polar (MoR):** Serbia is listed among Polar's payout countries via Stripe Connect Express. Polar says sellers in listed countries can get payouts even where standalone Stripe isn't available. Customers can pay from anywhere except US-sanctioned countries — [Polar docs](https://polar.sh/docs/merchant-of-record/supported-countries) (via search snippet)
- **Paddle (MoR):** Paddle says it supports sellers in 200+ countries and territories. Its sanctions-based unsupported list (Belarus, Cuba, Iran, Russia, Syria, etc.) doesn't include Serbia. I couldn't read Serbia's row directly — [Paddle supported countries](https://developer.paddle.com/concepts/sell/supported-countries-locales); [Paddle help](https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle)
- **Lemon Squeezy:** Payouts go to a bank account in a supported country (in USD) or to PayPal, which covers 200+ countries. The bank list was truncated before "S" — [Lemon Squeezy supported countries](https://docs.lemonsqueezy.com/help/getting-started/supported-countries); [Getting paid](https://docs.lemonsqueezy.com/help/getting-started/getting-paid)
- **Creem:** Lists 86 local-bank payout countries (snippet truncated; an older FAQ list doesn't include Serbia). If your country isn't listed, you can't use Creem. Non-SEPA/non-EU payouts cost the greater of USD/EUR 7 or 1%. USDC payouts on Polygon are an alternative, with a 2% fee — [Creem supported countries](https://docs.creem.io/merchant-of-record/supported-countries); [Creem FAQ](https://docs.creem.io/faq/supported-countries); [Creem payouts](https://docs.creem.io/finance/payouts)
- **Dodo Payments:** Has a Serbia page about accepting payments from 220+ countries, but it doesn't confirm Serbian-resident merchant payouts — [Dodo Payments](https://dodopayments.com/payments-in/serbia)
- Balkan payment friction is a known pain point: the AgentOS founder (Panche Isajeski, likely North Macedonian) started by building a fix for payment processing in the Balkans, then pivoted. AgentOS reportedly reached $9.5k MRR two months after relaunch — [Indie Hackers](https://www.indiehackers.com/post/tech/starting-from-scratch-and-hitting-9-5k-mrr-in-two-months-j5pMaED5FEbKw8qmeyj9)

### Inferences
- Easiest models to run from Serbia, in order:
  1. **Mobile apps with in-app purchases/subscriptions** (Apple/Google handle global VAT/sales tax and pay into a Serbian FX account).
  2. **Web SaaS through Polar** (confirmed) or **Paddle** (likely), both acting as merchant of record.
  3. **Stripe via a foreign entity** (most flexible, but most complex).
- A merchant of record means one foreign payer: no need to register for VAT/sales tax around the world, and the seller invoices a single entity. That fits the paušal/d.o.o. bookkeeping model.
- RevenueCat sits on top of the App Store and Google Play billing, so it doesn't change the payout rail.

### Gaps
- Apple payout currency for Serbian bank accounts (USD/EUR vs RSD) and whether payouts arrive by SWIFT. No source found. Background knowledge says Apple pays by EFT/wire in a currency tied to the bank's country. Needs verification in App Store Connect.
- Serbia's row on Paddle's table, the Lemon Squeezy bank list, Creem's full list, Dodo's merchant-onboarding list, FastSpring and Gumroad (Gumroad pays via PayPal/bank; Serbia not verified). The fetch tools were blocked.
- Lemon Squeezy's status after its acquisition by Stripe (background knowledge, July 2024) and whether it's merging into Stripe's products. Not researched.
- Tax treatment of a US LLC owned by a Serbian resident. No source found. Background knowledge: a single-member LLC is disregarded for US tax, and the Serbian resident is taxed on worldwide income. Serbia may treat the LLC as a controlled foreign entity or deem profits domestic if it's managed from Serbia (permanent establishment / place-of-management risk). Needs a Serbian tax advisor.

## Serbian tax treatment of app store / SaaS income (paušal, 6M RSD cap, independence test, d.o.o., VAT)

### Takeaway
A preduzetnik paušalac can earn foreign income, and app-store payouts are foreign income counted toward the 6M RSD (about EUR 51k) annual paušal cap. Over the cap, the business has to move to bookkeeping (knjigaš) or a d.o.o. The independence test targets IT contractors who work like employees for one client. It's aimed at service relationships, not at selling a product to millions of end users through Apple. Even so, Apple/Google/MoR as the "only payer" is a grey area I couldn't confirm with an official source.

### Cited Findings
- **Eligibility and cap:** Preduzetnici who expect annual turnover under 6M RSD can apply for paušal. Crossing 6M forces a switch to bookkeeping — [Biznis.rs](https://biznis.rs/vesti/srbija/preduzetnicima-rok-do-kraja-oktobra-za-prelazak-na-pausalno-oporezivanje/); [Biznis.rs](https://biznis.rs/preduzetnik/novoosnovani-pausalci-placaju-vece-poreze-zbog-promena-u-odredjivanju-osnovice/)
- Foreign-client income counts toward the 6M limit. Every payment must be recorded in the KPO book with no minimum — [Pausalko 2026](https://pausalko.rs/blog/kako-pausalac-da-naplati-od-stranih-klijenata-2026/)
- Income from a paušal business is excluded from the base for annual personal income tax — [Pausalko](https://pausalko.rs/blog/pausalac-i-devizni-racun-firme-sta-sve-treba-da-znate/)
- **Independence test** (since 2020): it has nine criteria, and failing five of them means the income is taxed as employment-like income with no recognized flat expenses. At introduction, one source said most of roughly 11,000 IT preduzetnici didn't actually simulate employment — [N1](https://n1info.rs/biznis/a533854-Nova-poreska-pravila-za-pausalce-problem-za-deo-IT-zajednice/); [Danas](https://www.danas.rs/ekonomija/tri-godine-da-se-it-sektor-uvede-u-poreske-tokove/)
- Startit ran a piece saying paušal is "no longer the best option" and listing alternatives — [Startit](https://startit.rs/pausalni-porez-vise-nije-najbolja-opcija-ali-zato-su-tu-alternative/) (content not retrieved)
- A paušalac can work with EU firms; there's a guide on the tax/VAT aspects — [Pausalko](https://pausalko.rs/blog/da-li-pausalac-moze-da-radi-sa-firmama-iz-eu/)
- **VAT:** Serbian tax-practice sites cover a domestic company selling an app through the Google and Apple stores, under "place of supply" and "invoicing" (opinion dated 2023-11-20). There's also a 2024-11-11 Q&A on app-usage services sold via a website, plus the topic "internal VAT calculation" (reverse charge) — [Neobilten](https://www.neobilten.com/tag/mesto-prometa/?lang=lat) (only titles/tags were visible)
- A 2026 secondary guide (beancount.io) says crossing the paušal ceiling triggers full-profit taxation with no grace period — [beancount.io](https://beancount.io/it/blog/2026/07/30/serbia-pausal-flat-rate-tax-freelancer-guide) (foreign secondary source, couldn't open)

### Inferences
- For an app business, the independence-test criteria (one client, set working hours, client's equipment, and so on) mostly don't fit product sales. Apple/Google act as agent or reseller to millions of end users. The risk is lower than for outsourced dev work, but get an accountant's written opinion.
- A paušalac doesn't control the tax amount. It's set by the Tax Administration from a base tied to activity code and municipality. Background knowledge puts IT (6201) in Belgrade at roughly 35–45k RSD/month total in recent years. Verify the 2026 amount.
- Path: start as paušal. Above about EUR 40–50k a year, or if paušal tax becomes inefficient, move to a d.o.o. (15% corporate profit tax plus 15% withholding on dividends). That works out to about 27.75% effective on distributed profit, and allows real expense deductions (contractors, ads, UGC).

### Gaps
- No official 2026 confirmation (purs.gov.rs) for: the current paušal cap (6M RSD), the second 8M RSD limit (background knowledge: also tied to VAT registration), 2026 paušal amounts, or whether the cap or rules changed for 2026.
- The 15% corporate tax and 15% dividend withholding rates are background knowledge; I didn't retrieve a source this session.
- VAT reverse charge: background knowledge says a non-VAT-registered paušalac may still owe internal VAT on certain services from foreign suppliers (e.g., Apple/Google commission, Meta/Google ads, MoR fees), depending on how the supply is structured. Apple and Google generally act as commissionaire/reseller to the consumer. No authoritative source found; the Neobilten opinion should be retrieved.
- No official ruling found on whether a single MoR/app-store payer triggers the independence test.

## Serbian/Balkan indie founders with successful apps or SaaS

### Takeaway
The standout ex-Yugoslav bootstrapped software success is Serbian: CAKE.com/Clockify (Nenad Milanović, Novi Sad), with $25M+ ARR and profitable. Nordeus (Belgrade, mobile games) sold for up to $378M. True solo indie-app founders from Serbia with public revenue numbers were not findable through search. The Serbian startup press covers few indie app revenue stories.

### Cited Findings
- **CAKE.com / Clockify (Novi Sad, Serbia):** Founder Nenad Milanović. The company is fully bootstrapped with no VC. Milanović puts ARR at $25M–100M, profitable with 96%+ gross margins. Latka estimates Clockify at $26.4M (2023) and CAKE.com at $85.2M ARR (2024); these are third-party estimates. He spent 10 years on side projects before this success — [Expandi interview](https://expandi.io/gtm-expert/nenad-milanovic-cake-com/); [Europe Startup Guide](https://europe-startup-guide.com/serbia/startup/cake-com-clockify); [Latka Clockify](https://getlatka.com/companies/clockify); [Latka CAKE.com](https://getlatka.com/companies/cake.com); [Indie Hackers](https://www.indiehackers.com/post/tech/after-10-years-of-building-side-hustles-this-founder-built-a-25m-arr-success-GN8KEteJuEUDpmtjO6HA); [Starter Story](https://www.starterstory.com/cake-breakdown)
- **Nordeus (Belgrade):** Maker of Top Eleven (240M+ registered users). Take-Two acquired it in June 2021 for up to $378M ($225M upfront, including $90M in stock, plus an EBITDA-based earn-out) — [Business Wire / Take-Two](https://www.businesswire.com/news/home/20210602005247/en/Take-Two-Interactive-Software-to-Acquire-Mobile-Games-Developer-Nordeus); [tech.eu](https://tech.eu/brief/take-two-buys-serbian-games-studio-nordeus-for-378-million-in-cash-stock/)
- **Plausible Analytics:** Bootstrapped, EU-based. Co-founder Marko (search sources didn't confirm surname or Croatian ties). An early interview reported about $4.1k MRR; later sources say $1M+ ARR (undated) — [Failory](https://www.failory.com/interview/plausible); [Wikipedia](https://en.wikipedia.org/wiki/Plausible_Analytics)
- **AgentOS (Panche Isajeski, likely North Macedonia):** His first product, aimed at Balkan payment processing, failed. The relaunch hit $9.5k MRR in two months (IH post dated 2026-10-06) — [Indie Hackers](https://www.indiehackers.com/post/tech/starting-from-scratch-and-hitting-9-5k-mrr-in-two-months-j5pMaED5FEbKw8qmeyj9)
- **Appidemia (Appricot, Serbia):** At one point ranked above Facebook in the Indian App Store, with about 50k active users; no revenue disclosed — [Dnevnik.hr](https://dnevnik.hr/vijesti/tech/aplikacija-iz-srbije-appidemia-u-indiji-popularnija-od-facebooka---405053.html)
- **MyFitWorld (Serbia):** Fitness subscription app founded by DIF graduates. Pricing: EUR 7.49/month or 59.99/year, plus B2B per-employee pricing (article about 3.5 years old) — [Netokracija](https://www.netokracija.rs/myfitworld-206373)
- **Ecosystem:** Netokracija's Startap Skener 2026 found 36.7% of Serbian startups still have no revenue — [Netokracija](https://www.netokracija.rs/startap-skener-2026-226596)
- **Older talk:** Aleksandar Vacić (Radiant Tap) gave "Mobile app biz u Srbiji" talks on doing the App Store business from Serbia — [Speaker Deck](https://speakerdeck.com/radianttap/mobile-app-biz-u-srbiji-1)

### Inferences
- The Serbian precedent is "bootstrapped B2B SaaS with a freemium funnel sold globally" (Clockify) and "mobile F2P games" (Nordeus, plus a strong Serbian game-dev scene). Both point to global English-language products, not local-market ones.
- Clockify's path (years of side projects, then one freemium SEO-driven tool) is a realistic model for a solo founder.

### Gaps
- No Serbian solo indie app founder with verified public revenue (X/#buildinpublic, IH) was found. Searches for Serbian founders on IH and Startit returned nothing relevant. A targeted X search or a TrustMRR/IH country filter would be needed.
- Croatian/Slovenian/Bosnian indie examples weren't researched beyond Plausible (unconfirmed).

## Cost advantages (salaries, freelancers, UGC creators)

### Takeaway
Serbian developers are expensive by local standards but cheap by Western ones. The average net salary in computer programming is about 311k RSD/month (about EUR 2,650) as of Feb 2026, versus a national average of about 120k RSD (about EUR 1,026). For a solo founder, the bigger advantage is low personal cost of living, plus access to regional designers and creators at below-Western rates.

### Cited Findings
- RZS, February 2026: computer programming had the highest average net wage, 311,370 RSD. The national average was 116,127 RSD net / 160,067 RSD gross — [Biznis.rs](https://biznis.rs/vesti/srbija/prosecna-neto-plata-u-februaru-116-127-dinara/)
- June 2026 national average net was 120,401 RSD (about EUR 1,026) — [Kurir](https://biznis.kurir.rs/info-biz/10085965/prosecna-plata-za-jun-2026-nova-statistika-o-zaradama-u-srbiji)
- Earlier figures: programmers at about 285k RSD and above 300k RSD in 2025 releases — [021.rs](https://www.021.rs/info/srbija/424942/programeri-najplaceniji-u-proseku-zaradjivali-285000-dinara); [021.rs](https://www.021.rs/story/Info/Biznis-i-ekonomija/422333/Programeri-i-dalje-medju-najplacenijim-delatnostima-Prosecna-plata-premasila-300000-dinara.html)
- Top Serbian programmers earn up to about EUR 7,500/month (Telegraf analysis) — [Telegraf](https://www.telegraf.rs/amp/hi-tech/edukacija/3318713-analiza-kako-programeri-u-srbiji-zaradjuju-i-do-7500-evra-mesecno)
- Global benchmark: only about 1 in 6 apps clears $1k/month in revenue (RevenueCat data via Croatian press) — [Bug.hr](https://www.bug.hr/biznis/paywall-pretplate-poskupljenja-kako-zivjeti-od-softvera-48436); a 2026 analysis puts the median solo app under $1k/month — [You Could Ship This](https://youcouldshipthis.com/blog/indie-app-revenue-realistic-expectations)

### Inferences
- An app earning $3–5k/month already exceeds the average Serbian programmer's net salary. Breakeven is much lower than for a US founder.
- Since dev salaries are about EUR 2.5k+ net, hiring full-time devs isn't "cheap". Part-time freelance designers and junior devs on paušal contracts are more realistic.
- Many paušal IT freelancers work for foreign clients, so a local contractor pool exists. Watch the independence test if you engage one contractor full-time.

### Gaps
- No 2026 data found on freelance hourly rates for Serbian designers/devs, or on UGC creator rates in the Balkans/Serbia. Not researched due to the tool-call budget.
- Living-cost figures for Belgrade/Novi Sad in 2026 weren't retrieved.
