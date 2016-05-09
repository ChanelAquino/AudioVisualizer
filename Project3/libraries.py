# sound_analysis.py
import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft, fft
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
