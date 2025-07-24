import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns
# import pandas as pd
# from scipy.optimize import curve_fit
# from scipy.ndimage import gaussian_filter1d
# from scipy.integrate import quad

x=np.linespace(0,10,100)
y=np.sin(x)

plt.plot(x,y)
plt.title('Sine wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
