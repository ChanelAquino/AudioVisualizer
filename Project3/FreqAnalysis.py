from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# read audio samples
input_data = read("bugs_left_turn.wav")
audio = input_data[1]

'''
SYNTAX FOR subplot()
	subplot(numrows, numcols, fignum)
	where fignum ranges from 1 to numrows * numcols;
	commas optional so subplot(211) is equal to subplot (2, 1, 1)
'''

''' PLOT THE FIRST 1024 SAMPLES '''
# the first figure
plt.figure(1)

# the first subplot in the first figure					
plt.subplot(3, 1, 1)		

# 'b:' indicates blue dotted lines	
plt.plot(audio[0:1024], 'b:')	

''' PLOT SAMPLES 1025 TO 2048 '''
# the second subplot in the first figure
plt.subplot(3, 1, 2)			

# 'm,' indicates magenta pixels
plt.plot(audio[1025:2048], 'm,')

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

'''
# set the title
plt.title("Left Turn at Albuquerque")
'''

# display the plot
plt.show()
