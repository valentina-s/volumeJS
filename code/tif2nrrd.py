"""
    tif2nrrd.py converts tif format to nrrd for slice visualization.
    It provides the option to to downsample the image.

    Usage:
    python tif2nrrd infile.tif outfile.nrrd 0.25

    The downsampling factor above is 0.5.
"""

import sys
from skimage.external.tifffile import imread
from skimage.transform import resize
import nrrd
import numpy as np

infile = sys.argv[1]
outfile = sys.argv[2]

if len(sys.argv)<4:
    zoom_factor = 1
else:
    zoom_factor = float(sys.argv[3])

im = np.array(imread(infile)[0])
im_small = resize(im,tuple(np.array(im.shape)*zoom_factor), mode='constant')
print('Original image dimensions: '+ str(im.shape))
print('Downsampled image dimensions: '+ str(np.squeeze(im_small).shape))
nrrd.write(outfile,np.squeeze(im_small))
