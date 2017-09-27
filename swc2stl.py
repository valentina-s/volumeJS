import sys
"""
    This file converts .swc file to a .stl_file

    Procedure:
    1) set radius to 1 in .swc (otherwise does not work to convert to vtk)
    2) convert swc to vtk using swc2vtk
    3) convert vtk to stl (I don't have this part yet, I am doing it through VisIt)

    Call:
    python swc_file.swc stl_file.stl

"""
swc_filename = sys.argv[1]
stl_filename = sys.argv[2]

import swc2vtk
import pandas as pd
import csv

# set radius to 1
data = pd.read_csv(swc_filename,sep = " ", skiprows = 3, names = ['n','type','x','y','z','radius','parent']) # not reading header
data['radius'] = 1
#swapping axes
# x = data['x'].copy()
# data['x'] = data['y'].copy()
#data['y'] = data['y'][::-1].copy()
data.to_csv('swc_file_radius1.swc', sep = " ", header = None, index = None)

# add back the header
with open('swc_file_radius1.swc', 'r') as no_header: data = no_header.read()

header = ''
with open(swc_filename, 'r') as swc_file:
     for row in swc_file.readlines()[:3]:
         header = header+row

with open('swc_file_radius1.swc', 'w') as modified: modified.write(header + data)


vtkgen = swc2vtk.VtkGenerator()
vtkgen.add_swc('swc_file_radius1.swc')
vtkgen.write_vtk(sys.argv[2])

# need to remove swc_file_radius1.swc
