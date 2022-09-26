import pyomo.environ as pe

def buildmodel():
    #model
    model = pe.ConcreteModel()
    #variables
    model.x = pe.Var(domain=pe.NonNegativeReals)
    model.y = pe.Var(domain=pe.NonNegativeReals)
    #objective
    model.obj = pe.Objective(expr = 40*model.x + 50*model.y, sense = pe.maximize)
    #constraints
    model.c1 = pe.Constraint(expr = model.x + model.y <= 50)
    model.c2 = pe.Constraint(expr = 3*model.x + 4*model.y <=180)
    model.c3 = pe.Constraint(expr = model.y <=40)
    return model
    
   
if __name__ == "__main__":
    model = buildmodel()
    opt = pe.SolverFactory("glpk")
    opt.solve(model)
    print("x: ",pe.value(model.x))
    print("y: ",pe.value(model.y))
