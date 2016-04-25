from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft, fft
import matplotlib.pyplot as plt
import scipy
import numpy as np


#-------------------------------------------#
#---------CUSTOM INFO FOR subplot()---------#
#-------------------------------------------#
numRows = 4
numCols = 1

fig = plt.subplots(nrows = 4, ncols = 1)
plt.tight_layout()	# create space between subplots
plt.title("Left Turn At Alburqueque")

#-------------------------------------------#
#---------AUDIO SAMPLES INFORMATION---------#
#-------------------------------------------#

#-------- audio INFORMATION --------#
input_data = read("bugs_left_turn.wav")
audio = input_data[1]
audio = audio[0:1024] 	# first 1024 samples

# plot figure 1
plt.figure(1)	# the first figure			
plt.subplot(numRows, numCols, 1)	
plt.title("Original Audio")
plt.xlim([0, 1024])	
plt.plot(audio, 'b')


#-------- audioHann INFORMATION --------#
window = hann(1024)			# compute a 1024-point Hanning window
audioHann = audio * window	# apply window to audio

# plot figure 2
plt.subplot(numRows, numCols, 2)
plt.title("Audio with Hanning Window")
plt.xlim([0, 1024])				
plt.plot(audioHann, 'c') 


#-------- magnitudeValues INFORMATION --------#
magnitudeValues = abs(rfft(audio))	# fft
magnitudeValues = 20 * scipy.log10(magnitudeValues)	# convert to a decibel scale
magnitudeValues -= max(magnitudeValues)	# normalize to have a maximum value of 0 dB

# plot figure 3
plt.subplot(numRows, numCols, 3)
plt.title("Normalized with FFT")
plt.xlim([0, 1024])	
plt.plot(magnitudeValues, 'r')


#-------- other INFORMATION --------#
duration = len(audio)
k = np.arange(duration)	# returns values up to duration
T = duration/44100.0
freq = k/T	# two sides frequency
#freq = freq[range(duration/2)]	# one side frequency
Y = fft(audio)/duration	# fft computing and normalizing
Y = Y[range(duration/2)]

# plot figure 4
plt.subplot(numRows, numCols, 4)
plt.title("Other")
plt.xlim([0, 500])	
plt.ylim([0,5])
plt.plot(abs(Y), 'm')


# display the plot
plt.show()
'''
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")

# set the title
plt.title("Left Turn at Albuquerque")
'''


