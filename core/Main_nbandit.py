from Configure_nbandit import setup
from Analytics_nbandit import analysis

def get_q_max(Q_val,epsilon=0):
    from numpy.random import choice
    choice_arr = []
    action_arr = []
    max = 0
    for i in range(0,len(Q_val)-1):
        max = i if Q_val[i] > Q_val[i+1] else (i+1)
        choice_arr.extend([epsilon/(len(Q_val)-1)])
        action_arr.extend([i])
    choice_arr.append(1-epsilon)
    action_arr.append(max)
    return choice(action_arr,1, p=choice_arr)[0]

(bandit_arr,Q_val,epsilon,E,sim_tim) = setup.configure()
an = analysis()

for i in range(1,sim_tim):
    for j in range(0,len(Q_val)):
        R = bandit_arr[j].lever_pull()
        Q_val[j] += E*(R-Q_val[j])
        bandit_arr[j].update(Q_val[j],R,i)
    print(get_q_max(Q_val,epsilon))
    an.current_Opt_Act(get_q_max(Q_val,epsilon),i)
    
an.plot_opt_action(Q_val.index(max(Q_val)))
print("Optimum Q value: "+str(max(Q_val)))
    
for i in bandit_arr:
    print("Cummulative actual reward :",i.plotter())

print(max(Q_val),Q_val)
