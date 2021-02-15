class analysis:
    def __init__(self):
        self.plot_x = [1]
        self.plot_y = [0]
        self.plot_percent = [0]
    def current_Opt_Act(self,Q_max_index,i):
        self.plot_y.append(Q_max_index)
        self.plot_x.append(i)
    def plot_opt_action(self,Q_opt):
        from matplotlib import pyplot as p
        tot = 0
        for i in range(0,len(self.plot_y)-1):
            if int(self.plot_y[i]) == int(Q_opt):
                tot+=1
                self.plot_percent.append((tot/self.plot_x[i])*100)
            else:
                self.plot_percent.append((tot/self.plot_x[i])*100)
        p.plot(self.plot_x,self.plot_percent)
        p.title('Percentage of Optimum Reward')
        p.show()
