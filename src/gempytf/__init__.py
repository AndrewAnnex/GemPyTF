"""
Module initialisation for GemPy
Created on 21/10/2016

@author: Miguel de la Varga
"""


import sys

from .core.gempy_api import *
from .plot import plot_api as _plot
from .plot import plot 
from .plot.plot_api import plot_grav

__version__ = '2.1.1'

if __name__ == '__main__':
    pass
