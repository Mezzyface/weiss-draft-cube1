# 🔴 Red — 50 (Toyo-model v2, FIRST PASS)

Light lean = **memory** (feed/check the memory zone, Resonate, recur-from-memory). Physical = **18 / 12 / 6 / 10 / 4 = 50**. Copy cap 4, Lv1 CX combo = 6.
Baked-in change per card: all traits + all name references universal; color → Red where needed. **Only 1 recolor** (Erio); rest native Red.
Built to match the role skeleton (soul-trigger Lv0 · consistency/memory Lv0s · one Lv1 CX combo ×6 + Lv1 counter event + body · synergy/removal Lv2 · CX + non-CX + early-play-heal Lv3 · 2-event row).

## Lv0 — 18 physical (6 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 4 | Meetup on Christmas Eve, Ai | [OSK/S121-E027](https://en.ws-tcg.com/cardlist/?cardno=OSK/S121-E027) | reverser — on-reverse re-reverse a low-level opponent (printed Red) |
| 4 | Anne: Miracle Fairy | [NIK/S117-E034](https://en.ws-tcg.com/cardlist/?cardno=NIK/S117-E034) | trigger-salvage — on climax trigger → salvage a character (printed Green → recolor Red) |
| 2 | Where Is the Self? Mafuyu Asahina | [PJS/S91-E090](https://en.ws-tcg.com/cardlist/?cardno=PJS/S91-E090) | **memory payoff** — from memory at CX phase → grab a climax (printed Blue → recolor Red) |
| 2 | Obligation of a Lycoris, Chisato | [LRC/WE47-E12](https://en.ws-tcg.com/cardlist/?cardno=LRC/WE47-E12) | **soul-trigger Lv0** — CIP search a Lv1-or-lower char (cost: WR char → bottom of clock) (native Red) |
| 3 | At the Secret Place, Kosaki | [NK/W30-E091](https://en.ws-tcg.com/cardlist/?cardno=NK/W30-E091) | **memory wall** — +2000 on opp turn vs few chars; memory recur (printed Blue → recolor Red) |
| 3 | Aiming For the Universe, Erio | [Gds/WS02-E064](https://en.ws-tcg.com/cardlist/?cardno=Gds/WS02-E064) | searcher/dig — CIP discard → dig (printed Green → recolor Red) |

## Lv1 — 12 physical (4 distinct)
| × | Card | id | Role |
|---|---|---|---|
| **6** | Unparalleled Beauty, Yotsuba Nakano | [5HY/W101-E024](https://en.ws-tcg.com/cardlist/?cardno=5HY/W101-E024) | **Lv1 CX combo (memory)** — dig X (scales w/ memory, up to 7) → grab a character (printed Green → recolor Red) |
| 2 | Getting Fired Up! Tsuruno | [MR/W80-E059](https://en.ws-tcg.com/cardlist/?cardno=MR/W80-E059) | memory-pay salvage on attack + on-reverse re-reverse a low opponent |
| 2 | A Dream Wished For, Ai | [OSK/S121-E035](https://en.ws-tcg.com/cardlist/?cardno=OSK/S121-E035) | +4000 attacker; on-reverse self→memory + dig/grab |
| 2 | Bond of the Student Council, Kaguya & Chika & Miko | [KGL/S95-PE07](https://en.ws-tcg.com/cardlist/?cardno=KGL/S95-PE07) | memory engine — CIP load a card into memory; ACT salvage |

## Lv2 — 6 physical (3 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 2 | To The Skies, Carl Fredricksen | [PXR/S94-E093](https://en.ws-tcg.com/cardlist/?cardno=PXR/S94-E093) | Assist +2000; ACT Memory → conditional direct attack (printed Blue → recolor Red) |
| 2 | Staying Together Overnight, Mai Sakurajima | [SBY/W114-E053](https://en.ws-tcg.com/cardlist/?cardno=SBY/W114-E053) | Assist +lvl×500; CIP stock-ramp; memory scry-on-trigger + pump |
| 2 | Towards the Future Together, Shishiro Botan | [HOL/W91-E121](https://en.ws-tcg.com/cardlist/?cardno=HOL/W91-E121) | memory beater — 3+ diff names in memory → +2500 + attack opp back row (printed Blue → recolor Red) |

## Lv3 — 10 physical (3 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 4 | The Year I Spent With You, Mai Sakurajima | [SBY/W114-E049](https://en.ws-tcg.com/cardlist/?cardno=SBY/W114-E049) | **Lv3 CX combo (memory)** — CIP heal; combo: deck-destruction burn ×X (X scales w/ memory) |
| 3 | The Start of Youth, Erio | [Gds/WS02-E049](https://en.ws-tcg.com/cardlist/?cardno=Gds/WS02-E049) | **non-CX memory finisher** — P11000; on-reverse → opp clock (removal); dies to memory, replays from memory (printed Green → recolor Red) |
| 3 | Deciding Each Member's Color, Ruby | [OSK/S107-E043](https://en.ws-tcg.com/cardlist/?cardno=OSK/S107-E043) | **early-play (memory)** — −1 lvl w/ 3+ diff names in memory; CIP soft-heal from clock; on-reverse self-bounce |

## Events — 4 physical (2 distinct)
| × | Card | id | Role |
|---|---|---|---|
| 2 | Birthday Present | [SFN/S108-E065a](https://en.ws-tcg.com/cardlist/?cardno=SFN/S108-E065a) | **memory salvage** — mill 2 → salvage a char by level; self → memory + recur on level-up |
| 2 | Degtyaryov Anti-Tank Rifle | [GGO/S59-E030](https://en.ws-tcg.com/cardlist/?cardno=GGO/S59-E030) | **scaling memory burn** — scry opp; self → memory; deal X = copies of this in memory (printed Green → recolor Red) |

## Status
- [x] Red 50 locked (memory engine) — all picks reviewed
- [x] Committed to cube.db (build_cube.py Red block)
- [ ] Last color: Green (stock lean)
