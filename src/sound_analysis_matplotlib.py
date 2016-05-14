from libraries import *

#################################################
def plotSignalWave(song_file, style):
	# open .wav file
	sound_wave = wave.open(song_file, 'r')
	
	# extract raw audio from .wav file
	signal = sound_wave.readframes(-1)
	signal = np.fromstring(signal, 'Int16')

	# frame rate of .wav file
	frame_rate = sound_wave.getframerate()

	# time vector spaced linearly with
	# the size of the audio file
	Time = np.linspace(0, len(signal)/frame_rate, num = len(signal))

	# plot Time versus signal
	plt.title("Signal Wave")
	plt.plot(Time, signal, style)
	plt.show()
	return ''
#################################################


#################################################
def plotAudioHanningWindow(song_file, style):
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
	plt.plot(audioHann, style)
	plt.show()
	return ''
#################################################


#################################################
def plotAudioNormalizedFFT(song_file, style):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]

	duration = len(audio)
	audioFFT = fft(audio)/duration	# fft computing and normalizing
	audioFFT = audioFFT[range(duration/2)]

	# plot audioFFT
	plt.title("Audio Normalized with FFT")
	plt.plot(abs(audioFFT), style)
	plt.show()
	return ''
#################################################


#################################################
def plotAudioMagnitudeValues(song_file, style):
	# read in sound file; get first 1024 samples
	input_data = read(song_file)
	audio = input_data[1]

	# compute a 1024-point Hanning window;
	# apply window to audio
	window = hann(1024)
	audio = audio[0:1024] * window

	# compute and normalize magnitude values
	magnitudeValues = abs(rfft(audio))	# fft
	magnitudeValues = 20 * scipy.log10(magnitudeValues)	# convert to a decibel scale
	magnitudeValues -= max(magnitudeValues)	# normalize to have a maximum value of 0 dB 

	# plot magnitudeValues
	plt.title("Audio Magnitude Values")
	plt.xlim([0, 1024]) # x-axis range
	plt.plot(magnitudeValues, style)
	plt.show()
	return ''
#################################################




