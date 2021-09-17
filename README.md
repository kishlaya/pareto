# Pareto Distribution and Price's Law

## Why?

I was watching a lecture by Jordan Peterson, where he talks about Pareto Distribution and Price's Law.
So I thought I would try and verify that on a simple game, similar to the one he shows in his lecture.

## What?
 
I tried running a small, very-simplistic experiment:
- 200 people are in a room each with $10
- Two arbitrary people get up and play a random game
- Loser loses $1 to the winner
- Once someone is out of money, they are out of game

## Results

`pareto.py` is the script which manages this and the results show that the wealth
- starts out as a point mass distribution
- quickly transforms to a normal distribution
- moves towards a more and more skewed pareto distribution

https://user-images.githubusercontent.com/4151255/132993405-2a90c64a-a868-48d8-ba6a-5e766350d799.mp4

## Theory

Let the collection of all people be underlying sample space and the power set to be the accompanying sigma algebra. 
Now let X_t be the random variable which maps each person to their wealth at time t.

X_0 has point mass distribution is given. Now X_1 is decided according to the above rules.

With abuse of notation, X_t can be seen to be a Markov Chain, with the state space given as ordered tuple of wealth of each person.

How does this Markov Process X_t behave? Does the process stabilize - all but one owns all the wealth OR does some set of people own majority of the wealth?

### TODO

- Better understand the theory
- What is the limiting distribution?
- What happens as the population increases?
- Quantified relation with Price's Law
