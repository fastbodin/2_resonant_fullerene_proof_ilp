from pulp import *

def h(i):
    return (i-1) % 7

def j(i):
    return (i+1) % 7

def sum_all(var_type):
    return sum(var_type[i] for i in range(7))

def add_cons_type_14(ilp, vars):
    ilp += (0 == sum_all(vars['y00105']) + sum_all(vars['y00104']))

def add_cons_type_13(ilp, vars):
    ilp += (3*vars['N'] - vars['s'] + 7 ==
            20 + 2*vars['s']+
            4*vars['y22020'] + 4*vars['y20120'] +
            4*vars['y02120'] + 3*vars['y00330'] +
            2*sum_all(vars['y20003']) +
            2*sum_all(vars['y02003']) +
            2*sum_all(vars['y20004']) +
            2*sum_all(vars['y02004']) +
            2*sum_all(vars['y00105']) +
            2*sum_all(vars['y00104']) +
            4*sum_all(vars['y00212']) +
            4*sum_all(vars['y00213']) +
            4*sum_all(vars['y20112']) +
            4*sum_all(vars['y02112']) +
            4*sum_all(vars['z20112']) +
            4*sum_all(vars['z02112'])
            )

def add_cons_type_12(ilp, vars):
    ilp += (4 - vars['y22020'] >=
            vars['y20120'] + sum_all(vars['y20003'])
            )
    ilp += (4 - vars['y22020'] >=
            vars['y02120'] + sum_all(vars['y02003'])
            )

def add_cons_type_11(ilp, vars):
    ilp += vars['y22020'] <= 1

def add_cons_type_10(ilp, vars):
    ilp += (5 ==
            vars['y22020'] + vars['y20120'] +
            sum_all(vars['y20003']) +
            sum_all(vars['y20004']) +
            sum_all(vars['y20112']) +
            sum_all(vars['z20112'])
            )

def add_cons_type_9(ilp, vars):
    ilp += (vars['s'] + 7 ==
            5*sum_all(vars['y00105']) +
            4*sum_all(vars['y00104']) +
            2*sum_all(vars['y00212']) +
            3*sum_all(vars['y00213']) +
            3*sum_all(vars['y20003']) +
            4*sum_all(vars['y20004']) +
            2*sum_all(vars['y20112']) +
            2*sum_all(vars['z20112']) +
            3*sum_all(vars['y02003']) +
            4*sum_all(vars['y02004']) +
            2*sum_all(vars['y02112']) +
            2*sum_all(vars['z02112'])
            )

def add_cons_type_8(ilp, vars):
    ilp += (18 - vars['s'] ==
            vars['y20120'] + vars['y02120'] +
            sum_all(vars['y20003']) +
            sum_all(vars['y02003']) +
            sum_all(vars['y00104']) +
            sum_all(vars['y00212'])
            )

def add_cons_type_7(ilp, vars):
    ilp += ((vars['N'] - vars['s'] + 11)/2 ==
            10 + vars['y22020'] + vars['y00330'] +
            vars['y20120'] + vars['y02120']
            )

def add_cons_type_6(ilp, vars):
    for i in range(7):
        ilp += (vars['z20112'][i] <=
                vars['y20003'][h(i)] + vars['y20004'][h(i)] +
                vars['y20112'][h(i)]
                )
        ilp += (vars['z02112'][i] <=
                vars['y02003'][h(i)] + vars['y02004'][h(i)] +
                vars['y02112'][h(i)]
                )
        ilp += (vars['z20112'][i] + vars['z02112'][i] <=
                vars['y00105'][j(i)] + vars['y00104'][j(i)] +
                vars['y00212'][j(i)] + vars['y00213'][j(i)] +
                vars['y20112'][j(i)] + vars['y02112'][j(i)]
                )

def add_cons_type_5(ilp, vars):
    for i in range(7):
        ilp += (vars['y20112'][i] + vars['y02112'][i] <=
                vars['y00105'][h(i)] + vars['y00104'][h(i)] +
                vars['y00212'][h(i)] + vars['y00213'][h(i)] +
                vars['z20112'][h(i)] + vars['z02112'][h(i)]
                )
        ilp += (vars['y20112'][i] <=
                vars['y20003'][j(i)] + vars['y20004'][j(i)] +
                vars['z20112'][j(i)]
                )
        ilp += (vars['y02112'][i] <=
                vars['y02003'][j(i)] + vars['y02004'][j(i)] +
                vars['z02112'][j(i)]
                )

