#!/usr/bin/env python3
"""Build cube.db (Toyo-model v2). Entry: (cardno, cube_color, section, role, count, notes).
Baked-in change per card: all traits + all name references universal; color reassigned to balance.
Template per color: Lv0 18 / Lv1 12 / Lv2 6 / Lv3 10 / Event 4 = 50."""
import sqlite3
from pathlib import Path

SRC = Path(__file__).with_name("cards.db")
OUT = Path(__file__).with_name("cube.db")
UNI = "all traits + all name references universal"
COLORS = ["Yellow", "Blue", "Red", "Green"]

# JP-only cards (not in EN cards.db): cardno -> (name, printed_color, level, cost, power, soul, trigger, ability, image_url)
JPIMG = "https://ws-tcg.com/wordpress/wp-content/images/cardlist/"
JP_EXTRA = {
    "YRC/W116-001": ("Walking at the Campground, Ena & Hanpen & Chikuwa", "Green", "0", "0", "1000", "1", "-",
        "CIP discard 1 -> salvage a char (lvl<=revealed) + place top card as a marker under a Tent-named char.",
        JPIMG + "y/yrc_w116/yrc_w116_001.png"),
    "YRC/W116-041": ("Memo Memo, Nadeshiko", "Red", "0", "0", "1500", "1", "-",
        "ACT [(1) place this in WR]: look top 4, grab a char to hand + place 1 as a marker under a Tent-named char.",
        JPIMG + "y/yrc_w116/yrc_w116_041.png"),
    "YRC/W116-076": ("Tent at the Ooigawa", "Blue", "0", "0", "1500", "1", "-",
        "Untargetable. Markers under it scale: 1+ anthem +500; 2+ on-CX-trigger bounce; 3+ Assist +1000; self->WR if 5+ total markers.",
        JPIMG + "y/yrc_w116/yrc_w116_076.png"),
}

