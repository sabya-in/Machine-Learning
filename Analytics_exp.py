class analysis:
    def __init__(self):
        self.plot_x = [1]
        self.plot_y = [0]
        self.plot_y1 = [0]
        self.plot_percent = [0]
        self.plot_percent1 = [0]
    def percent_Opt_Act(self,R_max,R,Q_max,Cumm_R,i):
        if R_max == R:
            self.plot_y.append((self.plot_y[i-1]+1))
        else:
            self.plot_y.append(self.plot_y[i-1])
        if Q_max == Cumm_R:
            self.plot_y1.append((self.plot_y1[i-1]+1))
        else:
            self.plot_y1.append(self.plot_y1[i-1])
        self.plot_x.append(i)
        self.plot_percent.append(self.plot_y[i]/i*100)
        self.plot_percent1.append(self.plot_y1[i]/i*100)
    def plot_opt_action_imm(self):
        from matplotlib import pyplot as p
        p.plot(self.plot_x,self.plot_percent)
        p.title('Optimum Immediate Reward Percentage from current Action')
        p.show()
        #return (self.plot_y)
    def plot_opt_cumm_rew(self):
        from matplotlib import pyplot as p
        p.plot(self.plot_x,self.plot_percent1)
        p.title('Optimum Cumulative Reward Percentage from current Action')
        p.show()
