from libraries import *

#################################################
def plotOriginalAudio(song_file):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]
	audio = audio[0:1024]

	# plot audio
	plt.title("Original Audio")
	plt.xlim([0, 1024]) # x-axis range
	plt.plot(audio)
	plt.show()
#################################################

#################################################
def plotAudioHanningWindow(song_file):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]
	audio = audio[0:1024]

	# compute a 1024-point Hanning window;
	# apply window to audio
	window = hann(1024)
	audioHann = audio * window

	# plot audioHann
	plt.title("Audio with Hanning Window")
	plt.xlim([0, 1024]) # x-axis range
	plt.plot(audioHann)
	plt.show()
#################################################

#################################################
def plotAudioNormalizedFFT(song_file):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]
	audio = audio[0:1024]

	duration = len(audio)
	audioFFT = fft(audio)/duration	# fft computing and normalizing
	audioFFT = audioFFT[range(duration/2)]

	# plot audioFFT
	plt.title("Audio Normalized with FFT")
	plt.xlim([0, 500]) # x-axis range
	plt.ylim([0,5])	# y-axis range
	plt.plot(abs(audioFFT))
	plt.show()
#################################################

#################################################
def plotAudioMagnitudeValues(song_file):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]
	audio = audio[0:1024]

	# compute and normalize magnitude values
	magnitudeValues = abs(rfft(audio))	# fft
	magnitudeValues = 20 * scipy.log10(magnitudeValues)	# convert to a decibel scale
	magnitudeValues -= max(magnitudeValues)	# normalize to have a maximum value of 0 dB 

	# plot magnitudeValues
	plt.title("Audio Magnitude Values")
	plt.xlim([0, 1024]) # x-axis range
	plt.plot(magnitudeValues)
	plt.show()
#################################################