def add_cons_type_4(ilp, vars):
    for i in range(7):
        ilp += (vars['y20003'][i] <=
                vars['y20003'][h(i)] + vars['y20004'][h(i)] +
                vars['y20112'][h(i)]
                )
        ilp += (vars['y02003'][i] <=
                vars['y02003'][h(i)] + vars['y02004'][h(i)] +
                vars['y02112'][h(i)]
                )
        ilp += (vars['y20003'][i] <=
                vars['y20003'][j(i)] + vars['y20004'][j(i)] +
                vars['z20112'][j(i)]
                )
        ilp += (vars['y02003'][i] <=
                vars['y02003'][j(i)] + vars['y02004'][j(i)] +
                vars['z02112'][j(i)]
                )

def add_cons_type_3(ilp, vars):
    for i in range(7):
        ilp += (vars['y20004'][i] <=
                vars['y20003'][h(i)] + vars['y20004'][h(i)] +
                vars['y20112'][h(i)]
                )
        ilp += (vars['y02004'][i] <=
                vars['y02003'][h(i)] + vars['y02004'][h(i)] +
                vars['y02112'][h(i)]
                )
        ilp += (vars['y20004'][i] <=
                vars['y20003'][j(i)] + vars['y20004'][j(i)] +
                vars['z20112'][j(i)]
                )
        ilp += (vars['y02004'][i] <=
                vars['y02003'][j(i)] + vars['y02004'][j(i)] +
                vars['z02112'][j(i)]
                )

def add_cons_type_2(ilp, vars):
    for i in range(7):
        ilp += (1 ==
            vars['y00105'][i] + vars['y00104'][i] + vars['y00212'][i] +
            vars['y00213'][i] + vars['y20003'][i] + vars['y02003'][i] +
            vars['y20004'][i] + vars['y02004'][i] + vars['y20112'][i] +
            vars['y02112'][i] + vars['z20112'][i] + vars['z02112'][i]
            )

def make_variables():
    # Constraint Type 1 is used when defining all variables

    # Variables from Table 1
    y22020 = LpVariable('f_{22002}', lowBound=0, cat = 'Integer')
    y00330 = LpVariable('f_{00033}', lowBound=0, cat = 'Integer')
    y20120 = LpVariable('f_{20012}', lowBound=0, cat = 'Integer')
    y02120 = LpVariable('f_{02012}', lowBound=0, cat = 'Integer')

    # Variables from Table 2
    y00105 = [LpVariable('f_{'+str(i)+',00105}', cat = 'Binary')
              for i in range(7)]
    y00104 = [LpVariable('f_{'+str(i)+',00104}', cat = 'Binary')
              for i in range(7)]
    y00212 = [LpVariable('f_{'+str(i)+',00212}', cat = 'Binary')
              for i in range(7)]
    y00213 = [LpVariable('f_{'+str(i)+',00213}', cat = 'Binary')
              for i in range(7)]
    y20003 = [LpVariable('f_{'+str(i)+',20003}', cat = 'Binary')
              for i in range(7)]
    y02003 = [LpVariable('f_{'+str(i)+',02003}', cat = 'Binary')
              for i in range(7)]
    y20004 = [LpVariable('f_{'+str(i)+',20004}', cat = 'Binary')
              for i in range(7)]
    y02004 = [LpVariable('f_{'+str(i)+',02004}', cat = 'Binary')
              for i in range(7)]

    # Variables from Table 3
    y20112 = [LpVariable('f_{'+str(i)+',20112}', cat = 'Binary')
              for i in range(7)]
    y02112 = [LpVariable('f_{'+str(i)+',02112}', cat = 'Binary')
              for i in range(7)]
    z20112 = [LpVariable('g_{'+str(i)+',20112}', cat = 'Binary')
              for i in range(7)]
    z02112 = [LpVariable('g_{'+str(i)+',02112}', cat = 'Binary')
              for i in range(7)]

    # Variables from Table 4
    s = LpVariable('s', lowBound = 0, cat = 'Integer')
    N = LpVariable('N', lowBound = 0, cat = 'Integer')

    # Return all variables in a dict
    return {
        'y22020': y22020,
        'y00330': y00330,
        'y20120': y20120,
        'y02120': y02120,
        'y00105': y00105,
        'y00104': y00104,
        'y00212': y00212,
        'y00213': y00213,
        'y20003': y20003,
        'y02003': y02003,
        'y20004': y20004,
        'y02004': y02004,
        'y20112': y20112,
        'y02112': y02112,
        'z20112': z20112,
        'z02112': z02112,
        's': s,
        'N': N
    }

