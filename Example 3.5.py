# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 10:22:03 2022

@author: grace_elizabeth
"""

from gurobipy import *

try:
    
    #Parameters
    w = [6, 10, 8, 4]
    x = [10, 10, 8, 12]
    y = [2, 10, 6, 5]
    
    #Indices
    n = len(w)
    
    #Create model
    m = Model("Example 3.5")
    
    #Decision variables
    x_bar = m.addVars(1, vtype = GRB.CONTINUOUS, name = "x-bar")
    y_bar = m.addVars(1, vtype = GRB.CONTINUOUS, name = "y-bar")
    xp = m.addVars(n, lb = 0, vtype = GRB.CONTINUOUS, name = "x-positive")
    xn = m.addVars(n, lb = 0, vtype = GRB.CONTINUOUS, name = "x-negative")
    yp = m.addVars(n, lb = 0, vtype = GRB.CONTINUOUS, name = "y-positive")
    yn = m.addVars(n, lb = 0, vtype = GRB.CONTINUOUS, name = "y-negative")
    
    #Set objective fuction
    m.setObjective(quicksum(w[i] * (xp[i] + xn[i] + yp[i] + yn[i]) for i in range(n)), GRB.MINIMIZE)
    
      #Write constraints
    for i in range(n):
        m.addConstr(x[i] - x_bar[0] == xp[i] - xn[i], name = "Constraint 3.20")
        m.addConstr(y[i] - y_bar[0] == yp[i] - yn[i], name = "Constraint 3.21")

    #Call Gurobi Optimizer
    m.optimize()
    if m.status == GRB.OPTIMAL:
       for v in m.getVars():
           if v.x > 0:
               print('%s = %g' % (v.varName, v.x)) 
       print('Obj = %f' % m.objVal)
    elif m.status == GRB.INFEASIBLE:
       print('LP is infeasible.')
    elif m.status == GRB.UNBOUNDED:
       print('LP is unbounded.')
except GurobiError:
    print('Error reported')