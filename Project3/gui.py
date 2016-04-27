import Tkinter as tk
from Tkinter import *
import tkFont

#----------------------------------------#
#----------FONT CUSTOM INFO--------------#
#----------------------------------------#
TITLE_FONT = ("Helvetica", 45, "bold")
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
		for F in (StartPage, PageOne, PageTwo):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
			frame.configure(bg=BG_COLOR) 

		self.show_frame("StartPage")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Choose a song.", bg = BUTTON_TEXT_COLOR, width = "45", height ="5", fg = BUTTON_COLOR, font=TITLE_FONT)

		label.pack(side="top", fill="x", pady=10)

		button1 = tk.Button(self, text="HANDS DOWN",  fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="10", highlightbackground=BUTTON_COLOR, activebackground= BUTTON_HIGHLIGHT, command=lambda: controller.show_frame("PageOne"))

		button2 = tk.Button(self, text="RETURN OF THE MACK", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR,  width="45", height="10", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("PageTwo"))

		button3 = tk.Button(self, text="TBD", fg = BUTTON_TEXT_COLOR, bg = BUTTON_COLOR, width="45", height="10", highlightbackground=BUTTON_COLOR,  activebackground= BUTTON_HIGHLIGHT, 
				            command=lambda: controller.show_frame("PageTwo"))


		button1.pack()
		button2.pack()
		button3.pack()



class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
				           command=lambda: controller.show_frame("StartPage"))
		button.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Go to the start page",
				           command=lambda: controller.show_frame("StartPage"))
		button.pack()



if __name__ == "__main__":
	app = SampleApp()
	app.geometry("800x850")
	app.mainloop()

