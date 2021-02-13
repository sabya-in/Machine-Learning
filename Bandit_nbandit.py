class bandit:
    def __init__(self, mu=0.5, sigma=0.2, name='K'):
        self.name = name
        self.mu = mu
        self.sigma = sigma
        self.cumm_reward = [0]
        self.Q_val = [0]
        self.itr = [0]
    def lever_pull(self):
        import random
        return (random.gauss(self.mu,self.sigma))
    def get_imm_reward(self):
        return self.cumm_reward
    def update(self,q,r,i):
        self.Q_val.append(q)
        self.cumm_reward.append(self.cumm_reward[i-1]+r)
        self.itr.append(i)
    def plotter(self):
        from matplotlib import pyplot as p
        p.plot(self.itr,self.Q_val)
        p.title(str(self.name)+' optimum action transition')
        p.show()
        return (self.cumm_reward[-1])
