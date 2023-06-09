from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.layouts import row
from bokeh.models import Button

import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)

source = ColumnDataSource(data={'x': x, 'y': y})

plot = figure(title='Bokeh Server Scatter Plot', x_axis_label='X', y_axis_label='Y')
plot.circle('x', 'y', source=source, size=10, color='blue', alpha=0.5)

def update():
    new_data = {'x': source.data['x'] + [np.random.randn()],
                'y': source.data['y'] + [np.random.randn()]}
    source.data = new_data

button = Button(label='Add Point')
button.on_click(update)

layout = row(plot, button)

curdoc().add_root(layout)
