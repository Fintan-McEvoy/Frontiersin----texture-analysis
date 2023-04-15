# Frontiersin----texture-analysis
Material to accompany the Frontiers in Veterinary Science paper -- A survey of testicular texture on canine ultrasound images

This code in thid repository on Python 3 and accompanies the paper "A survey of testicular texture on canine ultrasound images" Submitted to Frontiers in Veterinary Science",  Panida Pongvittayanon et al., 2023.

If the Jupyter notebook ("texture.ipynb") is run on a local machine, the notebook file "texture.ipynb" and the directory "images", containing one or more images files (in "png" format) should be present in the same directory. The code will generate an output file called "output.csv" containing the texture analysis results and a "png" image file that shows the ROI selected data.

If the python script ("texture.py") is run, again the script file and the directory "images", containing one or more image files (in "png" format) should be present in the same directory.

The Python environment should be Python version 3.  The code requires that the following modules are installed:
cv2, csv, os, and skimage.
