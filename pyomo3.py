import pyomo.environ as pe

def buildmodel():
    #model
    model = pe.ConcreteModel()
    #variables
    model.x1 = pe.Var(domain = pe.NonNegativeReals)
    model.x2 = pe.Var(domain = pe.NonNegativeReals)
    model.x3 = pe.Var(domain = pe.NonNegativeReals)
    model.x4 = pe.Var(domain = pe.NonNegativeReals)
    model.x5 = pe.Var(domain = pe.NonNegativeReals)
    model.x6 = pe.Var(domain = pe.NonNegativeReals)
    model.x7 = pe.Var(domain = pe.NonNegativeReals)
    #objective
    model.obj = pe.Objective ( expr = model.x1*294 + model.x2*93 + model.x3*96 + model.x4*155 + model.x5*294 + model.x6*96 + model.x7*155, sense = pe.maximize)
    #constraints
    model.c1 = pe.Constraint(expr = 600*model.x1 + 396*model.x2 + model.x3*195 + model.x4*660 + model.x5*600 + model.x6*195 + model.x7*660<=884)
    model.c2 = pe.Constraint(expr = 600*model.x1 + 396*model.x2 + model.x3*195 + model.x4*660 + model.x5*600 + model.x6*195 + model.x7*660<=884)
    model.c3 = pe.Constraint(expr = 600*model.x1 + 396*model.x2 + model.x3*195 + model.x4*660 + model.x5*600 + model.x6*195 + model.x7*660<=884)
    model.c4 = pe.Constraint(expr = model.x1>=0)
    model.c5 = pe.Constraint(expr = model.x2>=0)
    model.c6 = pe.Constraint(expr = model.x3>=0)
    model.c7 = pe.Constraint(expr = model.x4>=0)
    model.c8 = pe.Constraint(expr = model.x5>=0)
    model.c9 = pe.Constraint(expr = model.x6>=0)
    model.c10 = pe.Constraint(expr = model.x7>=0)
    model.c11 = pe.Constraint(expr = model.x1<=1)
    model.c12 = pe.Constraint(expr = model.x2<=1)
    model.c13 = pe.Constraint(expr = model.x3<=1)
    model.c14 = pe.Constraint(expr = model.x4<=1)
    model.c15 = pe.Constraint(expr = model.x5<=1)
    model.c16 = pe.Constraint(expr = model.x6<=1)
    model.c17 = pe.Constraint(expr = model.x7<=1)
    return model

if __name__ == '__main__':
    model = buildmodel()
    opt = pe.SolverFactory('glpk')
    opt.solve(model)
    print('x1:',pe.value(model.x1))
    print('x2:',pe.value(model.x2))
    print('x3:',pe.value(model.x3))
    print('x4:',pe.value(model.x4))
    print('x5:',pe.value(model.x5))
    print('x6:',pe.value(model.x6))
    print('x7:',pe.value(model.x7))
