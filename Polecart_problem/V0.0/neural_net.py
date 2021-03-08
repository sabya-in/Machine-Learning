from sklearn.neural_network import MLPClassifier as mlp
from collections import deque
import numpy as np
import random

class q_neural_network:

    def __init__(self,state_set_size,action_set_size,epsilon):
        self.states = state_set_size
        self.actions = action_set_size
        self.memory = []
        self.last_100 = []
        X_train = np.ones((1,state_set_size))
        Y_train = (np.array([1,0])).reshape((1,action_set_size))
        self.model = mlp(random_state=2,max_iter=1000)
        self.model.partial_fit(X_train,Y_train,classes=np.unique(Y_train))
        
    def store(self,state,action,reward,state_n,done):
        self.memory.append((state,action,reward,state_n,done))
        
    def flush(self):
        self.memory = []
        
    def train_batch(self,gamma,batch_size):
        for state,action,reward,state_n,done in self.memory:
            discounted_reward = reward if done else (gamma*np.amax(self.model.predict(state_n.reshape(1,-1))) + reward)
            Y_train = self.model.predict(state.reshape(1,-1))
            Y_train[0][action] = discounted_reward
            X_train = state.reshape(1,-1)
            self.model = self.model.partial_fit(X_train,Y_train)
            
    def action_decide(self,state,epsilon,exploration_decay):
        if np.random.rand() <= epsilon/exploration_decay:
            return random.randrange(self.actions)
        q_val = self.model.predict(state)
        return np.argmax(q_val[0])

    def avg_reward_solver(self,current_reward):
        if len(self.last_100) < 100:
            self.last_100.append(current_reward)
        else:
            self.last_100 = self.last_100[1:99]
            self.last_100.append(current_reward)
        return None
        
    def check_avg_reward_of_solver(self):
        return(sum(self.last_100)/len(self.last_100))
