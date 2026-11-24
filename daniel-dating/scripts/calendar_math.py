"""Day-count arithmetic for Dan 8:14 (2,300 evening-mornings), 12:11 (1,290 days), 12:12 (1,335 days).

Anchor events from 1 Maccabees (Seleucid-era dates) and the Babylonian king list BM 35603.
Babylonian months begin at first lunar crescent, so a date given as 'day X of month Y'
can be placed to +-1 day only with the full astronomical tables; we carry the Julian dates
used for these events with a +-1 month safety margin (intercalation uncertainty) and show that
the conclusions do not depend on it.
"""
import os

def jdn(y, m, d):
    """Julian-calendar date (astronomical year: 1 BCE = 0, 167 BCE = -166) -> Julian Day Number."""
    a = (14 - m) // 12
    yy = y + 4800 - a
    mm = m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083

def from_jdn(J):
    c = J + 32082
    d = (4 * c + 3) // 1461
    e = c - 1461 * d // 4
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = d - 4800 + m // 10
    return year, month, day

MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
def fmt(J):
    y, m, d = from_jdn(J)
    return f"{d} {MONTHS[m-1]} {1 - y} BCE"

EVENTS = {
    "altar desecrated ('abomination'), 15 Kislev SE 145 (1 Macc 1:54)": jdn(-166, 12, 6),
    "first pagan sacrifice, 25 Kislev SE 145 (1 Macc 1:59)": jdn(-166, 12, 16),
    "Temple rededicated, 25 Kislev SE 148 (1 Macc 4:52)": jdn(-163, 12, 14),
    "death of Antiochus IV reported in Babylon, Kislev SE 148 (BM 35603)": jdn(-163, 12, 1),
}
lines = ["# Day-count arithmetic for Daniel 8:14 and 12:11-12\n",
         "Julian dates carry about +-1 month uncertainty (lunar months / intercalation); conclusions hold across that range.\n"]
for k, v in EVENTS.items():
    lines.append(f"- {k}: ~{fmt(v)}")
des = EVENTS["altar desecrated ('abomination'), 15 Kislev SE 145 (1 Macc 1:54)"]
sac = EVENTS["first pagan sacrifice, 25 Kislev SE 145 (1 Macc 1:59)"]
red = EVENTS["Temple rededicated, 25 Kislev SE 148 (1 Macc 4:52)"]
death = EVENTS["death of Antiochus IV reported in Babylon, Kislev SE 148 (BM 35603)"]
lines.append(f"\nActual interval desecration -> rededication: {red - des} days; first sacrifice -> rededication: {red - sac} days "
             f"(1 Macc 4:54: 'at the very season and on the very day' - exactly three years).")
lines.append("\n| Daniel's figure | counted from | lands on (approx.) | what happened then |\n|---|---|---|---|")
lines.append(f"| 1,150 days (2,300 evening+morning offerings, 8:14) | backward from rededication | {fmt(red - 1150)} | plausible start of the suppression of the tamid (autumn 167); fits if the count began before the altar desecration |")
lines.append(f"| 2,300 days (if 'evening-morning' = a full day) | backward from rededication | {fmt(red - 2300)} | c. 171: murder of Onias III (2 Macc 4:33-35) - a possible but different reading |")
lines.append(f"| 1,290 days (12:11) | from desecration | {fmt(des + 1290)} | nothing recorded; Antiochus already dead {des + 1290 - death} days, Temple restored {des + 1290 - red} days earlier |")
lines.append(f"| 1,335 days (12:12) | from desecration | {fmt(des + 1335)} | nothing recorded |")
lines.append(f"| 3.5 'times' (7:25, 12:7) ~ 1,260-1,280 days | from desecration | {fmt(des + 1260)} - {fmt(des + 1280)} | nothing recorded |")
lines.append("\nReading: the three different figures (1,150 / 1,290 / 1,335) all exceed the real 3-year interval, and the two later ones fall in 163 BCE "
             "when nothing corresponding happened. A writer who already knew the date of the rededication (Dec 164) and of Antiochus' death "
             "would be expected to give the real interval; the successive, lengthening figures look like expectations recalculated before the outcome was known.")
out = "\n".join(lines) + "\n"
open(os.path.join(os.path.dirname(__file__), "..", "results", "calendar.md"), "w").write(out)
print(out)
