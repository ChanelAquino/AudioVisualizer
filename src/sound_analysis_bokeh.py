from libraries import *

#################################################
def plotSignalWave(song_file, style):
    # read audio samples
    input_data = read(song_file)
    audio = input_data[1]

    x = []
    x.extend(range(0, len(audio)))
    showBokeh("Signal Wave", style, x, audio)
#################################################


#################################################
def plotAudioHanningWindow(song_file, style):
    # read audio samples
    input_data = read(song_file)
    audio = input_data[1]

    # apply a Hanning window
    window = hann(1024)
    audio = audio[0:1024] * window

    mags = abs(rfft(audio)) # fft
    mags = 20 * scipy.log10(mags)   # convert to dB
    mags -= max(mags)   # normalise to 0 dB max

    x = []
    x.extend(range(0, len(mags)))
    showBokeh("Hanning Window", style, x, mags)
#################################################


#################################################
def plotAudioNormalizedFFT(song_file, style):
    # read audio samples
    input_data = read(song_file)
    audio = input_data[1]
    
    duration = len(audio)   # duration of audio
    audioFFT = fft(audio)/duration  # fft computing and normalizing
    audioFFT = audioFFT[range(duration/2)]
    audioFFT = audioFFT[1:]

    x = []
    x.extend(range(0,len(audioFFT)))
    showBokeh("Normalized FFT", style, x, abs(audioFFT))
#################################################


#################################################
def plotAudioMagnitudeValues(song_file, style):
    # read in sound file; get first 1024 samples
    input_data = read(song_file)
    audio = input_data[1]
    audio = audio[0:1024]

    # compute and normalize magnitude values
    magnitudeValues = abs(rfft(audio))  # fft
    magnitudeValues = 20 * scipy.log10(magnitudeValues)  # convert to a decibel scale
    magnitudeValues -= max(magnitudeValues)  # normalize to have a maximum value of 0 dB

    x = []
    x.extend(range(0, len(magnitudeValues)))
    showBokeh("Magnitude Values", style, x, magnitudeValues)
#################################################


#################################################
def returnNewFigure(title):
    # create a new plot with a title and axis labels
    return figure(title=title, x_axis_label='time', y_axis_label='amplitude', toolbar_location="above",
               tools="xwheel_zoom, pan, box_select, box_zoom, lasso_select, reset")
#################################################


#################################################
def showBokeh(title, style, x, y):
    output_file("bokeh_audio_plot.html", title=title)
    p = returnNewFigure(title)
    
    color_string = style[0]
    colorDict = {"c": "cyan", "m": "magenta", "g": "green", "b": "black"}
    color = colorDict[color_string]

    shape = style[1]
    if shape == "*":
        p.asterisk(x, y, line_width=2, color=color, fill_color="black", size=6)

    if shape == "-":
        p.line(x,y, line_width=2, line_color=color,)

    if shape == "o":
        p.circle(x, y, line_width=2, color=color, fill_color="black", size=6)

    if shape == ",":
        p.triangle(x, y, line_width=2, color=color, fill_color="black", size=6)

    show(p)
#################################################