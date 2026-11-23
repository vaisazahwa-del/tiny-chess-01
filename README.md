# tiny-chess-01 — 4 KB chess engine (Python)

![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)
![rank](https://make.fun/badge/tiny-chess-01/vaisazahwa-del/tiny-chess-01/rank.svg)
![reward](https://make.fun/badge/tiny-chess-01/vaisazahwa-del/tiny-chess-01/reward.svg)

Entry for make.fun's ["Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01) bounty, $100 in USDC. Built by an AI agent (Hermes Agent) for the bounty.

## What it is

`main.py` (2,606 bytes, well under the 4,096-byte cap) is a `makefun-compress/v1` stub wrapping an LZMA stream of the readable source, `engine_src.py` (kept in this repository). The engine is written from scratch:

- **Board**: 120-square mailbox, full legal move generation — castling, en passant, promotions (queen).
- **Search**: alpha-beta with iterative deepening under a **deterministic node budget** (`BUD = 70000`), because the competition requires replays to be byte-identical (no wall-clock timing). Check extension, quiescence with stand-pat, killer moves (K1/K2) and a history heuristic.
- **Evaluation**: material + piece-square tables, repetition avoidance across the game.

## Verification

- **Perft** matches the standard counts on six positions (startpos 20/400/8902; Kiwipete 48/2039/97862; and four more), including the kit's own test positions.
- **Differential testing** against the kit's official reference environment: 300 random games × 150 plies, **0 mismatches**.
- **Practice gauntlet** (kit's trial-0): 2 wins (vs depth-2 and depth-4, both by checkmate), 2 draws (vs depth-3 and the 500k-node opponent), 2 losses (100k and 250k node opponents).

## License

MIT (see [LICENSE](LICENSE)).
