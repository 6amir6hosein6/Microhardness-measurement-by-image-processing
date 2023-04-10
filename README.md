# Microhardness-measurement-by-image-processing

<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/documentation/image1.png">

Microhardness testing is one of the hardness testing methods that is specifically used. Common examples of microhardness include measuring the hardness of a very small area, obtaining the hardness of a galvanized coating, determining the hardness of the threads of a small screw, measuring the hardness of a microscopic phase, or determining the hardness of a thin clock gear.

Microhardness testing is done by Vickers and Knoop methods. One of the most common standards of these two methods is ASTM E 384. The principles of the micro Vickers test method are the same as the standard Vickers test, with the difference that the applied forces are below one kilogram.


In the Vickers hardness test, a diamond pyramid with a square base is used as a mandrel. The angle between the opposite faces of this pyramid is 136 degrees. The applied load is usually applied between 10 and 15 seconds. The effect of this method is on the square test sample.
<br>
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/documentation/image3.png" width="20%">

In the standard Vickers testing devices, two microscope intraocular blades are embedded. The blades are adjusted to fit right over the edges of the recess. The distance between two blades is read from a scale connected to an eyepiece. The read number is called the optical number and with each testing device there are tables to convert the optical number to the Vickers hardness number for different forces. The optical number can be read with an accuracy of 0.001 mm.

### Vickers hardness calculation formula:

In this formula, VH is the hardness number and a pyramidal diamond-shaped drill bit in kg/mm2, F is the input load in kg, and d is the square diameter of the indentation in mm.

| ![](https://latex.codecogs.com/svg.latex?\Large&space;HV=\frac{F}{A}=\frac{1.8544*F}{d^2}) |
| --- |

The output of the mandrel signal can be seen in the picture below, the pictures below are the pictures taken from the Ness MH4 micro-hardness.
<br>

<p align="center">
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/documentation/image2.png" width="25%">
  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;
  &nbsp; &nbsp; &nbsp;
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/image.jpeg" width="25%" />
</p>

<hr>

### Step 1 :

As we embark on our OpenCV project, the first step will involve enhancing the quality of our images by adjusting their settings. The following changes will be made to achieve this goal:

1. Increase the light balance by 20%
2. Decrease the brightness by 25%
3. Increase the contrast by 10%
4. Increase the saturation by 15%
5. Adjust the temperature by 17%

The temperature adjustment is especially critical to achieving the desired results. The result of these modifications will be a significantly improve0d image, as shown below:


<p align="center">
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/image_edit.jpeg" width="25%" />
  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;
  &nbsp; &nbsp; &nbsp;
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/image_edit2.jpeg" width="25%" />
</p>

### Step 2 :

After adjusting the settings of our image as outlined in the previous step, the next phase of our OpenCV project involves thresholding. Applying thresholding to the image will result in the following output:
<p align="center">
<img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/threshed_image.jpeg" width="25%" />
</p>

### Step 3 :

With the thresholded image produced in the previous step, we now move on to the next stage of our OpenCV project. The goal of this step is to reduce noise and smooth out the image. To achieve this, we will apply a technique known as blurring. After blurring the thresholded image, we will perform buffering to enhance the edges and contours in the image. These processes will result in a cleaner and more polished image.

<p align="center">
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/threshed_image_unnoised.jpeg" width="25%" />
  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/threshed_image_unnoised_smooth.jpeg" width="25%" />
</p>

### Step 4 :

In this phase of our OpenCV project, we will obtain the contours of the image produced in the previous step. After obtaining the contours, we will then extract the sharp points of those contours.

<p align="center">
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/contours.jpeg" width="25%" />
  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/corner_detection.jpeg" width="25%" />
</p>

### Step 4 :

we will draw a line between the detected sharp points and superimpose it on the original image.

<p align="center">
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/final_image.jpeg" width="25%" />
  &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; 
    <img src="https://github.com/6amir6hosein6/Microhardness-measurement-by-image-processing/blob/main/final_image2.jpeg" width="25%" />
</p>





