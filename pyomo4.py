import pyomo.environ as pe

def buildmodel():
    #model
    model = pe.ConcreteModel()
    #variables
    model.x1 = pe.Var(domain = pe.NonNegativeReals)
    model.x2 = pe.Var(domain = pe.NonNegativeReals)
    model.x3 = pe.Var(domain = pe.NonNegativeReals)
    #objective
    model.obj = pe.Objective(expr = model.x1*2.5 + model.x2*4.5 + model.x3*7.5,sense = pe.maximize)
    #constraints
    model.c1 = pe.Constraint(expr = model.x1/15 + model.x2/6 + model.x3/11 <=45)
    model.c2 = pe.Constraint(expr = model.x1*5 + model.x2*2 + model.x3*4 <=450)
    model.c3 = pe.Constraint(expr = model.x1>=0)
    model.c4 = pe.Constraint(expr = model.x2>=0)
    model.c5 = pe.Constraint(expr = model.x3>=0)
    model.c6 = pe.Constraint(expr = model.x1<=230)
    model.c7 = pe.Constraint(expr = model.x2<=150)
    model.c8 = pe.Constraint(expr = model.x3<=140)
    return model
    
if __name__ == '__main__':
    model = buildmodel()
    opt = pe.SolverFactory('glpk')
    opt.solve(model)
    print('x1:',pe.value(model.x1))
    print('x2:',pe.value(model.x2))
    print('x3:',pe.value(model.x3))
    print('z:',pe.value(model.x1)*2.5 + pe.value(model.x2)*4.5 + pe.value(model.x3) * 7.5) 
    
