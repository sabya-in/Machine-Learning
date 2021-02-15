from Bandit_nbandit import bandit

class setup:
    def __init__():
        pass
    def configure():
        Q = 0
        Q_arr = []
        bandit_arr = []
        n = int(input("Enter number of slot machines / bandits 2-N intergers "))
        E = float(input("Enter step size or Past-Reward diminishing factor between 0-1 "))
        Q = float(input("Enter beginning Q value 0-N whole numbers "))
        epsilon = float(input("Enter epsilon for exploration between 0-1 "))
        sim_tim = int(input("Enter simulation time / iterations 50-10k integers"))
        for i in range(0,n):
            mu = float(input("Enter mean for Bandit"+str(i)+" "))
            sigma = float(input("Enter standard deviation for Bandit"+str(i)+" "))
            name = str(input("Enter name any string "))
            bandit_arr.extend([bandit(mu,sigma,name)])
            Q_arr.extend([Q])
        return((bandit_arr,Q_arr,epsilon,E,sim_tim))
