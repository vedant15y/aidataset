# AI Lab Practicals 1–5

The first five practicals extracted from `BSBXLB302P_AI_Lab_Practical_Report.docx`. Each practical has a Python program and a Markdown report containing its questions, explanation, code, and source sample outputs.

## Numbered practicals

1. **PYTHON FOR AI — SETUP AND BASICS** — [Program](01_python_for_ai_setup_and_basics.py) · [Report](01_python_for_ai_setup_and_basics.md)
2. **IMPLEMENTING BFS AND DFS** — [Program](02_bfs_and_dfs.py) · [Report](02_bfs_and_dfs.md)
3. **IMPLEMENTING A* SEARCH** — [Program](03_a_star_search.py) · [Report](03_a_star_search.md)
4. **SOLVING TIC-TAC-TOE USING MINIMAX** — [Program](04_tic_tac_toe_minimax.py) · [Report](04_tic_tac_toe_minimax.md)
5. **KNOWLEDGE REPRESENTATION USING PROLOG/PYTHON** — [Program](05_knowledge_representation.py) · [Report](05_knowledge_representation.md)

## Run the programs

Use Python 3 and install the libraries used by Practical 1:

```sh
python -m pip install -r requirements.txt
```

Run any numbered program, for example:

```sh
python 02_bfs_and_dfs.py
```

Practicals 2–5 use only Python's standard library. Practical 4 runs the report's simulated human-versus-AI game.

## Source notes

The Markdown reports preserve the source code and sample outputs. These outputs are examples from the document, not freshly verified execution logs; library versions, set ordering, and tied A* paths may differ.

In the runnable Practical 4 program, the human move list is corrected from `[4, 0, 2, 7]` to `[4, 2, 7]`, matching the source's displayed game trace and avoiding an occupied square. A move validation check is included. The report retains the original code.
