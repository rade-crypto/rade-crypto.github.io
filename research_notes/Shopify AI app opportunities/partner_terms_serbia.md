# Shopify Partner Terms and Payouts for a Serbian Solo Developer (preduzetnik / paušalac), 2026

> Method note: Research done 2026-10-14. Direct fetches of shopify.dev, help.shopify.com and shopify.com/partners were blocked from the research environment (proxy 403 / DNS failure), and so were several Serbian sites (feruvi.rs, cicapravnica.rs). Findings attributed to Shopify pages come from search-engine excerpts of those official pages, not full-page reads. Re-check exact wording on the live pages before any decision.

## 1. Shopify App Store revenue share, fees, and 2025–2026 changes

### Takeaway
Shopify takes 0% revenue share on a partner's first USD 1M of **lifetime** App Store revenue (counted from 1 Jan 2025; the old annual reset is gone) and 15% above that. It also charges a 2.9% processing fee on Public App sales and a one-time USD 19 App Store registration fee per Partner account. For a solo developer, the effective cost is roughly 2.9% plus the USD 19 fee until lifetime revenue passes USD 1M.

### Cited Findings
- Shopify "sunset the annual exemption reset". Developers keep a revshare exemption on the first USD 1M of **lifetime** revenue and pay 15% on amounts above that. Earnings are aggregated at the partner level, including apps under associated developer accounts — [Shopify dev changelog: Update to Shopify's app developer revenue share](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share) (via search excerpt)
- Earnings before 1 January 2025 do not count toward the USD 1M lifetime threshold. Changes reported as effective 16 June (2025) — [Shopify revenue share docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share); [Hyper.ai summary](https://hyper.ai/ja/headlines/4927cc8277cf29bbb5f930997db0fae5)
- Older structure (2021): 0% on the first USD 1M **annually**, then 15% on marginal revenue, with an annual reset. This is now superseded — [TechCrunch](https://techcrunch.com/?p=2171395)
- One-time USD 19 registration fee per Partner account to list on the Shopify App Store. It is waived for accounts created before 1 Aug 2021 and for developers who only build custom/private apps — [Shopify revenue share docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share); [Shopify Help Center glossary](https://help.shopify.com/en/partners/partner-program/glossary)
- Public Applications accepted for sale through the Shopify App Store are subject to a 2.9% Processing Fee — [Shopify Partner Program Agreement](https://www.shopify.com/partners/terms) (via search excerpt)
- Third-party claim: developers earning USD 20M or more on the App Store, or USD 100M or more in company revenue, get 85% of all revenue (no exemption). Not seen on Shopify's own pages in this research — [Shopify partner program guide (adsx)](https://www.adsx.com/blog/shopify-partner-program-guide); [mktclarity](https://mktclarity.com/blogs/news/shopify-apps-new-revenue-share-policy)

### Inferences
- A solo Serbian developer will almost certainly stay under USD 1M lifetime for years, so the practical cost is the 2.9% processing fee, the USD 19 registration fee, and payout/FX costs (section 2).
- Because the threshold is aggregated at the partner level, splitting apps across several partner accounts does not reset it.

### Gaps
- I could not verify whether the 2.9% processing fee applies within the 0% tier. The agreement text excerpt suggests it applies to all Public App sales. Confirm on the live Partner Program Agreement.
- No 2026-specific change beyond the June 2025 lifetime rule was found.

## 2. Payout methods, Serbia support, PayPal Serbia, Balkan developer issues

### Takeaway
Shopify Partner payouts run through Hyperwallet (a PayPal company) with three possible methods: PayPal, bank account, and wire transfer. The methods available depend on the partner's country and payout currency, and no public source confirms which ones Shopify offers for Serbia. PayPal Serbia accounts can receive money but withdraw only to Visa cards (not to RSD bank accounts). Hyperwallet's own docs suggest Serbia supports wire transfer rather than local bank deposit. The definitive check is the Partner Dashboard payout screen (Settings > Payouts > Manage payout method) with Serbia selected.

### Cited Findings
- Payout methods: PayPal, Bank Account, Wire Transfer. Which ones a partner gets depends on country/region and the payout currency. Options are checked in Partner Dashboard > Settings > Payouts > Manage payout method — [Shopify Help Center: payout method](https://help.shopify.com/en/partners/manage-account/manage-payouts-invoices/payout-method)
- Per-payout caps: PayPal up to USD 100,000; Bank Account up to USD 500,000; Wire up to USD 5,000,000. Caps may be lower depending on country/currency — [Shopify Help Center: payout method](https://help.shopify.com/en/partners/manage-account/manage-payouts-invoices/payout-method)
- Payouts are managed through Hyperwallet, and partners must create a Hyperwallet account in the Partner Dashboard first. **Virtual bank accounts such as Payoneer are not supported** for Partner payouts. A real bank account is required — [Shopify Help Center: payout method](https://help.shopify.com/en/partners/manage-account/manage-payouts-invoices/payout-method)
- Schedule: earnings for the 1st–15th are paid 5 business days after the 15th, and earnings for the 16th–month-end 5 business days after month-end. Sales and referral earnings are tracked separately, each with its own threshold — [Shopify Help Center: Getting paid](https://help.shopify.com/en/partners/getting-started/getting-paid?itcat=partner_blog&amp;amp;amp=&amp;amp;itterm=payout_methods)
- Minimum payout of USD 25 is reported by third parties only. Non-USD conversion is done by Hyperwallet, with its own fees — [hulkapps](https://www.hulkapps.com/blogs/shopify-hub/understanding-shopify-payouts-schedule-methods-and-best-practices); [Shopify Help Center: getting paid](https://help.shopify.com/en/partners/partner-program/getting-paid)
- Hyperwallet transfer-method docs list Serbia with Bank Deposit "-" (not available) and a local wire option in RSD — [Hyperwallet docs: bank account](https://docs.hyperwallet.com/content/transfer-methods/v1/bank-account) (via search excerpt)
- A third-party Hyperwallet country list (WorkMarket, not Shopify-specific) shows Serbia under Wire Transfer in AUD/EUR/GBP/USD with a 2% fee — [WorkMarket Hyperwallet supported countries](https://workmarket.zendesk.com/hc/en-us/articles/31431909954455-Hyperwallet-Supported-Countries-and-Transfer-Fees)
- PayPal's developer docs list Serbia under the "Send, receive, and withdraw" feature set — [PayPal Payouts supported features](https://developer.paypal.com/payouts/supported-features). A third-party list marks "Serbia & Montenegro" unsupported, but that list looks outdated — [cs-cart](https://www.cs-cart.com/blog/paypal-countries-availability/)
- PayPal receiving has been enabled in Serbia since 8 October (2018) — [B92](https://www.b92.net/o/tehnopolis/komentari?nav_id=896649); [webinfo.rs](https://www.webinfo.rs/becej/111-info/6479-paypal-primanje-uplata-omoguceno-i-u-srbiji)
- From a Serbian PayPal account you cannot withdraw directly to an RSD current account. Withdrawals go to a **Visa** card only (Mastercard funds stay stuck on the balance). Minimum withdrawal is EUR 10 and takes a few business days. Reported fees are about 3.4% + fixed fee to receive and about 4% for PayPal currency conversion. Sources recommend using the bank's conversion rather than PayPal's — [Feruvi: PayPal u Srbiji](https://feruvi.rs/blog/paypal-srbija); [ITNetwork PayPal guide](https://www.itnetwork.rs/paypal-u-srbiji-ultimativni-vodic-za-prezivljavanje-u-digitalnoj-ekonomiji-zaobilazenje-birokratije-i-naplatu-vaseg-rada-bez-da-poludite/) (via search excerpts)
- An older comment says linking Payoneer to a Serbian PayPal account is no longer possible — [milos.io](https://milos.io/kako-da-primate-novac-u-srbiji-sa-paypal-a-na-payoneer-karticu/)

### Inferences
- The most likely workable route for a Serbian preduzetnik is a **wire transfer (USD or EUR) via Hyperwallet to the preduzetnik's foreign-currency (devizni) business account** at a Serbian bank. This is likely, not confirmed, and the reported fee is about 2% per transfer.
- PayPal is a fallback. For a registered preduzetnik, money landing in PayPal and then on a Visa card is awkward for bookkeeping: the income still has to be booked, and business income should flow to the business account.
- Expect FX losses at two points: Hyperwallet conversion, then Serbian bank conversion to RSD. Receiving USD/EUR to a devizni account avoids Hyperwallet's conversion.

### Gaps
- No primary Shopify source lists the payout methods available for Serbia. No Serbian or Balkan developer testimonials on Shopify Partner payouts were found. This must be verified empirically in the Partner Dashboard (free to sign up) before building.
- Whether PayPal business accounts for Serbian preduzetnici work differently from personal accounts was not established.

## 3. Tax forms, US withholding, and Serbian tax treatment (preduzetnik / paušalac)

### Takeaway
Non-US payees typically submit W-8BEN (individual / sole proprietor) or W-8BEN-E (entity). I could not confirm Shopify's exact form workflow. There is **no US–Serbia income tax treaty**, so where US-source income is involved the default 30% US withholding cannot be reduced by treaty. App income paid by Shopify (a Canadian company) for services performed in Serbia is generally not US-source, which is what the W-8 certifies. On the Serbian side, foreign income counts toward the 6M RSD paušal cap. Turnover from services supplied abroad reportedly does not count toward the 8M RSD VAT threshold. Whether App Store app sales qualify for paušal at all is genuinely uncertain and needs an accountant or Poreska uprava ruling.

### Cited Findings
**US forms / withholding**
- W-8BEN is for non-US individuals who are the beneficial owner of income. W-8BEN-E is for foreign entities. Without a valid form, the payer withholds 30% (or 24% backup withholding in some cases) — [salaccounting W-8BEN guide](https://salaccounting.ca/blog/form-w8ben-guide/); [Deel glossary](https://www.deel.com/glossary/form-w-8ben/)
- W-8 forms generally expire at the end of the third calendar year after signing — [eBay Partner Network tax forms](https://partnernetwork.ebay.co.uk/resources/how-to-submit-your-tax-information)
- Some platforms don't require tax forms from non-US partners working only with non-US companies — [impact.com](https://help.impact.com/en/support/solutions/articles/48001236645-electronic-tax-documents-for-partners-explained) (shown for comparison; not Shopify-specific)
- No US–Serbia income tax treaty is in force in 2026, and Serbia is not on the IRS treaty A–Z list. One law-firm page contradicts this but looks wrong — [omnivoo (May 2026)](https://omnivoo.com/blog/paying-serbian-contractors-from-us-company); [BrightTax Serbia](https://brighttax.com/countries/serbia/); contradicted by [Zunic Law](https://zuniclaw.com/en/double-taxation-serbia)

**Serbian tax**
- Paušal eligibility: total annual income must not exceed **6,000,000 RSD**, and foreign income is included — [Aktiva sistem](https://aktivasistem.com/news/porez-freelancer-prihod-iz-inostranstva/); [cicapravnica 2026 paušal guide](https://cicapravnica.rs/pravni-saveti/pausalno-oporezivanje-preduzetnika)
- An increase of the paušal cap to 8M RSD was requested but was reported as tied to EU accession, not enacted — [biznis.rs](https://biznis.rs/vesti/srbija/privrednici-traze-povecanje-limita-za-pausalno-oporezivanje-na-osam-miliona-dinara/); [biznis.rs](https://biznis.rs/vesti/srbija/kada-prekoracenje-limita-menja-poreski-status-preduzetnika/)
- VAT threshold: 8,000,000 RSD of turnover in the previous 12 months, unchanged in 2026. Registering for VAT ends paušal status — [biznis.rs](https://biznis.rs/preduzetnik/porezi/pausalcima-se-nece-menjati-granica-za-ulazak-u-pdv/); [Aktiva sistem](https://aktivasistem.com/news/freelancer-porez-na-uplate-iz-inostranstva/)
- A secondary news piece says the 8M VAT limit counts only turnover within Serbia, so invoicing foreign clients does not count toward it. This should be verified against the Zakon o PDV — [biznis.rs](https://biznis.rs/vesti/srbija/sta-sve-ne-ulazi-u-godisnji-limit-za-pausalce/)
- Paušalci not in the VAT system generally don't charge VAT on invoices to foreign clients, but VAT obligations can arise (e.g., on imported services) — [Aktiva sistem](https://aktivasistem.com/news/freelancer-porez-na-uplate-iz-inostranstva/)
- Foreign-currency income is recorded in the KPO book in RSD at the NBS middle rate — [pitajknjigovodju.rs 2026](https://pitajknjigovodju.rs/prihodi-od-inostranstva-porez-srbija/)
- Credit for foreign tax depends on a double-tax treaty, and with the US there is none — [Aktiva sistem](https://aktivasistem.com/news/porez-freelancer-prihod-iz-inostranstva/)
- Activity code 62.01 (computer programming) covers writing, testing and maintaining software. Sources conflict on whether it covers publishing or selling packaged software for wide use — [epreduzetnik 62.01](https://epreduzetnik.rs/sifra_delatnosti/informisanje-i-komunikacije/racunarsko-programiranje-konsultantske-i-s-tim-povezane-delatnosti/racunarsko-programiranje-konsultantske-i-s-tim-povezane-delatnosti/racunarsko-programiranje/); [epreduzetnik 62.0](https://epreduzetnik.rs/sifra_delatnosti/informisanje-i-komunikacije/racunarsko-programiranje-konsultantske-i-s-tim-povezane-delatnosti/racunarsko-programiranje-konsultantske-i-s-tim-povezane-delatnosti/)
- Paušalci reportedly cannot engage in trade or resell licenses. They can invoice only their own services or products — [bandd.abit.rs FAQ](https://bandd.abit.rs/najcesca-pitanja-novih-pausalaca-evo-odgovora/)
- The independence test (test samostalnosti) has 9 criteria, and failing 5 makes you a non-independent worker. One criterion is 70%+ of income from a single client — [bandd.abit.rs](https://bandd.abit.rs/najcesca-pitanja-novih-pausalaca-evo-odgovora/); [unija.com](https://unija.com/sr/da-li-ce-programeri-pausalci-otici-zbog-izmena-zakona/)
- Paušalci need a fiscal cash register when selling goods at retail or providing services to individuals. A programmer invoicing companies with payment to an account generally does not — [bandd.abit.rs](https://bandd.abit.rs/najcesca-pitanja-novih-pausalaca-evo-odgovora/)

### Inferences
- **Selling your own app is your own product, not resale of a third party's licenses**, so the "no trade" restriction plausibly does not bite. Activity code fit (62.01 vs 58.29 software publishing) still matters and is unresolved.
- **The test samostalnosti risk is ironic here.** Under the Partner Agreement, Shopify collects merchant charges and pays the partner, so on paper nearly 100% of income may come from one payer (Shopify). That could trip the 70%-single-client criterion. Whether Poreska uprava treats Shopify as the "client" or the underlying merchants as clients is unknown. Ask an accountant.
- Merchants are businesses and the money arrives by bank transfer from a foreign payer, so a fiscal register is likely unnecessary. This is not confirmed.
- **Reverse-charge VAT.** Shopify's fees (the USD 19 fee, the 2.9% processing fee, any revenue share) are services from a foreign supplier to the Serbian preduzetnik. Under the Serbian VAT law, a non-VAT-registered recipient may still owe reverse-charge VAT (20%) on such services as poreski dužnik. This is a known pitfall to raise with an accountant. I found no source confirming it for paušalci.
- **Revenue headroom.** 6M RSD is roughly EUR 51k/yr, at ~117 RSD/EUR (my approximation, not sourced). Exceeding it forces a switch to bookkeeping (knjigaš) or a d.o.o.
- US withholding should not apply if a W-8BEN is on file and the income is from services performed outside the US. Without a treaty, though, there is no fallback reduced rate.

### Gaps
- Shopify's exact tax-form workflow (which W-8 form, which contracting entity — Shopify Inc. Canada vs. another affiliate) was not verified, because Shopify pages could not be fetched.
- No official Poreska uprava (purs.gov.rs) opinion was found on app-marketplace income under paušal.
- Reverse-charge VAT handling for a paušalac receiving Shopify's services is not confirmed by any source.

## 4. Shopify App Store publishing requirements (review, GDPR webhooks, Billing API, Built for Shopify)

### Takeaway
To list a paid app, the developer must charge through Shopify's Billing API or Managed App Pricing (no external billing) and implement the three mandatory privacy/compliance webhooks with HMAC verification. The app must also pass Shopify's manual review; new public apps reportedly must use the GraphQL Admin API. Built for Shopify (BFS) is an optional, stricter tier with performance, design and traction thresholds.

### Cited Findings
- Apps must implement Shopify App Pricing (Managed Pricing) or the Shopify Billing API correctly. Merchants must be able to upgrade or downgrade plans without contacting support or reinstalling — [Shopify App Store requirements](https://shopify.dev/docs/apps/launch/shopify-app-store/app-store-requirements) (via excerpt); [codersy 2026](https://www.codersy.com/blog/shopify-api-development-best-practices/shopify-app-store-guidelines-updates-2026)
- The mandatory compliance webhooks are `customers/data_request`, `customers/redact` and `shop/redact` (the last fires about 48h after uninstall). Reviewers test them, and stub handlers are a common rejection cause — [triadmark BFS checklist](https://www.triadmark.com/blog/built-for-shopify-app-review-checklist); [digitalheroes submission checklist](https://digitalheroesco.com/journal/shopify-app-submission-checklist/)
- Security: HMAC verification on the raw request body, encrypted token storage, and minimal scopes — [adsx security checklist](https://adsx.com/blog/shopify-app-security-checklist)
- New public apps must use the GraphQL Admin API only. Sources disagree on the date (1 Apr 2025 vs Apr 2026) — [codersy](https://www.codersy.com/blog/shopify-api-development-best-practices/shopify-app-store-guidelines-updates-2026); [eseospace](https://eseospace.com/blog/shopify-app-store-approval/)
- BFS reportedly requires admin Web Vitals within budget, **at least 50 net paid installs and 5 reviews**, and Polaris-aligned design (third-party claim) — [adsx BFS badge requirements](https://adsx.com/blog/built-for-shopify-badge-requirements)
- BFS also limits how much an app may lower storefront Lighthouse scores — [eseospace](https://eseospace.com/blog/shopify-app-store-guide/)
- BFS category changes: returns/exchanges and subscription apps must use the Customer Account API by 1 Dec 2026. Fulfillment-service thresholds were adjusted 1 Aug 2026 — [Shopify changelog: BFS returns/subscriptions](https://shopify.dev/changelog/built-for-shopify-requirements-for-returns-and-exchanges-and-subscription-apps.md); [Shopify changelog: fulfillment services](https://shopify.dev/changelog/updated-built-for-shopify-requirements-for-fulfillment-services-apps.md)
- Official BFS requirements page — [shopify.dev BFS requirements](https://shopify.dev/docs/apps/launch/built-for-shopify/requirements) (content not retrieved)
- BFS review reportedly adds 2–4 weeks — [codersy](https://www.codersy.com/blog/shopify-api-development-best-practices/shopify-app-store-guidelines-updates-2026)

### Inferences
- Mandatory Shopify billing means all revenue flows through Shopify and then Hyperwallet. The payout question (section 2) is therefore make-or-break: you cannot route App Store merchants to Stripe or Paddle instead.
- BFS cannot be obtained at launch, because it needs traction (installs and reviews). Plan it as a post-launch milestone.

### Gaps
- Exact BFS numeric thresholds (LCP/CLS/INP limits, rating floor) were not retrieved from Shopify's page.
- Current review turnaround times for 2026 were not found from a primary source.

## 5. Alternatives if Shopify payouts to Serbia don't work

### Takeaway
Options are limited. Shopify explicitly rejects virtual bank accounts (Payoneer and similar) for Partner payouts, and Wise does not offer balance holding for Serbian residents. Realistic options are a Hyperwallet wire to a Serbian devizni account, PayPal (Visa-card withdrawal), or, last resort, a foreign entity or bank account (e.g., an EU/US company), which changes the whole tax picture.

### Cited Findings
- Payoneer and other virtual bank accounts are not supported as Shopify Partner payout bank accounts — [Shopify Help Center: payout method](https://help.shopify.com/en/partners/manage-account/manage-payouts-invoices/payout-method)
- Payoneer's Serbian page says Serbian users can receive from major markets and withdraw to a local bank account, with a 0.5% inter-balance conversion fee — [Payoneer SR](https://www.payoneer.com/sr/resources/how-to-use-payoneer/primite-uplatu-bankovni-racun/)
- Payoneer pricing (updated 1 Jan 2026) is reported as 1% (min USD 1) to receive non-local currency, with bank withdrawals at 1.2%–4% depending on route — [quasa.io](https://quasa.io/sr/media/wise-ili-payoneer-kartica-i-konverzija-pojedu-razlicit-deo-uplate); [beancount 2026](https://beancount.io/ja/blog/2026/07/26/wise-vs-payoneer-freelancers-cross-border-payment-fees-guide)
- Nuvei agreed to acquire Payoneer for about USD 2.75B (June 2026), with closing expected by mid-2027 — [quasa.io](https://quasa.io/sr/media/wise-ili-payoneer-kartica-i-konverzija-pojedu-razlicit-deo-uplate) (secondary)
- Wise: Serbia is reportedly not on Wise's list of countries where residents can hold money. Wise is useful mainly for senders paying into Serbian accounts — [quasa.io](https://quasa.io/sr/media/wise-ili-payoneer-kartica-i-konverzija-pojedu-razlicit-deo-uplate)
- Payoneer's own Shopify payouts guide (merchant-oriented) — [Payoneer](https://www.payoneer.com/resources/general-payments/shopify-payouts-withdrawal/)

### Inferences
- Payoneer could still be a route for non-Shopify income, e.g., selling the same tool off-platform. For off-platform SaaS billing, Paddle or Lemon Squeezy (merchant-of-record) are commonly used by Serbian developers, but this research did not verify that.
- If neither Hyperwallet wire nor PayPal works for a Serbian partner, the fallback is a foreign entity (e.g., a US LLC or Estonian e-Residency OÜ) with its own bank account. That entity would then file W-8BEN-E or W-9, which adds cost and Serbian CFC/tax-residency complexity.

### Gaps
- No confirmed Serbian or Balkan developer report of successfully receiving Shopify Partner payouts was found, either positive or negative. This is the single most important item to verify, by creating a free Partner account and checking the payout-method screen with Serbia as the country.
- The Paddle / Lemon Squeezy option for Serbia was not researched (out of scope).
