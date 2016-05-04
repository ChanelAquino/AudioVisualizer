import Tkinter as tk
from Tkinter import *
import tkFont

from test_analysis import *

#----------------------------------------#
#----------FONT CUSTOM INFO--------------#
#----------------------------------------#
TITLE_FONT = ('times', 20, "bold")
BUTTON_COLOR = "#1A1511" 
BG_COLOR = "#68625E"
BUTTON_TEXT_COLOR = "#9D958D"
BUTTON_ACTIVE = "#D4D2CF"

song_file = ""
DEFAULT_SONG = "bugs_left_turn.wav"
SONG_1 = "hands_down.wav"
SONG_2 = "return_of_the_mack.wav"
SONG_3 = "going_to_california.wav"


#################################################
class AudioViz(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# container to stack frames on top of each other
		# the desired visible frame will be raised above the others
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		# initialize empty list to hold all frames
		self.frames = {}

		for F in (SongSelection, VisualSelection):
			page_name = F.__name__
			frame = F(container, self)

			# declare elements of frames list
			self.frames[page_name] = frame 

			# all pages in the same location
			frame.grid(row=0, column=0, sticky="nsew") 
			frame.configure(bg=BG_COLOR) 

		# first visible frame
		self.show_page("SongSelection")

	# display SongSelection frame
	def show_page(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()

	#def display_audio_visualizer(self, song):
	#	plotOriginalAudio(song)
#################################################


#################################################
# menu to select song file
class SongSelection(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="Choose a song.", bg=BUTTON_TEXT_COLOR, width="45", height="5", fg=BUTTON_COLOR)
		title.config(font=TITLE_FONT)
		title.pack(side="top", fill="x", pady=10)

		# song1 button
		song1 = tk.Button(self, text="HANDS DOWN", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="10", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: controller.show_page("VisualSelection"))
		# song2 button
		song2 = tk.Button(self, text="RETURN OF THE MACK", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="10", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: controller.show_page("VisualSelection"))

		# song3 button
		song3 = tk.Button(self, text="GOING TO CALIFORNIA", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="10", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: controller.show_page("VisualSelection"))

		# display buttons
		song1.pack()
		song2.pack()
		song3.pack()
#################################################


#################################################
# menu to select audio visualizer method
class VisualSelection(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="Select a visualizer.", bg=BUTTON_TEXT_COLOR, width="45", height="5", fg=BUTTON_COLOR)
		title.config(font=TITLE_FONT)
		title.pack(side="top", fill="x", pady=10)

		# original audio
		orig_audio = tk.Button(self, text="ORIGINAL AUDIO", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: plotOriginalAudio("bugs_left_turn.wav"))

		# audio with hanning window
		audio_hann = tk.Button(self, text="AUDIO WITH HANNING WINDOW", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: plotAudioHanningWindow("bugs_left_turn.wav"))

		# audio normalized with fft
		audio_fft = tk.Button(self, text="AUDIO NORMALIZED WITH FFT", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: plotAudioNormalizedFFT("bugs_left_turn.wav"))

		# audio magnitude values
		audio_mag = tk.Button(self, text="AUDIO MAGNITUDE VALUES", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: plotAudioMagnitudeValues("bugs_left_turn.wav"))

		# button to allow user to select a different song
		change_song = tk.Button(self, text="Select a different song.", fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, width="45", height="4", highlightbackground=BUTTON_COLOR, activebackground=BUTTON_ACTIVE, command=lambda: controller.show_page("SongSelection"))

		orig_audio.pack()
		audio_hann.pack()
		audio_mag.pack()
		audio_fft.pack()
		change_song.pack()
#################################################


#################################################
# run application
if __name__ == "__main__":
	app = AudioViz()
	app.geometry("800x850")
	app.title("Audio Visualizer")
	app.mainloop()
#################################################




