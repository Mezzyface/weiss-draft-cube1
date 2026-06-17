# 🔵 Blue — 50 (Toyo-model v2, FIRST PASS — mirrors Yellow's skeleton)

Light lean = **markers / tempo**. Physical = **18 / 12 / 6 / 10 / 4 = 50**. Copy cap 4, Lv1 CX combo = 6.
Baked-in change per card: all traits + all name references universal; color → Blue where needed.
Built to match the role skeleton you converged on for Yellow (soul-trigger Lv0 · consistency Lv0s · one Lv1 CX combo ×6 + Lv1 counter events · synergy/removal Lv2 · non-CX + CX + early-play-heal Lv3 · 2-event row). **3 recolors** (Scrooge, Beachside Kanna, Ena — rest native Blue). *Ena (YRC/W116-001) is a JP-only card not in cards.db → needs manual details when committing.*

## Lv0 — 18 physical (6 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 2 | "Mirrorverse" Scrooge McDuck | [MRd/S111-TE01](https://en.ws-tcg.com/cardlist/?cardno=MRd/S111-TE01) | **soul-trigger Lv0** — anthem +500 + salvage (printed Yellow → recolor Blue) |
| 4 | "SAFE 50-50" Epinel | [NIK/S117-E105](https://en.ws-tcg.com/cardlist/?cardno=NIK/S117-E105) | marker beater (+1500/marker; on-reverse self-marker) |
| 4 | Sought-After Girl, Alexia Midgar | [EIS/SX07-039](https://en.ws-tcg.com/cardlist/?cardno=EIS/SX07-039) | marker self-fueler (+2000 w/ marker; CIP self-marker; bounce on damage-cancel) (printed Red → recolor Blue) |
| 3 | Walking at the Campground, Ena & Hanpen & Chikuwa | [YRC/W116-001](https://ws-tcg.com/cardlist/?cardno=YRC/W116-001) | **JP-only** (Yuru Camp△ S3) — CIP discard 1 → salvage a char + Tent-marker place (printed Green → recolor Blue) |
| 3 | Memo Memo, Nadeshiko | [YRC/W116-041](https://ws-tcg.com/cardlist/?cardno=YRC/W116-041) | **JP-only** (U) — ACT dig 4 → grab a char + place a Tent-marker (marker placer) (printed Red → recolor Blue) |
| 2 | Tent at the Ooigawa | [YRC/W116-076](https://ws-tcg.com/cardlist/?cardno=YRC/W116-076) | **JP-only (native Blue, U)** — marker PAYOFF: untargetable; 1+ marker = anthem +500, 2+ = on-CX-trigger bounce, 3+ = Assist +1000; self→WR if 5+ total markers |

## Lv1 — 12 physical (4 distinct)
| × | Card | id | Role |
|---|---|---|---|
| **6** | Unparalleled Beauty, Miku Nakano | [5HY/W101-E078](https://en.ws-tcg.com/cardlist/?cardno=5HY/W101-E078) | **Lv1 CX combo (marker)** — P4000; CIP place a marker; CX combo salvage a char ≤ total markers on board; +3000 if marker under it |
| 2 | "Nico Is Popular" Nico | [LL/EN-W01-030](https://en.ws-tcg.com/cardlist/?cardno=LL/EN-W01-030) | **no-CX marker body** — P6000; +1000/marker; on-reverse self-marker; ACT +1 soul (printed Yellow → recolor Blue) |
| 2 | Creating Potions! Rimuru | [TSK/S70-E078](https://en.ws-tcg.com/cardlist/?cardno=TSK/S70-E078) | **no-CX marker toolbox** — ACT heal / place a marker / turn a marker into stock (native Blue) |
| 2 | Unlimited Appetite | [KMD/W96-E097](https://en.ws-tcg.com/cardlist/?cardno=KMD/W96-E097) | **Lv1 event (marker)** — cost-0: reveal top → grab a character + may place this as a marker under any char (native Blue) |

## Lv2 — 6 physical (3 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 2 | United Front, Ryuji and Taiga | [Gtd/WS02-E020S](https://en.ws-tcg.com/cardlist/?cardno=Gtd/WS02-E020S) | marker engine — Assist +lvl×500; ACT pump + self-marker; pay costs with markers (printed Yellow → recolor Blue) |
| 2 | Blessing of the Marriage License, Sakuta Azusagawa | [SBY/W114-E072](https://en.ws-tcg.com/cardlist/?cardno=SBY/W114-E072) | marker payoff — Assist +2000; CX-phase 3+ markers → dump + burn 1; self-marker on damage-cancel (printed Red → recolor Blue) |
| 2 | Wings of Love, Tohru | [KMD/W96-E020](https://en.ws-tcg.com/cardlist/?cardno=KMD/W96-E020) | marker→soul burst (other char attacks → +1000/+X soul = markers); CX combo dig 3 + self-marker (printed Yellow → recolor Blue) |

## Lv3 — 10 physical (3 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 4 | Arataka Reigen | [MOB/SX02-001](https://en.ws-tcg.com/cardlist/?cardno=MOB/SX02-001) | **Lv3 CX combo (marker)** — P9000; combo deals damage = markers under a chosen char; +1500/back-row char (printed Yellow → recolor Blue) |
| 3 | Pringer X | [DG/EN-S03-E054](https://en.ws-tcg.com/cardlist/?cardno=DG/EN-S03-E054) | **non-CX marker finisher** — P10000, +1500/marker; Great Performance (forces opp to attack it); ACT marker-feed +1 soul (printed Green → recolor Blue) |
| 3 | Blue-Haired Maid, Rem | [RZ/S46-E060](https://en.ws-tcg.com/cardlist/?cardno=RZ/S46-E060) | **early-play heal + marker payoff** (−1 lvl in hand; +1000/marker; CIP heal; on-reverse self-marker) |

## Events — 4 physical (2 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 2 | In the Wall | [AOT/S50-E098](https://en.ws-tcg.com/cardlist/?cardno=AOT/S50-E098) | event — 【COUNTER】 dig 3 → bin up to 3 (filter / self-mill / feeds WR salvage) |
| 2 | Sleep Mode | [TSK/S82-E025](https://en.ws-tcg.com/cardlist/?cardno=TSK/S82-E025) | L1 event — 【COUNTER】 give a char **"cannot become 【REVERSE】"** (combat save) (printed Yellow → recolor Blue) |

## Notes
- **Marker engine:** Zeta / Epinel / Ako place markers at Lv0; Assassin of Black (Lv2) and Batmobile (Lv3) cash them in. Markers are self-contained so the theme works under universal traits.
- **CX pool:** any climax fires Kirito's combo (universal names); a standard 8-trigger spread covers it. Furious Fist wants a 【SOUL】/door climax for its clock-kick.
- **Soul-trigger Lv0** = Scrooge ✅. Mirrors Yellow's structure throughout.
- **vs. Yellow balance:** Blue is more proactive (marker beaters) and less counter-heavy than Yellow — good contrast.

## Status
- [x] Blue 50 locked (18 distinct) — marker/tempo engine
- [x] Committed to cube.db (build_cube.py, with JP cards handled via JP_EXTRA)
- [ ] Next colors: Red, Green
