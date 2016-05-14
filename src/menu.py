import Tkinter as tk
from Tkinter import *
from Tkinter import Canvas

from sound_analysis_bokeh import *
import sound_analysis_bokeh as bkPlot

from sound_analysis_matplotlib import *
import sound_analysis_matplotlib as mpPlot

#----------------------------------------#
#----------FONT CUSTOM INFO--------------#
#----------------------------------------#
TITLE_FONT = ("AppleGothic", 85, "bold")
BUTTON_FONT = ("AppleGothic", 35)
SMALL_FONT = ("AppleGothic", 20)
BUTTON_COLOR = "#607D8B" # accent color: gray blue
BG_COLOR = "#212121" # primary color: matte black
TEXT_COLOR = "#F5F5F5" # primary text: beige gray

#--------------------------#
#------GLOBAL STRINGS------#
#--------------------------#
song_file = "" 
style_string = ""
plot_style = ""

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

		for F in (WelcomeScreen, SongSelect, ColorSelect, StyleSelect, PlotSelect, VisualSelectBokeh, VisualSelectMPL):
			page_name = F.__name__
			frame = F(container, self)

			# declare elements of frames list
			self.frames[page_name] = frame 

			# all pages in the same location
			frame.grid(row=0, column=0, sticky="nsew") 
			frame.configure(bg=BG_COLOR) 

		# first visible frame
		self.show_welcome()

	# display WelcomeScreen
	def show_welcome(self):
		global song_file 
		song_file = ""

		global style_string
		style_string = ""
		
		frame = self.frames["WelcomeScreen"]
		frame.tkraise()

	# display SongSelect frame
	def show_song_menu(self):
		frame = self.frames["SongSelect"]
		frame.tkraise()

	# display ColorSelect frame
	def show_color_menu(self, song):
		global song_file 
		song_file = song

		frame = self.frames["ColorSelect"]
		frame.tkraise()

	# display StyleSelect frame
	def show_style_menu(self, color):
		global style_string
		style_string += color

		frame = self.frames["StyleSelect"]
		frame.tkraise()

	# display PlotSelect frame
	def show_plot_frame(self, shape):
		global style_string
		style_string += shape

		frame = self.frames["PlotSelect"]
		frame.tkraise()

	# display VisualSelectionBokeh frame
	def show_visualBokeh_menu(self):
		frame = self.frames["VisualSelectBokeh"]
		frame.tkraise()	

	# display VisualSelectionMPL frame
	def show_visualMPL_menu(self):
		frame = self.frames["VisualSelectMPL"]
		frame.tkraise()	


	
#################################################