def check_solve(ilp, solver_name, vars):
    # Possible solve states
    # “Not Solved”, “Infeasible”, “Unbounded”, “Undefined” or “Optimal”
    if LpStatus[ilp] == 'Optimal':
        obj = str(vars['N'].value())
        print(solver_name + ': Optimal solution found. Objective value: ' + obj)
    else:
        print(solver_name + ': ' + LpStatus[ilp])

def ilp_1():

    ilp = LpProblem("ILP_1", LpMaximize)

    vars = make_variables()

    # Constraint Type 1 is used when defining all variables
    add_cons_type_2(ilp, vars) # necessary, else always finds sol
    add_cons_type_3(ilp, vars) # necessary, else always finds sol
    add_cons_type_4(ilp, vars) # necessary, else always finds sol
    add_cons_type_5(ilp, vars) # necessary, else always finds sol
    add_cons_type_6(ilp, vars) # necessary, else always finds sol
    add_cons_type_7(ilp, vars) # necessary, else unbounded
    add_cons_type_8(ilp, vars) # necessary, else always finds sol
    add_cons_type_9(ilp, vars) # necessary, else always finds sol
    add_cons_type_10(ilp, vars) # necessary, else always finds sol
    add_cons_type_11(ilp, vars) # unnecessary but helps explore cons_type_12
    add_cons_type_12(ilp, vars) # necessary, else always finds sol
    add_cons_type_13(ilp, vars) # necessary, else unbounded

    # Objective function
    ilp += vars['N']

    # write lp file
    ilp.writeLP('output/ilp_1.lp')

    # Solve ILP
    scip_sol = ilp.solve(getSolver('SCIP_CMD', msg = False,
                                   logPath="output/scip_ilp_1.log"))
    check_solve(scip_sol, 'SCIP', vars)

    gurobi_sol = ilp.solve(getSolver('GUROBI_CMD', msg = False,
                                     logPath="output/gurobi_ilp_1.log"))
    check_solve(gurobi_sol, 'Gurobi', vars)

    coin_sol = ilp.solve(getSolver('COIN_CMD', msg = False,
                                   logPath="output/coin_ilp_1.log"))
    check_solve(coin_sol, 'COIN_CMD', vars)

def ilp_2():

    ilp = LpProblem("ILP_2", LpMaximize)

    vars = make_variables()

    # Constraint Type 1 is used when defining all variables
    add_cons_type_2(ilp, vars) # necessary, else always finds sol
    add_cons_type_3(ilp, vars) # necessary, else always finds sol
    add_cons_type_4(ilp, vars) # necessary, else always finds sol
    add_cons_type_5(ilp, vars) # necessary, else always finds sol
    add_cons_type_6(ilp, vars) # necessary, else always finds sol
    add_cons_type_7(ilp, vars) # necessary, else unbounded
    add_cons_type_8(ilp, vars) # necessary, else always finds sol
    add_cons_type_9(ilp, vars) # necessary, else always finds sol
    add_cons_type_10(ilp, vars) # necessary, else always finds sol
    add_cons_type_11(ilp, vars) # unnecessary but helps explore cons_type_12
    add_cons_type_12(ilp, vars) # necessary, else always finds sol
    add_cons_type_13(ilp, vars) # necessary, else unbounded
    add_cons_type_14(ilp, vars)

    # Objective function
    ilp += vars['N']

    # write lp file
    ilp.writeLP('output/ilp_2.lp')

    # Solve ILP
    scip_sol = ilp.solve(getSolver('SCIP_CMD', msg = False,
                                   logPath="output/scip_ilp_2.log"))
    check_solve(scip_sol, 'SCIP', vars)

    gurobi_sol = ilp.solve(getSolver('GUROBI_CMD', msg = False,
                                     logPath="output/gurobi_ilp_2.log"))
    check_solve(gurobi_sol, 'Gurobi', vars)

    coin_sol = ilp.solve(getSolver('COIN_CMD', msg = False,
                                   logPath="output/coin_ilp_2.log"))
    check_solve(coin_sol, 'COIN_CMD', vars)


def main():
    print("Available solvers on build:", listSolvers(onlyAvailable=True), "\n")

    print("Proof of Lemma 4.33\n")
    ilp_1()
    print("\nProof of Theorem 4.35\n")
    ilp_2()

main()
