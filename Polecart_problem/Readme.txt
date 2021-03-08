Classic polecart problem from GYM

Controlling a pole hinged upright to a pole cart with no control system but using Monte Carlo experiments.

Gym gives outout as position_cart,velocity_cart,pole_angle,angular_velocity_pole thus 4 state variables (and infinite state spaces because of not being quantized)
Quantizing the state variables should lead to faster implementation and can help us use other Q function learning algorithms other than Neural Network witch takes too much resource to learn.

The cart is control by quantized Left or Right movements thus two action spaces.

The reward is the amount of time pole stays within contollable limits (specified in pole cart base class in gym)


We use the following functions:

1. action_decide - It predicts the action from learned (by our neural network) Q_function with a probability of exprolaration of random choice

2. train_network - It trains the neural network with (State_i,Action,Reward,State_i+1,Done) values where input is state and output is action (left or right probability).

3. Store and Flush - Store and flush are to store and flush the (State_i,Action,Reward,State_i+1,Done) values ; Done stores if you are still in game and havent crossed the controllable limit
   Store and Flush seems to take lesser time to train in smaller batches than just storing all values in queues
