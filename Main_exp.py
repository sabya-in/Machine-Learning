from Configure_exp import setup
from Analytics_exp import analysis

def get_q_max(Q_val,epsilon=0):
    from numpy.random import choice
    choice_arr = []
    action_arr = []
    max = 0
    for i in range(0,len(Q_val)-1):
        max = i if Q_val[max] > Q_val[i+1] else (i+1)
        choice_arr.append(epsilon/(len(Q_val)-1))
        action_arr.append(i)
    choice_arr.append(epsilon/(len(Q_val)-1))
    action_arr.append(len(Q_val)-1)
    choice_arr[max] = 1-epsilon
    return choice(action_arr,1, p=choice_arr)[0]
    
def get_cum_reward_max(arr):
    max = 0
    for i in (0,len(arr)-2):
        max = i+1 if arr[i+1].get_imm_reward() > arr[i].get_imm_reward() else i
    return max

(bandit_arr,Q_val,epsilon,E,sim_tim) = setup.configure()
an = analysis()

for i in range(1,sim_tim):
    Q_max = int(get_q_max(Q_val,epsilon))
    R = bandit_arr[Q_max].lever_pull()
    Q_val[Q_max] = Q_val[Q_max] + E*(R-Q_val[Q_max])
    R_max = R
    for j in range(0,len(Q_val)):
        if j == Q_max:
            bandit_arr[j].update(Q_val[Q_max],R,i)
        else:
            R_others = bandit_arr[j].lever_pull()
            bandit_arr[j].update(None,R_others,i)
            R_max = R_others if R_others > R_max else R_max
    an.percent_Opt_Act(R_max,R,Q_max,get_cum_reward_max(bandit_arr),i)

an.plot_opt_action_imm()
an.plot_opt_cumm_rew()
    
for i in bandit_arr:
    print("Cummulative actual reward :",i.plotter())

print(max(Q_val),Q_val)
