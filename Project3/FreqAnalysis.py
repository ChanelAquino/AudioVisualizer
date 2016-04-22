from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# read audio samples
input_data = read("bugs_left_turn.wav")
audio = input_data[1]

'''
subplot(numrows, numcols, fignum)
  where fignum ranges from 1 to numrows * numcols;
  commas optional so subplot(211) is equal to subplot (2, 1, 1)
'''

# plot the first 1024 sample
plt.figure(1)					# the first figure
plt.subplot(3, 1, 1)			# the first subplot in the first figure
plt.plot(audio[0:1024], 'b:')	# 'b:' indicates blue dotted lines

plt.subplot(3, 1, 2)			# the second subplot in the first figure
plt.plot(audio[1025:2048], 'm,')# 'm,' indicates magenta pixels

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

'''
# set the title
plt.title("Left Turn at Albuquerque")
'''

# display the plot
plt.show()
