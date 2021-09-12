import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
 people = 200
 amount = 10
 state = [amount]*people
 return (people, amount, state)
 
def reset(n):
 plt.cla()
 plt.xlabel("Money")
 plt.ylabel("People")
 axes = plt.gca()
 axes.set_ylim([0,n])

def step(frame, n, step_size, state):
 reset(n)
 
 if frame == 0:
  plt.hist(state, bins=list(range(amt*5)))
  return 
  
 for _ in range(step_size):
  x = np.random.randint(n)
  y = np.random.randint(n)
  if x == y or state[x] == 0 or state[y] == 0:
   continue

  result = np.random.randint(2)
  if result == 0:
   state[x] -= 1
   state[y] += 1
  else:
   state[x] += 1
   state[y] -= 1

 plt.hist(state, bins=list(range(amt*5)))

(n, amt, state) = init()

fig = plt.figure(figsize=(12.8,9.6))

step_size = 10
fps_rate = 30
minutes = 1
frame_count = fps_rate * minutes * 60
anim = animation.FuncAnimation(fig, step, frame_count, fargs=(n, step_size, state, ))

anim.save("pareto.mp4", writer="ffmpeg", fps=fps_rate)
