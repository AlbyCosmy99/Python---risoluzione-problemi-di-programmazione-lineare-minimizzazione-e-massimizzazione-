import pyomo.environ as pe

def buildmodel():
    #model
    model = pe.ConcreteModel()
    #variables
    model.x1 = pe.Var(domain = pe.NonNegativeReals)
    model.x2 = pe.Var(domain = pe.NonNegativeReals)
    #objective
    model.obj = pe.Objective ( expr = model.x1*300 + model.x2*400, sense = pe.maximize)
    #constraints
    model.c1 = pe.Constraint(expr = 2*model.x1 + 4*model.x2 <=800)
    model.c2 = pe.Constraint(expr = 3*model.x1 + 5*model.x2 <=1200)
    model.c3 = pe.Constraint(expr = model.x2 <= model.x1)
    model.c4 = pe.Constraint(expr = model.x1>=0)
    model.c5 = pe.Constraint(expr = model.x1<=500)
    model.c6 = pe.Constraint(expr = model.x2 >=0)
    model.c7 = pe.Constraint(expr = model.x2<=300)
    return model

if __name__ == '__main__':
    model = buildmodel()
    opt = pe.SolverFactory('glpk')
    opt.solve(model)
    print('x1:',pe.value(model.x1))
    print('x2:',pe.value(model.x2))
