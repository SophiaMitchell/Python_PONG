import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
dist = np.arange(-100, 100, .01)
move = np.arange(-1, 1, .001)

# Generate fuzzy membership functions
far_below = fuzz.gbellmf(dist, 79.68, 24.6, -90)
close_below = fuzz.gaussmf(dist, -6.57989, 3.17) 
on_target = fuzz.gaussmf(dist, 0, 2)
close_above = fuzz.gaussmf(dist, 6.58, 3.17)
far_above = fuzz.gbellmf(dist, 79.68, 24.6, 90) 
down_fast = fuzz.trapmf(move, [-1.45, -1.05, -0.2, -0.1])
down_slow = fuzz.trimf(move, [-0.2, -0.1, 0])
none = fuzz.trimf(move, [-0.1, 0, 0.1])
up_slow = fuzz.trimf(move, [0, 0.1, 0.2])
up_fast = fuzz.trapmf(move, [0.1, 0.2, 1.14, 1.38])

# Visualize these universes and membership functions
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(8, 9))

ax0.plot(dist, far_below, 'b', linewidth=1.5, label='FBelow')
ax0.plot(dist, close_below, 'g', linewidth=1.5, label='CBelow')
ax0.plot(dist, on_target, 'r', linewidth=1.5, label='On')
ax0.plot(dist, close_above, 'b', linewidth=1.5, label='CAbove')
ax0.plot(dist, far_above, 'g', linewidth=1.5, label='FAbove')
ax0.set_title('Ball Relative Position')
ax0.legend()

ax1.plot(move, down_fast, 'b', linewidth=1.5, label='DFast')
ax1.plot(move, down_slow, 'g', linewidth=1.5, label='DSlow')
ax1.plot(move, none, 'r', linewidth=1.5, label='Stop')
ax1.plot(move, up_slow, 'b', linewidth=1.5, label='USlow')
ax1.plot(move, up_fast, 'g', linewidth=1.5, label='UFast')
ax1.set_title('Movement')
ax1.legend()

# Turn off top/right axes
for ax in (ax0, ax1):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()
