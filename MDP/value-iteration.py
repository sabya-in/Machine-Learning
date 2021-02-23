"""
Solving Gambler's problem using Value-Itertion.
Author : Sabyasachi Mondal (sachi.iiest@gmail.com)
"""

from matplotlib import pyplot as plt
import copy

state = []
action = []
prob = (0.5,0.5)
gamma = 0.9
state_n = []
v = []

print("A Gambler decides to bet money between 1-99$ . If the Gamber stakes a$ and wins then he gets 2a$ otherwise he loses his stake.")
print("Given he wins the bet once a total of 100$ is won how should he place his bets.")
p = float(input("Enter probability of winning a bet 0-1 float"))
prob = (1.0-p,p)
gamma = float(input("Enter reward discount 0-1 float"))

def get_policy(v):
    policy = []
    for s in range(1,len(v)-1):
        q = []
        for a in range(len(action[s])):
            sum = 0
            for s_index in range(len(state_n[s][a])):
                (r,s_) = (1,100) if(state_n[s][a][s_index]>=100) else (0,state_n[s][a][s_index])
                sum+=prob[s_index]*(r+gamma*v[s_])
            q.extend([sum])
        policy.extend([action[s][q.index(max(q))]])
    return policy

def initstates():
    for i in range(0,100):
        state.extend([i])
        v.extend([0])
        possact = [a for a in range(1,min(i+1,101-i))]
        state_nxt = [(i-a,i+2*a) for a in range(1,min(i+1,101-i))]
        if i == 0:
            action.extend([[0]])
            state_n.extend([[[0]]])
        else:
            action.extend([possact])
            state_n.extend([state_nxt])   
    state.extend([100])
    v.extend([0])

def val_iteration():
    eps = 1e-1
    delta,loop_break = 0,0
    while(loop_break < 10000):
        back_up = copy.deepcopy(v)
        for s in range(1,len(state)-1):
            q = []
            for a in range(len(action[s])):
                sum = 0
                for s_index in range(len(state_n[s][a])):
                    (r,s_) = (1,100) if(state_n[s][a][s_index]>=100) else (0,state_n[s][a][s_index])
                    sum+=prob[s_index]*(r+gamma*v[s_])  
                q.extend([sum])
            v[s]=max(q)
            delta = abs(back_up[s]-v[s]) if (abs(back_up[s]-v[s]) > delta) else delta
        if delta <= eps :
            break
        loop_break+=1
    return (v,loop_break)
    
initstates()
v,iter = val_iteration()
policy = get_policy(v)
plt.plot(state[1:-2],v[1:-2])
plt.show()
plt.plot(state[0:-2],policy)
plt.show()
