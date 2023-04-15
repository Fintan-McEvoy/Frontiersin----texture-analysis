


#https://scikit-image.org/docs/stable/auto_examples/applications/plot_haar_extraction_selection_classification.html



import cv2
import csv
from csv import writer
import os
import skimage
import skimage.measure


from skimage.io import imread
from skimage import io
from skimage.feature import greycomatrix
from skimage.feature import greycoprops

from skimage.transform import integral_image



home = os.getcwd()

if not os.path.exists(home+'/demo.csv'):
    print('No output file exists, it will be created and called output.csv')
    f = open('output.csv', 'w')
  
    # create the csv writer
    writer_head = csv.writer(f)
    header=['file_name','entropy','ASM','contrast','energy','dissimilarity','correlation','homogeneity','roi_1','roi_3','roi_0','roi_2','dynamic_range','depth','nodule_present','mineralization_present','comment']
    # write the header
    writer_head.writerow(header)

    # close the file
    f.close()



def crop_save_texture(image, image_name):
    roi = cv2.selectROI(image)

    #Crop selected roi from raw image
    roi_cropped = image[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Save the cropped image
    cv2.imwrite((str(image_name)[0:-4]+'_crop'+'.png'), roi_cropped)

    glcm = greycomatrix(roi_cropped, [5], [0], 256, symmetric=True, normed=True)
    ts = []
    us = []
    vs = []
    ws = []
    xs = []
    ys = []
    zs = []
    ts.append(skimage.measure.shannon_entropy(roi_cropped))
    us.append(greycoprops(glcm, 'ASM')[0, 0])    
    vs.append(greycoprops(glcm, 'contrast')[0, 0])
    ws.append(greycoprops(glcm, 'energy')[0, 0])    
    xs.append(greycoprops(glcm, 'dissimilarity')[0, 0])
    ys.append(greycoprops(glcm, 'correlation')[0, 0])
    zs.append(greycoprops(glcm, 'homogeneity')[0, 0])

    feature_type = ['type-2-x', 'type-2-y']
    feature_coord= None

    dr =input("Enter a value for dynamic range: ")
    depth = input("Enter a value image depth: ")
    nodule = input("Enter a value for nodule 1 present zero not present: ")
    mineral = input("Enter a value for mineralization 2 present, zero not present: ")
    comment = input("Enter an optional free text comment: ")

    print("entrophy is {}\n\
    ASM is {}\n\
    Contrast is {}\n\
    Energy is {}\n\
    Dissimilarity is {}\n\
    Correlation is {}\n\
    Homogeneity is {}\n"\
    .format(ts,us,vs,ws,xs,ys,zs))
 
    # List with file and texture data to append to our output file as a new row
    List = [image_name,str(ts)[1:-1],str(us)[1:-1],str(vs)[1:-1],str(ws)[1:-1],str(xs)[1:-1],str(ys)[1:-1],str(zs)[1:-1],int(roi[1]),int(roi[3]),int(roi[0]),int(roi[2]),dr,depth,nodule,mineral,comment] 



    # Open our existing CSV file in append mode
    # Create a file object for this file
    
    #with open('event.csv', 'a') as f_object:
    with open('output.csv', 'a') as f_object:

        
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
 
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
 
        # Close the file object
        f_object.close()


# get a list of file names in the directory "images" so that the code can run  in a loop on each image in the list
dirs=os.listdir(home+'/images/')


#Run the function "crop_save_texture" defined above.  This will append data to the output.csv file and save a  croped image of the region of interest. 
for file in dirs:
    print(home+'/images/'+file)
    image=cv2.imread(home+'/images/'+file,cv2.IMREAD_GRAYSCALE)[:,]
    crop_save_texture(image, file)






