# ILPs used to prove necessary and sufficient conditions for 2-anionic-resonance in fullerenes

## Background

### Definitions

A **fullerene** $F_n$ is a 3-regular graph such that every face is a pentagon
or a hexagon. By Euler's formula, there are exactly 12 pentagons. A fullerene
is said to be **k-resonant** if the deletion of the vertices of any $k$
independent hexagons results in a graph that admits a perfect
matching. This definition is inspired by the **Clar number** of a fullerene.
The **anionic Clar number** is a recent generalization of the Clar number to
anionic systems. In this generalization, pentagons compete with hexagons to
form Clar sextets. Given this generalization, we say that a fullerene is
**k-anionic-resonant** if the deletion of the vertices of any $k$ independent
pentagons results in a graph that admits a perfect matching.

### Necessary and sufficient conditions for 2-anionic-resonace

My PhD thesis (Chapter 4) establishes necessary and sufficient conditions for a
fullerene to be 2-anionic-resonant (Theorem 4.4). This proof relies on the
outputs from two Integer Linear Programs. The first one, used to prove
Lemma 4.26, corresponds with `ilp_1` in `src/ilp.py`. The second one, used to
complete the proof of Theorem 4.4, corresponds with `ilp_2` in `src/ilp.py`.

## Code

### Requirements:

1. Python version >= 3.12 (version it was tested on).

2. Python PuLP library (https://pypi.org/project/PuLP/) version >= 2.8 (version
   it was tested on).

3. The code uses the following three solvers: `SCIP`, `GUROBI`, and `PULP_CBC`.
   The PuLP library ships with `PULP_CBC`. If you want to run it with `SCIP` or
`GUROBI`, you should download them from (https://www.scipopt.org/) and
(https://www.gurobi.com/), respectively. The latter requires a licence. Please
comment out the appropriate lines of code in `src/ilp.py` to only use solvers
available on your machine (this will be stated upon running the script if you
are unsure).

### To run:

```
python src/ilp.py
```

### Output:

The first command line output is the available solvers on your machine. Again,
comment out the code in `src/ilp.py` corresponding to solvers you do not have
downloaded. The subsequent output is the optimal solutions: 33 to `ilp_1`
(Lemma 4.26) per solver and the lack of a feasible integer solution to
`ilp_2` (Theorem 4.4).

Output from my machine:

```
Available solvers on build: ['GUROBI_CMD', 'MOSEK', 'PULP_CBC_CMD', 'COIN_CMD', 'SCIP_CMD']

Proof of Lemma 4.33

SCIP: Optimal solution found. Objective value: 33.0
Gurobi: Optimal solution found. Objective value: 33.0
COIN_CMD: Optimal solution found. Objective value: 33.0

Proof of Theorem 4.35

SCIP: Infeasible
Gurobi: Not Solved
COIN_CMD: Infeasible
```

Log files for each solver used  and LP files for `ilp_1` and `ilp_2` are written
to `output`.

## Citation
If you use this code in your research, please cite it via:

```
@software{Slobodin_ILPs_to_prove_2025,
  author = {Slobodin, A.},
  month = Jan,
  title = {{ILPs to prove necessary and sufficient conditions for 2-anionic-resonance in fullerenes}},
  url = {https://github.com/fastbodin/2_resonant_fullerene_proof_ilps},
  version = {1.0.0},
  year = {2025}
}
```
