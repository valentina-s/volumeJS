import sys
from skimage.external.tifffile import imread
from skimage.transform import resize
import nrrd
import numpy as np

infile = sys.argv[1]
outfile = sys.argv[2]
zoom_factor = float(sys.argv[3])

im = np.array(imread(infile)[0])
im_small = resize(im,tuple(np.array(im.shape)*zoom_factor), mode='constant')
print(im_small.shape)
print(im.shape)
nrrd.write(outfile,im_small)
