from ortools.sat.python import cp_model


def maximizeIt(m,lists):
    model=cp_model.CpModel()
    k=model.NewIntVar(0,100,'k')
    x=[]
    for i in range(len(lists)):
        temp=[]
        for j in range(len(lists[i])):
            temp.append(model.NewIntVar(0, 1, 'x'))
        x.append(temp)
    for i in range(len(lists)):
        sum=0
        for j in range(len(lists[i])):
            sum=sum+x[i][j]
        model.Add(sum==1)
    obj=0
    for i in range(len(lists)):

        for j in range(len(lists[i])):
            obj=obj+x[i][j]*lists[i][j]**2
    model.Add(obj-m*k>=0)
    model.Maximize(obj+m*k)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    return solver.ObjectiveValue()-solver.Value(k)*m*2


m=100
lists=[]
lists.append([1,2,3,6,8])
lists.append([5,5,7,6])

print(maximizeIt(m,lists))
