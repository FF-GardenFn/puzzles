ero-Sum Game: Two players (batter and pitcher) with opposing goals. The batter wants to maximize expected score; the pitcher wants to minimize it. What one gains, the other loses.
•  Mixed Strategies: Players randomize actions to keep opponents guessing. For example, the pitcher might throw a strike with probability  x  and a ball with  1 - x .
•  Nash Equilibrium: A strategy pair where neither player can improve by unilaterally changing their strategy. In mixed strategies, it often makes the opponent “indifferent” between choices.
•  Why It Matters Here: Both players choose simultaneously and secretly, so we solve for equilibria at each state to find optimal play.

Expected Value (EV): The long-run average outcome. For a state with value  V ,  V = \sum (\text{probability of outcome} \times \text{value of outcome}) .
•  Markov Chains/States: The at-bat is a process with states (e.g., 0 balls, 0 strikes). Transitions depend on actions and probabilities.
•  Backward Induction: Start from end states (walk, strikeout, home run) and work backward to compute EVs and strategies.
•  Forward Propagation: Once strategies are known, simulate from the start to compute probabilities of reaching specific states.
•  Optimization: Vary  p  and maximize  q , the probability of hitting state (3,2).
1.3 Key Math Tools
•  Payoff Matrix: For each state, a 2x2 matrix of EVs based on actions (pitcher: strike/ball; batter: swing/wait).
•  Indifference Principle: At equilibrium, the EV for one player’s choices equals when the other mixes optimally.
•  Numerical Optimization: Since analytical solutions are hard, use code to find the  p  that maximizes  q .
These concepts model uncertainty (e.g., home run with prob  p ) and strategic interaction.
•  At-Bat Structure: Starts at (0 balls, 0 strikes). Ends with:
	•  4 balls: 1 point (walk).
	•  3 strikes: 0 points (out).
	•  Home run: 4 points.
•  Actions per Pitch:
	•  Pitcher: Throw strike or ball.
	•  Batter: Swing or wait.
	•  Chosen simultaneously.
•  Outcomes:
	•  Pitcher ball + Batter wait: +1 ball.
	•  Pitcher strike + Batter wait: +1 strike.
	•  Pitcher ball + Batter swing: +1 strike (swinging at air).
	•  Pitcher strike + Batter swing: Home run with prob  p , else +1 strike.
•  States: Grid of (b, s) where b = 0-3 (since 4 ends), s = 0-2 (since 3 ends).
•  Objective: Quad-A tunes  p  (0 to 1) to maximize  q , the prob of reaching (3,2) under optimal play.
2.2 Constraints and Manipulations
•  Constraints:
	•  Independent pitches, but cumulative counts.
	•  No other hits; only home run or nothing on contact.
	•  Optimal mixed strategies: Players aren’t predictable.
•  Manipulation:  p  affects home run likelihood, influencing aggressiveness. High  p  encourages swinging (more home runs) but risks early outs if missing. Low  p  encourages waiting.
•  Key Insight: At equilibrium, strategies balance risks. We manipulate  p  to make deep counts (like full count) more likely by encouraging continuation over termination.
2.3 Challenges in Modeling
•  Termination Risks: Home runs end at-bats early, reducing chances of reaching (3,2).
•  State-Dependence: Strategies vary by count (e.g., more aggressive at 3-2).
•  Computation: 12 transient states (b=0-3, s=0-2). Need to solve equilibria per state.
Section 3: Thought Framework for Solution
3.1 Step 1: Define State Values with Backward Induction
•  Start from terminals:
	•  V(4, s) = 1 (walk, any s).
	•  V(b, 3) = 0 (strikeout, any b).
	•  Home run = 4 (immediate).
•  For each (b,s) from end to start (b=3 to 0, s=2 to 0):
	•  Build 2x2 payoff matrix for batter’s EV: skipeed here

Due to symmetry, optimal mixed prob  x  (pitcher strike prob = batter swing prob) is:
		•   \delta = V(b+1,s) - V(b,s+1) 
		•  Denom = p(4 - V(b,s+1)) + \delta
		•  If \delta > 0 and denom > 0, x = \delta / denom; else x=0.
	•  Then V(b,s) = x * V(b,s+1) + (1-x) * V(b+1,s)  (indifference EV).
This gives V(b,s) and x(b,s) for all states.