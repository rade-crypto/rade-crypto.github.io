// Renders TikTok/Reels slideshow stills (1080x1920) for the IRON90 app.
// Usage: node content/generator/render.mjs (uses the globally installed playwright)
import { createRequire } from 'module';
import { execSync } from 'child_process';
const require = createRequire(import.meta.url);
const { chromium } = require(execSync('npm root -g').toString().trim() + '/playwright');
import { mkdirSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const OUT = join(dirname(fileURLToPath(import.meta.url)), '..', 'stills');
mkdirSync(OUT, { recursive: true });

const BG = {
  steel: 'radial-gradient(120% 80% at 50% 0%, #2a2f36 0%, #0d0f12 60%, #050506 100%)',
  red: 'radial-gradient(110% 70% at 50% 100%, #4a0f12 0%, #140607 55%, #050505 100%)',
  night: 'radial-gradient(100% 60% at 50% 30%, #12203a 0%, #070a12 60%, #030304 100%)',
};

const base = (bg, body) => `<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;background:${bg};font-family:'Inter','Noto Color Emoji',sans-serif;color:#fff;overflow:hidden;position:relative}
body::after{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.015) 0 2px,transparent 2px 4px);pointer-events:none}
.safe{position:absolute;top:260px;left:90px;right:150px;bottom:420px;display:flex;flex-direction:column;justify-content:center;gap:48px}
.big{font-size:92px;font-weight:900;line-height:1.08;letter-spacing:-2px;text-shadow:0 6px 30px rgba(0,0,0,.8)}
.mid{font-size:64px;font-weight:800;line-height:1.15;text-shadow:0 4px 20px rgba(0,0,0,.8)}
.small{font-size:44px;font-weight:600;color:#b9c0c9;line-height:1.3}
.accent{color:#ff3b3b}
.tag{display:inline-block;font-size:34px;font-weight:800;letter-spacing:6px;color:#ff3b3b;border:3px solid #ff3b3b;padding:10px 22px;border-radius:12px;align-self:flex-start}
.card{background:rgba(20,22,26,.92);border:2px solid #2c3138;border-radius:36px;padding:48px;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.row{display:flex;align-items:center;gap:28px;font-size:50px;font-weight:700;padding:22px 0;border-bottom:2px solid #23272d}
.row:last-child{border-bottom:none}
.check{width:64px;height:64px;border-radius:18px;background:#1fbf5b;display:flex;align-items:center;justify-content:center;font-size:42px;flex:none}
.x{background:#3a1416;border:3px solid #ff3b3b}
.chat{display:flex;flex-direction:column;gap:28px}
.hdr{display:flex;align-items:center;gap:22px;font-size:40px;font-weight:800;padding-bottom:26px;border-bottom:2px solid #23272d}
.ava{width:84px;height:84px;border-radius:50%;background:linear-gradient(135deg,#ff3b3b,#7a0d10);display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900}
.sub{font-size:30px;color:#7f8893;font-weight:600}
.me{align-self:flex-end;background:#2f6bff;border-radius:40px 40px 10px 40px;padding:30px 38px;font-size:44px;font-weight:600;max-width:85%;line-height:1.3}
.bot{align-self:flex-start;background:#23262c;border-radius:40px 40px 40px 10px;padding:30px 38px;font-size:44px;font-weight:600;max-width:92%;line-height:1.35}
.bar{height:44px;border-radius:22px;background:#23272d;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,#ff3b3b,#ff8a3b)}
.btn{align-self:center;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#ff5a5a,#b30d12 70%);display:flex;align-items:center;justify-content:center;text-align:center;font-size:64px;font-weight:900;box-shadow:0 0 0 30px rgba(255,59,59,.12),0 0 0 70px rgba(255,59,59,.06),0 40px 100px rgba(0,0,0,.7)}
table{width:100%;border-collapse:collapse;font-size:44px;font-weight:700}
td{padding:26px 10px;border-bottom:2px solid #23272d}
td:nth-child(2){color:#7f8893;text-align:center}
td:nth-child(3){color:#1fbf5b;text-align:right}
th{font-size:32px;color:#7f8893;letter-spacing:4px;padding-bottom:20px;text-align:center}
th:first-child{text-align:left}th:last-child{text-align:right}
.mark{position:absolute;bottom:330px;left:90px;font-size:32px;font-weight:900;letter-spacing:8px;color:rgba(255,255,255,.35)}
</style></head><body><div class="safe">${body}</div></body></html>`;

const slides = {
  // Video 1 — "The coach roasted me"
  'v1_roast_1': base(BG.steel, `<div class="big">I told my AI coach I skipped the gym because I was <span class="accent">tired</span> 💀</div>`),
  'v1_roast_2': base(BG.steel, `<div class="card chat">
    <div class="hdr"><div class="ava">C</div><div>Coach<div class="sub">Day 24 of 90 · Rank: Iron</div></div></div>
    <div class="me">skipped today, was too tired</div>
    <div class="bot">Tired. You had enough energy for 3 hours of YouTube.</div>
    <div class="bot">Tomorrow 7:00am. Send proof or you drop a rank. Your call.</div></div>`),
  'v1_roast_3': base(BG.red, `<div class="tag">DAY 24 / 90</div><div class="big">Not skipping again.</div><div class="small">this app has no mercy</div>`),

  // Video 2 — "Day X of 90"
  'v2_day_1': base(BG.night, `<div class="tag">DAY 47 / 90</div><div class="big">of becoming a <span class="accent">different man</span></div>`),
  'v2_day_2': base(BG.night, `<div class="card">
    <div class="row"><div class="check">✓</div>Gym — proof sent</div>
    <div class="row"><div class="check">✓</div>160g protein</div>
    <div class="row"><div class="check">✓</div>Cold shower</div>
    <div class="row"><div class="check">✓</div>No porn · 47 day streak</div>
    <div class="row"><div class="check">✓</div>Read 10 pages</div>
    <div class="row"><div class="check">✓</div>In bed by 11</div></div>`),
  'v2_day_3': base(BG.night, `<div class="mid">Rank: Iron → <span class="accent">Steel</span></div>
    <div class="bar"><div class="fill" style="width:57%"></div></div><div class="small">13 days left. Miss one and I drop back.</div>`),

  // Video 3 — "Rules I locked for 90 days"
  'v3_rules_1': base(BG.red, `<div class="big">I locked these rules for <span class="accent">90 days</span>.</div><div class="mid">Break one and I lose everything.</div>`),
  'v3_rules_2': base(BG.steel, `<div class="tag">RULE 1</div><div class="big">No porn.</div><div class="small">Not "less". None.</div>`),
  'v3_rules_3': base(BG.steel, `<div class="tag">RULE 2</div><div class="big">Gym 6x a week.</div><div class="small">Proof photo or it didn't happen.</div>`),
  'v3_rules_4': base(BG.steel, `<div class="tag">RULE 3</div><div class="big">No phone the first hour.</div>`),
  'v3_rules_5': base(BG.steel, `<div class="tag">RULE 4</div><div class="big">In bed by 11.</div>`),
  'v3_rules_6': base(BG.red, `<div class="big">Day 1 starts tomorrow.</div><div class="mid accent">Who's in?</div>`),

  // Video 4 — "The urge button"
  'v4_urge_1': base(BG.night, `<div class="mid">11:48pm. About to relapse.<br>So I pressed this.</div><div class="btn">I'M ABOUT<br>TO SLIP</div>`),
  'v4_urge_2': base(BG.night, `<div class="card chat">
    <div class="hdr"><div class="ava">C</div><div>Coach<div class="sub">Day 31 · urge mode</div></div></div>
    <div class="bot">Phone goes in another room. Now.</div>
    <div class="bot">20 pushups. Then come back and tell me you did them.</div>
    <div class="bot">You're 31 days in. Don't trade that for 5 minutes.</div></div><div class="mid">it worked.</div>`),

  // Video 5 — "Day 1 vs Day 90"
  'v5_results_1': base(BG.steel, `<div class="big">What 90 days of discipline did to me</div>`),
  'v5_results_2': base(BG.steel, `<div class="card"><table>
    <tr><th></th><th>DAY 1</th><th>DAY 90</th></tr>
    <tr><td>Gym sessions</td><td>0</td><td>74</td></tr>
    <tr><td>Porn streak</td><td>0</td><td>90 days</td></tr>
    <tr><td>Wake up</td><td>11:00</td><td>6:30</td></tr>
    <tr><td>Books read</td><td>0</td><td>6</td></tr>
    <tr><td>Screen time</td><td>9h</td><td>2h</td></tr></table></div><div class="small">Rules locked. Coach on. No excuses.</div>`),
};

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => chromium.launch());
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
for (const [name, html] of Object.entries(slides)) {
  await page.setContent(html, { waitUntil: 'load' });
  await page.screenshot({ path: join(OUT, `${name}.png`) });
  console.log('rendered', name);
}
await browser.close();