CUBE = [
    ("SIL/W109-E037", "Generic", "Generic core", "Brainstorm-salvage", 4, "GIVEN, choice of color"),
    ("BTR/W107-E048", "Generic", "Generic core", "Drop Search",        4, "GIVEN, choice of color"),
    # YELLOW 50 -- lean: events / direct effects
    ("GBS/S63-E037",  "Yellow", "Lv0", "Salvage (discard CX or event)",              2, UNI),
    ("Foy/W120-E007", "Yellow", "Lv0", "Salvage + on-death dig",                     3, UNI),
    ("OSK/S121-E001", "Yellow", "Lv0", "Beater + on-reverse salvage",                4, UNI),
    ("KMD/W96-E018",  "Yellow", "Lv0", "Soul on direct-attack + self-bounce",        3, UNI),
    ("Fsa/W120-E009", "Yellow", "Lv0", "Beater + on-death CX dig",                   4, UNI),
    ("NIK/S117-TE02", "Yellow", "Lv0", "SOUL-TRIGGER Lv0 + CIP salvage",             2, UNI),
    ("OSK/S107-E067", "Yellow", "Lv1", "Lv1 CX COMBO - dig4 grab event-or-char",     6, UNI),
    ("GBS/S63-TE08",  "Yellow", "Lv1", "Lv1 event - COUNTER dig4 grab char",         4, UNI),
    ("SFN/S108-E066", "Yellow", "Lv1", "Lv1 event - COUNTER draw/discard + salvage", 2, UNI),
    ("SFN/S108-E018", "Yellow", "Lv2", "Event-synergy beater + CX disruption",       3, UNI),
    ("LRC/WE47-E09",  "Yellow", "Lv2", "Removal - CIP bounce opp char",              1, UNI),
    ("BD/W125-E063S", "Yellow", "Lv2", "Lv2 event - stock-reset disruption",         2, UNI),
    ("KC/S25-E002",   "Yellow", "Lv3", "Non-CX burn finisher (on-cancel)",           4, UNI),
    ("Fsh/W120-E079", "Yellow", "Lv3", "CX finisher + event synergy",                3, UNI),
    ("SPY/S106-E030", "Yellow", "Lv3", "Early-play heal + modal refund",             3, UNI),
    ("FGO/S75-E020",  "Yellow", "Event", "Burn - mill4 dmg per lv1+ card",           2, UNI),
    ("PXR/S94-E023",  "Yellow", "Event", "Modal toolbox",                            2, UNI),
    # BLUE 50 -- lean: markers / tempo
    ("MRd/S111-TE01", "Blue", "Lv0", "SOUL-TRIGGER Lv0 / anthem + salvage", 2, UNI),
    ("NIK/S117-E105", "Blue", "Lv0", "Marker beater (+1500/marker)",        4, UNI),
    ("EIS/SX07-039",  "Blue", "Lv0", "Marker self-fueler (+2000 w/ marker)",4, UNI),
    ("YRC/W116-001",  "Blue", "Lv0", "Salvage + Tent-marker (JP)",          3, UNI),
    ("YRC/W116-041",  "Blue", "Lv0", "Marker placer (JP)",                  3, UNI),
    ("YRC/W116-076",  "Blue", "Lv0", "Marker PAYOFF (JP)",                  2, UNI),
    ("5HY/W101-E078", "Blue", "Lv1", "Lv1 CX COMBO (marker)",               6, UNI),
    ("LL/EN-W01-030", "Blue", "Lv1", "No-CX marker body (+1000/marker)",    2, UNI),
    ("TSK/S70-E078",  "Blue", "Lv1", "No-CX marker toolbox",                2, UNI),
    ("KMD/W96-E097",  "Blue", "Lv1", "Lv1 event (marker) - grab + marker",  2, UNI),
    ("Gtd/WS02-E020S","Blue", "Lv2", "Marker engine - Assist + pay-with-markers", 2, UNI),
    ("SBY/W114-E072", "Blue", "Lv2", "Marker payoff - Assist + CX-phase burn", 2, UNI),
    ("KMD/W96-E020",  "Blue", "Lv2", "Marker -> soul burst + CX dig",         2, UNI),
    ("MOB/SX02-001",  "Blue", "Lv3", "Lv3 CX combo - burn = markers on chosen char", 4, UNI),
    ("DG/EN-S03-E054","Blue", "Lv3", "Non-CX marker finisher (+1500/marker, Great Performance)", 3, UNI),
    ("RZ/S46-E060",   "Blue", "Lv3", "Early-play heal + marker payoff (+1000/marker)", 3, UNI),
    ("AOT/S50-E098",  "Blue", "Event", "COUNTER filter - dig3 bin3",          2, UNI),
    ("TSK/S82-E025",  "Blue", "Event", "COUNTER - cannot become REVERSE (save)", 2, UNI),
    # RED 50 -- lean: memory
    ("OSK/S121-E027", "Red", "Lv0", "Reverser - re-reverse low-lvl opp",     4, UNI),
    ("NIK/S117-E034", "Red", "Lv0", "Trigger-salvage",                       4, UNI),
    ("PJS/S91-E090",  "Red", "Lv0", "Memory payoff - grab climax from memory",2, UNI),
    ("LRC/WE47-E12",  "Red", "Lv0", "SOUL-TRIGGER Lv0 + CIP search (clock cost)", 2, UNI),
    ("NK/W30-E091",   "Red", "Lv0", "Memory wall + recur",                   3, UNI),
    ("Gds/WS02-E064", "Red", "Lv0", "Searcher/dig",                          3, UNI),
    ("5HY/W101-E024", "Red", "Lv1", "Lv1 CX COMBO (memory) - dig X grab char",6, UNI),
    ("MR/W80-E059",   "Red", "Lv1", "Memory-pay salvage + reverser",         2, UNI),
    ("OSK/S121-E035", "Red", "Lv1", "Attacker; on-reverse self->memory + dig",2, UNI),
    ("KGL/S95-PE07",  "Red", "Lv1", "Memory engine - load memory + salvage", 2, UNI),
    ("PXR/S94-E093",  "Red", "Lv2", "Assist + ACT memory direct-attack",     2, UNI),
    ("SBY/W114-E053", "Red", "Lv2", "Assist; stock-ramp; memory scry",       2, UNI),
    ("HOL/W91-E121",  "Red", "Lv2", "Memory beater - attack opp back row",   2, UNI),
    ("SBY/W114-E049", "Red", "Lv3", "Lv3 CX COMBO (memory) - heal + deck-burn",4, UNI),
    ("Gds/WS02-E049", "Red", "Lv3", "Non-CX memory finisher - on-reverse->clock",3, UNI),
    ("OSK/S107-E043", "Red", "Lv3", "Early-play (memory) - soft-heal + self-bounce",3, UNI),
    ("SFN/S108-E065a","Red", "Event", "Memory salvage - mill2 + self->memory recur",2, UNI),
    ("GGO/S59-E030",  "Red", "Event", "Scaling memory burn - X = copies in memory",2, UNI),
    # GREEN 50 -- lean: stock / ramp
    ("DDD/S118-E025", "Green", "Lv0", "SOUL-TRIGGER Lv0 + self-recur",                2, UNI),
    ("BAV/W112-TE14", "Green", "Lv0", "Ramp - hand->stock + double-trigger",          4, UNI),
    ("GBS/S63-E060",  "Green", "Lv0", "Assist + stock-gain on refresh",               2, UNI),
    ("OSK/S121-E054", "Green", "Lv0", "CIP discard -> tutor/recur a char",            3, UNI),
    ("LRC/WE47-E15",  "Green", "Lv0", "Ramp - top->stock + tempo removal",            3, UNI),
    ("NIK/S117-TE14", "Green", "Lv0", "Clock-scaling beater + stock->clock dig 6",    4, UNI),
    ("NGL/S58-E028",  "Green", "Lv1", "Lv1 CX COMBO (stock) - ramp + reveal-grab",    6, UNI),
    ("DDM/S88-E020",  "Green", "Lv1", "Disruption - push opp into their stock + soul",3, UNI),
    ("LRC/WE47-E43",  "Green", "Lv1", "Experience reveal -> stock (ramp)",            3, UNI),
    ("LRC/WE47-E44",  "Green", "Lv2", "+10000 on turn; markers->stock on cancel",     2, UNI),
    ("AZL/S119-E038", "Green", "Lv2", "Refresh engine + ACT ramp 2 -> stock",         2, UNI),
    ("DDD/S118-E104", "Green", "Lv2", "Splashable; opp stock-shuffle disruption",     2, UNI),
    ("GCR/SE48-E42",  "Green", "Lv3", "Lv3 CX COMBO (stock payoff) - hand+stock->burn",4, UNI),
    ("GCR/SE48-E41",  "Green", "Lv3", "Non-CX finisher - search to hand+stock / clock",3, UNI),
    ("LRC/WE47-E49",  "Green", "Lv3", "Early-play (-1 lvl) - clock->stock + ramp",     3, UNI),
    ("P5/S45-E022",   "Green", "Event", "L1 toolbox - search / ramp->stock / +1 soul",2, UNI),
    ("OSK/S107-E029", "Green", "Event", "L3 modal - search CX / ramp->stock / pay-4 burn",2, UNI),
]

