import vtk
from vtk.util import numpy_support
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import os

def load_dicom(path: str) -> np.ndarray:
    """takes a filepath that contains DICOM image files (.dcm) and returns an h x w x n numpy array containing the pixel data"""
    
    reader = vtk.vtkDICOMImageReader()
    reader.SetDirectoryName(path)
    reader.Update()

    # Load dimensions using `GetDataExtent`
    _extent = reader.GetDataExtent()
    px_dims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

    # Load spacing values
    px_space = reader.GetPixelSpacing()

    x = np.arange(0.0, (px_dims[0]+1)*px_space[0], px_space[0])
    y = np.arange(0.0, (px_dims[1]+1)*px_space[1], px_space[1])
    z = np.arange(0.0, (px_dims[2]+1)*px_space[2], px_space[2])

    # Get the 'vtkImageData' object from the reader
    img_dat = reader.GetOutput()
    # Get the 'vtkPointData' object from the 'vtkImageData' object
    pt_dat = img_dat.GetPointData()
    # Ensure that only one array exists within the 'vtkPointData' object
    assert (pt_dat.GetNumberOfArrays()==1)
    # Get the `vtkArray` (or whatever derived type) which is needed for the `numpy_support.vtk_to_numpy` function
    dat = pt_dat.GetArray(0)

    # Convert the `vtkArray` to a NumPy array
    dicom = numpy_support.vtk_to_numpy(dat)
    # Reshape the NumPy array to 3D using 'ConstPixelDims' as a 'shape'
    dicom = dicom.reshape(px_dims, order='F')

    return dicom