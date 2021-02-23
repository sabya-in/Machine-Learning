# Multi-Armed-Bandit
Algorithm to analyze n-armed Bandit problem

# Multi Armed bandit problem (UCB tobe implemented later)

In the first part we have tried to visualize how perfect the Q learning works in extracting maximum reward, how successful it is in predicting intermeddiate rewards and in the end how well it predicted the slot machine that would give maximum cumulative rewards

In the second part we have checked how the Q value saturates and how the percentage of Optimum Action choosen stabilizes with the number of iteration

We have used Bell Curve for generating ranom numbers in python the random.gauss() function. 

Each such Bandit or Slot machine will thus have a charecteristic curve (specially when the mean and standard deviation for them is set, whose values are entered by the user (typically this should be closed and user should not be able to see what is the actual Mu and Sigma for each but for experimental purpose it is set by user themselves).

E = Step size (or weight of past reward on current Q value selesction);
epsilon = Exploration probability between 0-1;
R = Inital reward for faster and better reward searches;

# Instructions to run
  1. Files postfixed with _exp (experiment folder) are part of nbandit code for checking transition between different decision trees / banndits (slots)
  2. Files postfixed with _nbandit (core folder) are part of nbandit code and shows how the Q_max and percent of optimum actions selected saturates
  3. The Main_exp and Main_nbandit are launcher files
  4. Once you launch you need to provide E,epsilon,R
  5. Next seed bell curve for each slot machine or bandit in our n-bandit problem

# Core
  In this algorithm we calculate Qvalue deterministically for each iteration which ideally isnt the case in real world. 
  This model is very deterministic and hence the curve chooses the winner slot / optimum slot using the optimum policy very fast and remains saturated.
  The probablity of choosing another slot decereases after the first 100 iteration as we have clear winner.
  
# Experiment
  In this we choose only those Qvalue where we expect optimum reward we dont calculate Qvalue for each slot in each step.
  For a particular bandit we choose Qvalue only when we choose it as Action according to optimum policy.
  The variance of the graph is very good and almost always we choose the proper Action , ( which also many a times gives us the cumulative reward not always)
  If we have two bell curves _(Mu=4,sd=0.5) , (Mu=4,sd=2.8)_ the obvious smart choice is to choose (1) instead of (2) for a stable reward, 
  but if we are looking for wildly optimistic results we can choose (2) , this is evidient from the fact that setting greater value of _E_ leads to choose (2) which may in short term give wildly high jumps.   

# UCB implementation can make this implementation much better
