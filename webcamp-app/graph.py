from motion import df
from bokeh.plotting import figure, show, output_file

p=figure(x_axis_type="datetime", height=100, width=500, sizing_mode="scale_both", title="Motion Graph")

# Quad Left Right Bottom Top
q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1, color="green")

output_file("data/graph.html")

show(p)