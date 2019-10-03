import os
import sys
import scipy.io
import scipy.misc
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from PIL import Image
from nst_utils import load_vgg_model
import numpy as np
import tensorflow as tf
import imageio

#%matplotlib inline can only be used in ipython command line not in a python script
#get_ipython().run_line_magic('matplotlib', 'inline') To be removed

#Loading the pre-trained VGG weights (Model)

model = load_vgg_model("imagenet-vgg-verydeep-19.mat")
print(model)
#content_image = imageio.imread("louvre.jpg")
#imshow(content_image)
