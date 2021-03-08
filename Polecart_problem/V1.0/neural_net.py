from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense
import numpy as np
import random
import gym

class q_neural_network:

	def __init__(self,state_set_size,action_set_size,epsilon,learning_rate=0.001):
		self.states = state_set_size
		self.actions = action_set_size
		self.memory = []
		self.last_100 = []
		self.epsilon = epsilon
		self.epsilon_min = 0.01
		self.epsilon_decay = epsilon
		self.learning_rate = learning_rate
		self.model = self.build_model()
		
	def build_model(self):
		model = Sequential()
		model.add(Dense(24, input_dim=self.states, activation='relu'))
		model.add(Dense(24, activation='relu'))
		model.add(Dense(self.actions, activation='linear'))
		model.compile(loss='mse',optimizer=Adam(lr=self.learning_rate))
		return model
		
	def store(self,state,action,reward,state_n,done):
		self.memory.append((state,action,reward,state_n,done))
		
	def flush(self):
		self.memory = []
		
	def train_batch(self,gamma,batch_size):
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay
		for state,action,reward,state_n,done in self.memory:
			discounted_reward = reward if done else (gamma*np.amax(self.model.predict(state_n.reshape(1,-1))[0]) + reward)
			Y_train = self.model.predict(state.reshape(1,-1))
			Y_train[0][action] = discounted_reward
			X_train = state.reshape(1,-1)
			self.model.fit(X_train,Y_train,epochs=1, verbose=0)
			
	def action_decide(self,state,epsilon,exploration_decay):
		if np.random.rand() <= epsilon:
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
	
