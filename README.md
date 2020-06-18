# mri_segmentation_cnn

## load data
* .mat -> .npy ?
* direct DICOM (DCM) loading ?
* util
    * -> load_dicom
        * loads all the .dcm files in a filepath into a np.ndarray
    * -> load_nrrd
        * loads a single .nrrd file from filepath into a np.ndarray
        * optionally returns the header information

