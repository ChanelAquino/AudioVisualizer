from scipy.io.wavfile import read

import matplotlib.pyplot as plt

# read audio samples
input_data = read("C:\cst205\Project3\\bugs_left_turn.wav")
audio = input_data[1]

# plot the first 1024 samples
plt.plot(audio[0:1024])

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

# set the title
plt.title("Left Turn at Albuquerque")

# display the plot
plt.show()