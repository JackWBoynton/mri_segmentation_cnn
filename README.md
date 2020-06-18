# Fully Convolutional Network Architecture for the Automation of MR Image Segmentation

## load data
* load_dicom
    * loads all the .dcm files in a filepath into a np.ndarray
* load_nrrd
    * loads a single .nrrd file from filepath into a np.ndarray
    * optionally returns the header information

## Network Architecture and Ideas:
* Fully Convolutional Network
* Mark regions that are somewhat uncertain
    * Use Seg3D2 or own simple verification application
    * Different mask for each tissue + different mask for uncertain tissues
    * Re-trainable with new data -> after manual verification


## Issues:
* Output format?
* Prevent [Catastrophic Forgetting](https://en.wikipedia.org/wiki/Catastrophic_interference)
* Keep lr ```python currentLearningRate = K.get_value(model.optimizer.lr)```