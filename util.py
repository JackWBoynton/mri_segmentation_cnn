import vtk
from vtk.util import numpy_support
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import os
import nrrd

def load_dicom(path: str) -> np.ndarray:
    """takes a filepath that contains DICOM image files (.dcm) and returns an h x w x n numpy array containing the pixel data"""
    
    # initialize DICOM reader from vtk module
    reader = vtk.vtkDICOMImageReader()
    reader.SetDirectoryName(path)
    reader.Update()

    # Load dimensions
    _extent = reader.GetDataExtent()
    px_dims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

    # Load spacing values
    px_space = reader.GetPixelSpacing()

    # bounding axes
    x = np.arange(0.0, (px_dims[0]+1)*px_space[0], px_space[0])
    y = np.arange(0.0, (px_dims[1]+1)*px_space[1], px_space[1])
    z = np.arange(0.0, (px_dims[2]+1)*px_space[2], px_space[2])

    # Get the image data
    img_dat = reader.GetOutput()
    # Get the point data
    pt_dat = img_dat.GetPointData()
    # Get the actual point data from the vtk object
    dat = pt_dat.GetArray(0)

    # Convert the vtk to numpy array
    dicom = numpy_support.vtk_to_numpy(dat)
    # Reshape the numpy array to 3D using 'ConstPixelDims' as a 'shape'
    dicom = dicom.reshape(px_dims, order='F')

    return dicom

def load_nrrd(filename: str, header: bool = False) -> np.ndarray:
    """reads a nrrd file located at filename into a numpy ndarray. if header is True, will return header information"""

    readdata, headera = nrrd.read(filename)
    if header:
        return readdata, headera
    return readdata
