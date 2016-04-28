import Tkinter as tk
from Tkinter import *
import tkFont

#TODO: change names of functions/methods and variables
#TODO: change color scheme, font faces, etc.
#TODO: plot stuff


#----------------------------------------#
#----------FONT CUSTOM INFO--------------#
#----------------------------------------#
TITLE_FONT = ('times', 20, "bold")
BUTTON_COLOR = "#1A1511" 
BG_COLOR = "#68625E"
BUTTON_TEXT_COLOR = "#9D958D"
BUTTON_HIGHLIGHT = "#D4D2CF"




class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (SongSelection, PageOne, VisualSelection):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
			frame.configure(bg=BG_COLOR) 

		self.show_frame("SongSelection")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class SongSelection(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Choose a song.", bg = BUTTON_TEXT_COLOR, width = "45", height ="5", fg = BUTTON_COLOR)
		label.config(font=TITLE_FONT)

		label.pack(side="top", fill="x", pady=10)

		button1 = tk.Button(self, text="HANDS DOWN",  fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="10", highlightbackground=BUTTON_COLOR, activebackground= BUTTON_HIGHLIGHT, command=lambda: controller.show_frame("VisualSelection"))

		button2 = tk.Button(self, text="RETURN OF THE MACK", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="10", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("VisualSelection"))

		button3 = tk.Button(self, text="TBD", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR, width="45", height="10", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("VisualSelection"))


		button1.pack()
		button2.pack()
		button3.pack()



class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="This is page 1")
		label.config(font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
				           command=lambda: controller.show_frame("StartPage"))
		button.pack()


class VisualSelection(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Select a visualizer.", bg = BUTTON_TEXT_COLOR, width = "45", height ="5", fg = BUTTON_COLOR)
		label.config(font=TITLE_FONT)

		label.pack(side="top", fill="x", pady=10)
		button1 = tk.Button(self, text="METHOD #1",  fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="8", highlightbackground=BUTTON_COLOR, activebackground= BUTTON_HIGHLIGHT, command=lambda: controller.show_frame("VisualSelection"))

		button2 = tk.Button(self, text="METHOD #2", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="8", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("VisualSelection"))

		button3 = tk.Button(self, text="METHOD #3", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("VisualSelection"))

		button4 = tk.Button(self, text="METHOD #4", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR, width="45", height="8", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("VisualSelection"))

		button5 = tk.Button(self, text="Select a different song.", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR, width="45", height="4", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("SongSelection"))

		button1.pack()
		button2.pack()
		button3.pack()
		button4.pack()
		button5.pack()



if __name__ == "__main__":
	app = SampleApp()
	app.geometry("800x850")
	app.mainloop()
	app.title("Audio Visualizer")

