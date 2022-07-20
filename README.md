# GemPyTF
## Overview
This is a TensorFlow extension of [GemPy](https://github.com/cgre-aachen/gempy) to develop 3D subsurface model while keep tracking the derivatives of the parameters.
## Why TensorFlow
GemPy is the most popular Python-based 3-D structural geological modeling open-source software now, which allows the implicit (i.e. automatic) creation of complex geological models from interface and orientation data. We all love GemPy, however, the installation of [Theano](https://en.wikipedia.org/wiki/Theano_(software)) sometime could be frustrating. Therefore this project aims to extend the backend of GemPy with the modern machine learning package [TensorFlow](https://www.tensorflow.org/) for Automatic Differentiation (AD).

Try the simple demos in colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GeorgeLiang3/GemPyTF/blob/main/GemPyTF_demo.ipynb)

## Installation and dependency
The current version is depend on an older version of GemPy-'2.1.1'

- git clone this repo
- create conda environment `conda env create --name gempytf --file env.yml`
- `pip install -e .`
## Limitations
At the moment there are only limited models are tested (in [Examples](/Examples/)). 

current version has 
- no support for topology
- no support for fault block
- not been tested with topography

### Known bugs to be fixed
- <s>3D color map is in wrong order </s> (fixed)
- <s>2D plot function `show_data` function not correct</s> (fixed)
- Hessian in graph mode is limited
