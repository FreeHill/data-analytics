import numpy as np
import matplotlib.pyplot as plot

axes_values = np.arange(-100, 100, 10)
dx, dy = np.meshgrid(axes_values, axes_values)
print(dx, dy)

function = 2 * dx + 3 * dy
function_2 = np.cos(dx) + np.cos(dy)
print(function)

plot.imshow(function)
# plot.imshow(function_2)
plot.title("Function of plot 2*dx+3*dy")
# plot.title("Function of cosine plot")
plot.colorbar()
plot.savefig('myfig.png')
# plot.savefig('myfig2.png')