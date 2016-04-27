from bokeh.plotting import figure, output_file, show
from scipy.io.wavfile import read

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]



#-------- audio INFORMATION --------#
input_data = read("bugs_left_turn.wav")
audio = input_data[1]
audio = audio[0:1024] 	# first 1024 samples
print(audio[0:20])

# output to static HTML file
output_file("lines.html", title="line plot example")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Temp.", line_width=2)

# show the results
show(p)