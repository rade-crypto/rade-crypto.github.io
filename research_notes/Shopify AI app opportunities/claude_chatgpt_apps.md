# Building Apps for Claude and ChatGPT (MCP / Apps SDK): Opportunity Assessment for a Solo Developer in Serbia (Oct 2026)

Method note: WebFetch failed for every primary domain tried (DNS errors: developers.openai.com, paddle.com, pasqualepillitteri.it), so these notes rely on search-result snippets. Quotes and numbers come from those snippets, and many sources are secondary or vendor blogs. Verify the key facts (OpenAI digital-goods policy, Paddle/Lemon Squeezy/Creem country lists) on the primary pages before making decisions.

## 1. Distribution channels in 2026: what exists, paid listings, revenue share, built-in billing, real discovery

### Takeaway
Both Anthropic and OpenAI now have free, reviewed directories for third-party MCP connectors and apps. Neither offers built-in billing or a revenue share that an indie developer can use for subscriptions. OpenAI explicitly bans selling digital goods or subscriptions inside ChatGPT apps, and the discovery/traffic reports are weak. Treat these directories as a trust badge and an acquisition channel for your own SaaS, not as an App Store-style business.

### Cited Findings
**Anthropic / Claude**
- Anthropic opened a directory submission portal on Sept 25, 2026. It is open to developers on paid Claude plans and does not require Anthropic partner status. The portal reportedly sits at claude.ai/directory/manage and shows submission status at each stage, replacing an older Console form. Developers can submit a single MCP connector (a remote MCP server) or plugins that bundle connectors and/or Agent Skills. No submission fee was found. — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/18444/anthropic-portal-submit-plugins-mcp-connectors-claude); [Claude: Build plugins for Claude](https://claude.com/resources/articles/build-plugins-for-claude)
- Review times vary. Reddit posts from Aug 2026 report about 2 months from submission to listing in one case and about 20 days in another (anecdotal). — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1vfyomj/snapshots/2026-08-06T19%3A47%3A15.7352Z)
- The directory accepts three submission types: remote MCP servers, desktop extensions (MCPB bundles), and "MCP Apps" (servers that render interactive UI; these need 3–5 screenshots). — [Claude docs: submission](https://claude.com/docs/connectors/building/submission); [sunpeak.ai (May 2026)](https://sunpeak.ai/blogs/claude-connector-directory-submission)
- Claude Marketplace launched in March 2026 with only 6 partners (GitLab, Harvey, Lovable, Replit, Rogo, Snowflake). On Sept 23, 2026 it broadened to 2,000+ plugins and connectors, and developers, vendors and integrators can apply. Enterprise customers can pay for listed products from part of their Anthropic spend commitment, but that mechanism is a limited preview. — [SiliconANGLE (Mar 6 2026)](https://siliconangle.com/2026/03/06/anthropic-launches-claude-marketplace/); [BleepingComputer](https://bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors); [it-connect](https://www.it-connect.tech/claude-marketplace-grows-fast-anthropic-brings-2000-connectors-and-plugins-together/)
- Revenue share is unclear. Bloomberg reported in March that Anthropic would not take a cut of Marketplace purchases, but coverage of the September launch says the announcement doesn't address commission. — [Shopifreaks](https://www.shopifreaks.com/anthropic-is-launching-a-marketplace-for-ai-software/); [xenospectrum](https://xenospectrum.com/en/claude-marketplace-connectors-enterprise-procurement/)
- Inference from the above: the commit-spend purchasing route targets enterprise vendors, not $20/month self-serve indies.

**OpenAI / ChatGPT**
- ChatGPT app submissions opened to all developers on Dec 17, 2025 through the OpenAI Developer Platform, along with an App Directory. Apps that miss quality or safety bars are rejected, and only one version can be under review at a time. — [the-decoder](https://the-decoder.com/openai-launches-app-submissions-and-rolls-out-store-in-the-new-year/); [NOVALOGIQ](https://novalogiq.com/2025/12/18/openai-now-accepting-chatgpt-app-submissions-from-third-party-devs-launches-app-directory/); [Yahoo Tech](https://tech.yahoo.com/ai/chatgpt/articles/connector-era-over-now-submit-093446755.html)
- OpenAI's submission guidelines forbid selling digital products or services inside apps, including subscriptions, digital content, tokens and credits. Apps may link out to external sites for physical goods. OpenAI says it is "exploring" digital goods. I could not confirm whether this changed by Oct 2026. — [dforce.com.ua (2026)](https://dforce.com.ua/en/blog/how-to-build-a-chatgpt-app/); [Moburst](https://www.moburst.com/blog/chatgpt-app-directory-explained-what-brands-need-to-know/); [Forklog](https://forklog.com/en/openai-introduces-in-app-store-for-chatgpt/)
- An OpenAI community thread from Jan 2026 asks for the standard pattern for in-app purchases, subscriptions and usage billing, and gets no clear official answer. — [OpenAI Community](https://community.openai.com/t/chatgpt-app-monetization-apps-sdk/1372343.md)
- In March 2026 OpenAI moved away from Instant Checkout (in-chat purchase via Stripe/ACP). Purchases now happen in merchant-run apps with the merchants' own checkouts, and OpenAI focuses on discovery. The buy-button conversion rate was reportedly below 1%, against a 3–4% industry average. Shopify reportedly said it will not build a checkout app. — [Digital Commerce 360 (Mar 6 2026)](https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/); [Shopifreaks](https://www.shopifreaks.com/openai-pivots-from-instant-checkout-to-an-app-based-shopping-model-inside-chatgpt/); [Retail Insight Network](https://www.retail-insight-network.com/newsletters/openai-shifts-chatgpt-shopping-plans-to-retailer-run-apps-report)
- The GPT Store came up in no 2026 source as a monetization channel. One 2026 report says OpenAI now calls its "Plugins Directory" the main place users discover workflow capabilities. This is a secondary source, and the naming is unclear. — [li.solutions](https://li.solutions/blog/chatgpt-apps-sdk/)

**Discovery and traffic**
- Partner companies reportedly got little traffic from their ChatGPT apps. Users struggle to find apps, approvals are slow, and developers get almost no performance data. Bloomberg, via Modern Retail, reports complaints about tedious approval, a buggy SDK and missing usage data. One app developer told Modern Retail that adoption and conversion are "pretty low". — [Modern Retail](https://www.modernretail.co/technology/retailers-are-rushing-to-build-ai-apps-its-unclear-if-shoppers-will-use-them/); [PYMNTS 2026](https://www.pymnts.com/artificial-intelligence-2/2026/openai-aims-to-improve-developer-experience-around-third-party-chatgpt-apps/)
- Approval does not guarantee visibility, directory placement or conversational recommendation. Surfacing depends on model and context, and OpenAI says it is still experimenting with it. One estimate cites about 300 apps against 900M weekly users. — [li.solutions](https://li.solutions/blog/chatgpt-apps-sdk/); [stealwhatworks](https://stealwhatworks.com/blogs/news/chatgpt-apps-make-money-now)

### Inferences
- Neither platform gives a solo developer an equivalent of Shopify's App Store, where merchants search a category, install, and get billed through Shopify Billing API with an 80/20 or 100%-under-$1M share. Here you have to run your own billing (MoR) and send users from the directory to your own signup/OAuth.
- The listing still matters: it adds trust and in-client install discoverability. Claude's directory (2,000+ items) is less crowded than the 24k-server open MCP ecosystem.
- ChatGPT's ban on digital-goods sales means you can't upsell inside the app. The paid relationship has to exist on your own site, with OAuth linking the account.

### Gaps
- Official OpenAI Apps SDK monetization page (developers.openai.com/apps-sdk) could not be fetched. Whether digital-goods sales were allowed by Oct 2026 is unconfirmed.
- No hard install or traffic numbers were found for Claude directory listings.
- Anthropic's Marketplace commission terms are unconfirmed.

## 2. How indie developers monetize MCP servers / ChatGPT apps; revenue numbers and case studies

### Takeaway
Most monetization is a normal SaaS subscription or API key with MCP as an access channel. Marketplaces (Apify, mctx, MCPize, ATXP/FluxA pay-per-call) exist but are small. No credible, verified indie MCP revenue case study was found, and sources estimate fewer than 5% of MCP servers are monetized at all.

### Cited Findings
- The MCP spec has no billing. The two options are (a) tying usage to an account on your own service via OAuth or API key and metering/billing there, or (b) a marketplace that bundles payments, auth and hosting. — [dev.to (2026)](https://dev.to/hopkins_jesse_cdb68cfa22c/how-to-actually-monetize-your-mcp-server-in-2026-without-giving-away-free-labor-fhp)
- Industry estimates put monetized MCP servers below 5%. A typical server is a weekend project wrapping a public API. Price points are low ($5–$50/month) and churn is real. Custom MCP builds for clients sell for $8k–$50k+ plus retainers. — [mcpize.com](https://mcpize.com/blog/make-money-with-mcp); [a8gent.com](https://a8gent.com/blog/sell-mcp-servers-monetize-guide)
- Document and knowledge-base MCP servers often charge $15–$30/month for "unlimited" fair use. Without fair-use caps, one heavy user can turn a server into a loss leader. — [godberrystudios (2026)](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)
- Apify uses pay-per-event: `Actor.charge('eventName', count=N)`. A third party reports Apify pays out about 80% of charged events. — [Apify](https://apify.com/mcp/developers); [getchatads](https://www.getchatads.com/blog/tools-for-monetizing-mcp-servers/)
- mctx's own pages contradict each other: the docs say 0% platform fee (Stripe fees only), while the marketing page says 80/20. — [mctx docs](https://docs.mctx.ai/monetize/overview); [mctx.ai](https://mctx.ai/mcp-monetize)
- Agent-pays-per-call models exist: ATXP (agents pay from wallets) and FluxA (price per tool call). Ad models exist too: Agentic Ads (70% rev share) and ChatAds. All are early-stage vendor claims. — [ATXP](https://docs.atxp.ai/developers/monetize.md); [FluxA](https://fluxapay.substack.com/p/start-charging-agents-for-tools-tutorial); [skillselion](https://skillselion.com/mcp/tool/io.github.nicofains1/agentic-ads)
- On whether ChatGPT apps make money at all, one 2026 commentary says not directly yet. — [stealwhatworks](https://stealwhatworks.com/blogs/news/chatgpt-apps-make-money-now)
- General indie context (TrustMRR dataset): 67.8% of businesses earned less than $1k lifetime and 0.9% passed $1M. The same piece argues that products whose value is mostly saving coding time lose value as AI makes software cheap, while data and proprietary-info products hold up better (e.g. TrustMRR, DataFast). — [buildmvpfast (2026)](https://www.buildmvpfast.com/blog/saas-only-way-out-indie-hacker-dream-desperation-2026)

### Inferences
- At $5–$50/month, $20k MRR means roughly 400–4,000 paying users. That is realistic only if the product is a real SaaS (own data or workflow) where MCP is one surface. A thin wrapper around someone else's API won't get there.
- Marketplaces such as Apify suit usage-based data/scraping tools and handle payouts, which could help from Serbia. Their real earnings potential is unverified.

### Gaps
- No verified MRR case study for an MCP-first or ChatGPT-app-first indie product. Reddit r/mcp and r/SaaS threads didn't come up in search.
- No traffic or revenue numbers for Smithery or mcp.so. Neither appears to offer billing (unconfirmed).

## 3. In-demand but underserved connector categories

### Takeaway
The open MCP ecosystem is crowded (~24k servers, 33% remote), so generic categories are taken. The gaps are long-tail and regional SaaS without official servers, regulated verticals that need compliance controls, and proprietary or vertical data. Shopify itself now ships official MCP servers, so a generic Shopify MCP is commoditized.

### Cited Findings
- One registry analysis counts 24,011 MCP servers, of which 7,839 (33%) expose a remote URL. — [mcpplaygroundonline](https://mcpplaygroundonline.com/blog/why-your-saas-needs-an-mcp-server)
- Buyers are starting to prefer vendors with an official MCP server; one source cites a viral Aug 2026 post from a Resend employee. This is opinion, not survey data. — [mcpplaygroundonline](https://mcpplaygroundonline.com/blog/why-your-saas-needs-an-mcp-server.md); [naoma.ai](https://naoma.ai/blog/should-your-saas-have-an-mcp-server)
- Regional gap example: the "mcp-jp" project exists because Japanese SMB SaaS tools lack official MCP support. — [Enterprise DNA](https://enterprisedna.co/directories/mcp/mediiiiium-mcp-jp)
- Regulated verticals need audit logs and data residency (finance) or HIPAA and PHI restrictions (healthcare). — [shyft.ai](https://www.shyft.ai/blog/mcp-servers-by-industry)
- MCP directories run request pages for missing servers, which can serve as demand signals. — [mcpbundles](https://www.mcpbundles.com/request-mcp-server)
- Shopify has official MCPs: Storefront MCP (every store at /api/mcp), Dev MCP, Customer Account MCP (OAuth 2.0 + PKCE), Checkout MCP (preview), and Catalog MCP. Agentic Storefronts made stores discoverable in ChatGPT by default for eligible US merchants on Mar 24, 2026. In Jan 2026 Shopify announced UCP with Google. All of this is from third-party blogs. — [chattergo](https://www.chattergo.com/blog/shopify-mcp-ecosystem-deep-dive-developer-ai-platform); [shopify.tenten.co](https://shopify.tenten.co/shopify-ai-dev-ecosystem-mcp-server-the-cto-s-guide-to-agentic-commerce-architecture-in-2026); [Polar Analytics](https://www.polaranalytics.com/post/shopify-mcp-server-connect-your-store-to-claude-ai)
- Existing Shopify-to-Claude analytics products are already on the market, e.g. Polar Analytics offering a Shopify MCP to Claude. — [Polar Analytics](https://www.polaranalytics.com/post/shopify-mcp-server-connect-your-store-to-claude-ai)

### Inferences (concrete opportunity shapes)
- **Cross-tool merchant analytics or ops via MCP** (Shopify + ads + email + inventory merged into one queryable layer). Shopify's official MCPs cover store and catalog, not cross-platform analytics. This overlaps with incumbents like Polar Analytics.
- **Regional or long-tail SaaS connectors** (Balkan/EU accounting such as e-invoicing (SEF in Serbia), local couriers, regional marketplaces) where vendors won't build official servers. Willingness to pay may be low, and vendors may later ship official servers.
- **"MCP-ify your SaaS" for small SaaS vendors** (done-for-you or hosted). This is closer to services, and it conflicts with the no-sales-calls constraint.
- **Vertical data products exposed via MCP plus a web dashboard** (data moat). This matches the finding that proprietary data holds value.
- **Hybrid with Shopify:** a Shopify app (paid via Shopify Billing, which avoids the MoR problem) that also exposes its data to Claude/ChatGPT via MCP. Distribution and billing come from Shopify, and the AI connector becomes a differentiator.

### Gaps
- No quantitative demand ranking (search volume, request counts) was found.
- No data on Serbian or Balkan SaaS MCP coverage.

## 4. Payment collection from Serbia (Stripe and merchant-of-record options)

### Takeaway
Stripe is still unavailable to Serbian-registered businesses; no 2026 launch was found. Polar is the one MoR whose docs explicitly list Serbia. Paddle doesn't list Serbia as unsupported, so it is likely OK, but not confirmed directly. Lemon Squeezy (via PayPal or bank payouts) and Creem need checking against their full tables. Stripe Managed Payments (Stripe's MoR) would need a Stripe-supported country.

### Cited Findings
- Stripe is not available to businesses in Serbia as of 2026, per incorporation consultancies (which have a commercial interest in selling workarounds). Earlier confirmations come from Jotform (Jun 2023) and RevenueCat (Jan 2024). The usual workaround is a US LLC or UK Ltd. — [incorpuk (2026)](https://incorpuk.com/blog/how-to-open-stripe-account-in-serbia/); [Osome](https://osome.com/uk/blog/open-stripe-business-account-serbia); [Zenind](https://www.zenind.com/help/post/how-to-open-a-stripe-account-in-serbia-with-a-us-llc); [Jotform](https://www.jotform.com/sr/answers/5259575-how-to-make-stripe-work-in-serbia); [Stripe availability](https://support.stripe.com/questions/stripe-feature-availability-by-country)
- **Polar:** Serbia is on Polar's MoR supported-countries list. Payouts are open to individuals and companies in supported countries even where standalone Stripe is invite-only. One review says Polar covers about 120 payout countries via Stripe Connect. — [Polar docs](https://polar.sh/docs/documentation/polar-as-merchant-of-record/supported-countries); [fungies.io](https://fungies.io/lemonsqueezy-alternatives-2/)
- **Paddle:** Paddle works with software businesses anywhere except an unsupported list of sanctioned or high-risk jurisdictions (e.g. Belarus, Russia, Cuba, Iran, Syria). Serbia was not in the retrieved snippets. Paddle may request more information on any account. Fees are 5% + $0.50. — [Paddle help](https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle); [Paddle developer: supported countries](https://developer.paddle.com/concepts/sell/supported-countries-locales); [Payhip](https://payhip.com/blog/dodo-payments-alternatives/)
- **Lemon Squeezy:** You can sell if you can be paid into a bank or PayPal account in a supported country. PayPal payouts cover 200+ countries, and bank payouts are in USD. Serbia's presence on the bank list was not confirmed (the snippet was truncated). Effective fees for non-US sellers can reach about 6.5–7%. Stripe bought Lemon Squeezy in Jul 2024, and as of a Sept 2026 review it still runs standalone. — [LS supported countries](https://docs.lemonsqueezy.com/help/getting-started/supported-countries); [LS getting paid](https://docs.lemonsqueezy.com/help/getting-started/getting-paid); [fungies (2026)](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/); [dodopayments](https://dodopayments.com/blogs/lemon-squeezy-vs-stripe/)
- **Stripe Managed Payments:** Stripe's own MoR entered public preview in Feb 2026 at 5% + $0.50 and offers a migration path from Lemon Squeezy. Inference: it needs a Stripe account, so it isn't available to a Serbian entity. — [fungies (2026)](https://fungies.io/lemon-squeezy-stripe-acquisition-saas-founders-2026/); [dodopayments](https://dodopayments.com/blogs/lemonsqueezy-alternatives)
- **Creem:** Pays out to merchants in 86 countries, with local transfer fees of 7 EUR/USD or 1%, whichever is higher. Serbia unconfirmed (snippet truncated). — [Creem docs](https://docs.creem.io/merchant-of-record/supported-countries)
- **Dodo Payments:** MoR at 4% + 40c US domestic, +1.5% international, +0.5% subscriptions. Serbian eligibility not found. FastSpring uses quote-based pricing; Serbian eligibility not found. — [dodopayments](https://dodopayments.com/blogs/best-merchant-of-record-platforms)

### Inferences
- A Shopify app sidesteps this problem entirely: Shopify bills the merchant and pays the partner via PayPal or bank. That is a structural advantage for a Serbian developer.
- For an MCP/SaaS product, Polar is the lowest-friction confirmed option. Paddle is the most established (likely OK, verify). Keep a second MoR as a backup against account-review risk.

### Gaps
- Direct confirmation of Serbia for Paddle, Lemon Squeezy (bank), Creem, FastSpring and Dodo.
- Stripe's official country page could not be fetched.

## 5. Risks

### Takeaway
The main risks are: platforms absorbing features (OpenAI already reversed its commerce strategy once; Shopify, Anthropic and OpenAI ship first-party connectors), no in-platform monetization, low and unmeasurable discovery, low willingness to pay ($5–$50/month, high churn), and directory review requirements (OAuth 2.0, tool annotations, privacy policy, slow and uncertain approval).

### Cited Findings
- **Platform volatility:** OpenAI dropped in-chat Instant Checkout after about 6 months in favor of merchant apps. — [Digital Commerce 360](https://digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/)
- **First-party absorption:** Shopify ships official Storefront, Customer, Checkout and Catalog MCPs and puts merchants in ChatGPT by default. Software vendors are being pushed to ship official MCP servers, which displaces third-party wrappers. — [chattergo](https://www.chattergo.com/blog/shopify-mcp-ecosystem-deep-dive-developer-ai-platform); [mcpplaygroundonline](https://mcpplaygroundonline.com/blog/why-your-saas-needs-an-mcp-server)
- **Claude directory requirements:** must meet Anthropic security standards; every tool needs a title and readOnlyHint/destructiveHint; authenticated services must use OAuth 2.0 (no client-credentials M2M); local connectors need a privacy policy, and a missing one means immediate rejection. Reviewers test tool design, auth, privacy, external links, MCP App assets, docs and support. Compliance doesn't guarantee inclusion. — [Claude docs: submission](https://claude.com/docs/connectors/building/submission); [Claude docs: FAQ](https://claude.com/docs/connectors/faq); [sunpeak OAuth (May 2026)](https://sunpeak.ai/blogs/claude-connector-oauth-authentication/)
- **OAuth details:** supports DCR, CIMD or Anthropic-held credentials; requires Protected Resource Metadata (RFC 9728); callback is https://claude.ai/api/mcp/auth_callback. — [sunpeak](https://sunpeak.ai/blogs/claude-connector-oauth-authentication/); [Claude docs: authentication](https://claude.com/docs/connectors/building/authentication.md)
- **ChatGPT review friction:** reports of a tedious approval process, a buggy SDK, no usage data, and low adoption. — [Modern Retail](https://www.modernretail.co/technology/retailers-are-rushing-to-build-ai-apps-its-unclear-if-shoppers-will-use-them/)
- **Willingness to pay:** prices of $5–$50/month with real churn, fewer than 5% of servers monetized, and fair-use abuse risk. — [mcpize](https://mcpize.com/blog/make-money-with-mcp); [godberrystudios](https://godberrystudios.com/posts/how-to-monetize-mcp-servers-2026/)

### Inferences
- Comparison with a Shopify app: a Shopify app has proven merchant search intent, built-in billing (which solves the Serbia payments issue), and established indie benchmarks. An AI-assistant app today has no billing, opaque discovery and volatile platform rules. The pragmatic play is a Shopify app (or vertical SaaS) with an MCP/ChatGPT connector as a feature and an extra channel, not a standalone business.
- Pure "app that connects to Claude/ChatGPT" businesses look viable only when they own data or workflow, so that the connector is a front door to a paid product billed through Polar or Paddle.

### Gaps
- No data on how often third-party connectors were displaced by first-party ones.
- No published Claude directory rejection rates.
