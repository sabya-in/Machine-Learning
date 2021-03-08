from neural_net import q_neural_network as dqn
import numpy as np
import time as t
import math
import gym

if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    state_set_size = env.observation_space.shape[0]
    action_set_size = env.action_space.n
    q = dqn(state_set_size,action_set_size,0.9)
    penalty = 4.0
    penalty = float(input("Enter penalty for losing float(default 4.0):") or penalty)
    discount = 0.8
    discount = float(input("Enter reward discount float(default 0.8):") or discount)
    exploration = 0.3
    exploration = float(input("Enter exploration float(default 0.3):") or exploration)
    done = False
    batch_size = 40
    exploration = int(input("Enter Batch Size for neural network training after each game int(default 40):") or batch_size)
    direction = 'none'
    for episodes in range(16000):
        state = env.reset()
        state = np.reshape(state, [1, state_set_size])
        for time in range(400):
            env.render()
            action = q.action_decide(state.reshape(1,-1),exploration,math.sqrt((episodes+1)**(1/4)))
            direction = 'left' if bool(action) else 'right'
            #print(direction)
            #t.sleep(0.1)
            state_n,reward,done,debug = env.step(action)
            reward += 0 if not done else -penalty
            q.store(state,action,reward,state_n,done)
            state = state_n
            if done:
                q.avg_reward_solver(time)
                break
            if len(q.memory) > batch_size:
                q.train_batch(discount,batch_size)
                q.flush()
                print('Average reward in last 100 or less iterations - '+str(q.check_avg_reward_of_solver()))