def main():
    src = sqlite3.connect(SRC); out = sqlite3.connect(OUT)
    out.execute("DROP TABLE IF EXISTS cube")
    out.execute("CREATE TABLE cube (cardno TEXT PRIMARY KEY, name TEXT, cube_color TEXT, "
        "printed_color TEXT, section TEXT, availability TEXT, bundle_count INTEGER, role TEXT, "
        "level TEXT, cost TEXT, power TEXT, soul TEXT, trigger TEXT, ability TEXT, relabel_notes TEXT, image_url TEXT)")
    for cardno, cube_color, section, role, count, notes in CUBE:
        row = src.execute("SELECT name,color,level,cost,power,soul,trigger,ability,image_url "
            "FROM cards WHERE cardno=?", (cardno,)).fetchone()
        if not row:
            if cardno in JP_EXTRA:
                row = JP_EXTRA[cardno]
            else:
                print("!! not found:", cardno); continue
        name, pcolor, lv, cost, pw, soul, trig, ab, img = row
        avail = "given" if section == "Generic core" else "drafted"
        targets = COLORS if cube_color == "Generic" else [cube_color]
        for col in targets:
            key = cardno + " [" + col[0] + "]" if cube_color == "Generic" else cardno
            out.execute("INSERT INTO cube VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (key, name, col, pcolor, section, avail, count, role, lv, cost, pw, soul, trig, ab, notes, img))
    out.commit()
    print("cube.db built:", out.execute("SELECT COUNT(*) FROM cube").fetchone()[0], "distinct entries")
    print("physical by color (drafted):")
    for c,k in out.execute("SELECT cube_color,SUM(bundle_count) FROM cube WHERE availability='drafted' GROUP BY cube_color ORDER BY cube_color"): print("  ",c,k)
    for color in ("Yellow","Blue","Red","Green"):
        print(color, "by section:")
        for s,k in out.execute("SELECT section,SUM(bundle_count) FROM cube WHERE cube_color=? GROUP BY section",(color,)): print("   ",s,k)
    print("recolored:")
    for r in out.execute("SELECT name,printed_color,cube_color FROM cube WHERE cube_color!=printed_color AND cube_color NOT IN ('Generic','All')"): print("  ",r[0],"(",r[1],"->",r[2],")")
    out.close(); src.close()

if __name__ == "__main__":
    main()