#################################################
# welcome screen
class WelcomeScreen(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# title aesthetics
		title = tk.Label(self, text="Audio\nVisualizer", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# enter button
		enter = tk.Button(self, text="ENTER", padx="20", pady="5", highlightthickness="0", fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_song_menu())
		enter.config(font=BUTTON_FONT)
		enter.place(relx=0.5, rely=0.625, anchor=CENTER)
		
#################################################


#################################################
# menu to select song file
class SongSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="Song?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# song1 button
		song1 = tk.Button(self, text="Hands Down", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_color_menu("../wav/hands_down.wav"))
		song1.config(font=BUTTON_FONT)

		# song2 button
		song2 = tk.Button(self, text="Return of the Mack", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_color_menu("../wav/return_of_the_mack.wav"))
		song2.config(font=BUTTON_FONT)

		# song3 button
		song3 = tk.Button(self, text="Going to California", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_color_menu("../wav/going_to_california.wav"))
		song3.config(font=BUTTON_FONT)

		# song4 button
		song4 = tk.Button(self, text="Bugs Bunny", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_color_menu("../wav/bugs_left_turn.wav"))
		song4.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0",  fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		# display buttons
		song1.pack()
		song2.pack()
		song3.pack()
		song4.pack()
		start_over.pack()
#################################################


#################################################
# ask user to select color of plot
class ColorSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		# title aesthetics
		title = tk.Label(self, text="Color?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# cyan
		cyan = tk.Button(self, text="Cyan", width="15",  highlightthickness="0",  fg="#00ffff", background=BG_COLOR,highlightbackground="#00ffff", highlightcolor=BG_COLOR, command=lambda: controller.show_style_menu('c'))
		cyan.config(font=BUTTON_FONT)

		# magenta
		magenta = tk.Button(self, text="Magenta", width="15",  highlightthickness="0",  fg="#ff00ff", background=BG_COLOR, activebackground=BG_COLOR, highlightbackground="#ff00ff", highlightcolor=BG_COLOR, command=lambda: controller.show_style_menu('m'))
		magenta.config(font=BUTTON_FONT)

		# green
		green = tk.Button(self, text="Green", width="15",  highlightthickness="0",  fg="#009900", background=BG_COLOR, activebackground=BG_COLOR, highlightbackground="#009900", highlightcolor=BUTTON_COLOR, command=lambda: controller.show_style_menu('g'))
		green.config(font=BUTTON_FONT)

		# black
		black = tk.Button(self, text="Black", width="15", highlightthickness="0",  fg="#000000", background=BG_COLOR, activebackground=BG_COLOR, highlightbackground="#000000", highlightcolor=BUTTON_COLOR, command=lambda: controller.show_style_menu('k'))
		black.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0", fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		cyan.pack()
		magenta.pack()
		green.pack()
		black.pack()
		start_over.pack()
#################################################


#################################################
# ask user to select style of plot
class StyleSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="Style?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# solid line
		solid_line = tk.Button(self, text="Solid Line", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_plot_frame('--'))
		solid_line.config(font=BUTTON_FONT)

		# star
		star = tk.Button(self, text="Star", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_plot_frame('*'))
		star.config(font=BUTTON_FONT)

		# circle
		circle = tk.Button(self, text="Circle", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_plot_frame('o'))
		circle.config(font=BUTTON_FONT)


		# triangle
		triangle = tk.Button(self, text="Triangle", width="15", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_plot_frame('v'))
		triangle.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0",  fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		solid_line.pack()
		star.pack()
		circle.pack()
		triangle.pack()
		start_over.pack()
#################################################


#################################################
# menu to select Bokeh or matplotlib
class PlotSelect(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		
		# title aesthetics
		title = tk.Label(self, text="Plot Method?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# plot_bokeh
		plot_bokeh = tk.Button(self, text="Bokeh", width="10", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_visualBokeh_menu())
		plot_bokeh.config(font=BUTTON_FONT)

		# plot_matplotlib
		plot_matplotlib = tk.Button(self, text="matplotlib", width="10", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_visualMPL_menu())
		plot_matplotlib.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0",  fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		plot_bokeh.pack()
		plot_matplotlib.pack()
		start_over.pack()
#################################################


#################################################
# menu to select audio visualizer method w/ Bokeh
class VisualSelectBokeh(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		global song_file

		# title aesthetics
		title = tk.Label(self, text="Visualizer?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# original audio
		orig_audio = tk.Button(self, text="Signal Wave", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: bkPlot.plotSignalWave(song_file, style_string))
		orig_audio.config(font=BUTTON_FONT)

		# audio with hanning window
		audio_hann = tk.Button(self, text="Hanning Window", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: bkPlot.plotAudioHanningWindow(song_file, style_string))
		audio_hann.config(font=BUTTON_FONT)

		# audio normalized with fft
		audio_fft = tk.Button(self, text="Fast Fourier Transform", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: bkPlot.plotAudioNormalizedFFT(song_file, style_string))
		audio_fft.config(font=BUTTON_FONT)

		# audio magnitude values
		audio_mag = tk.Button(self, text="Magnitude Values", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: bkPlot.plotAudioMagnitudeValues(song_file, style_string))
		audio_mag.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0",  fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		orig_audio.pack()
		audio_hann.pack()
		audio_fft.pack()
		audio_mag.pack()
		start_over.pack()
#################################################


#################################################
# menu to select audio visualizer method with matplotlib
class VisualSelectMPL(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		# title aesthetics
		title = tk.Label(self, text="Visualizer?", bg=BG_COLOR, width="45", fg="#fff")
		title.config(font=TITLE_FONT)
		title.pack()

		# original audio
		orig_audio = tk.Button(self, text="Signal Wave", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: mpPlot.plotSignalWave(song_file, style_string))
		orig_audio.config(font=BUTTON_FONT)

		# audio with hanning window
		audio_hann = tk.Button(self, text="Hanning Window", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: mpPlot.plotAudioHanningWindow(song_file, style_string))
		audio_hann.config(font=BUTTON_FONT)

		# audio normalized with fft
		audio_fft = tk.Button(self, text="Fast Fourier Transform", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: mpPlot.plotAudioNormalizedFFT(song_file, style_string))
		audio_fft.config(font=BUTTON_FONT)

		# audio magnitude values
		audio_mag = tk.Button(self, text="Magnitude Values", width="20", highlightthickness="0",  fg=BG_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: mpPlot.plotAudioMagnitudeValues(song_file, style_string))
		audio_mag.config(font=BUTTON_FONT)

		# button to allow user to start over
		start_over = tk.Button(self, text="Start Over", width="15", highlightthickness="0",  fg=BUTTON_COLOR, activeforeground=BUTTON_COLOR, background=BG_COLOR, activebackground=BG_COLOR, highlightbackground=BUTTON_COLOR, highlightcolor=BUTTON_COLOR, command=lambda: controller.show_welcome())
		start_over.config(font=SMALL_FONT)

		orig_audio.pack()
		audio_hann.pack()
		audio_fft.pack()
		audio_mag.pack()
		start_over.pack()
#################################################


#################################################
# run application
if __name__ == "__main__":
	app = AudioViz()
	app.geometry("600x700")
	app.title("Audio Visualizer")
	app.mainloop()
#################################################




