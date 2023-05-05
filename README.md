traffic_signs is a class that helps in processing traffic signs images and pasting them onto background images.

# Initialization

When initializing an object of this class, the constructor takes a filename as an argument that should contain an image of a traffic sign. The image is loaded using OpenCV and is then resized to either 450x450 or 900x900 depending on the size of the input image.

# Methods
1. ToGray()
This method converts the input image to grayscale and returns the grayscale image.
this function for :

- Highlight image features: In many cases, the color in an image can be a distraction and make it difficult to see important image features. By converting the image to grayscale, we can focus on the texture, shape, and other features of the image .

- Reduce noise: Grayscale images tend to have less noise than color images.

2. FindEdges()
This method performs Canny edge detection on the grayscale image and returns the dilated edges.

-  Dilating the edges means expanding or thickening them to make them more prominent and better defined.

- to identify boundaries and shapes within an image. Edge detection algorithms highlight the regions of an image where there is a significant change in the intensity or color of adjacent pixels. These regions correspond to object boundaries or features in the image.

3. Thinning()
This method applies thinning to the dilated edges using the ximgproc module of OpenCV and returns the thinned image.

- Thinning is a process in image processing that aims to reduce the thickness of foreground objects in an image to a skeletonized representation. It is useful for various applications such as character recognition, pattern recognition

4. FindContoursArea()
This method finds contours on the thinned image using OpenCV's findContours function and then returns the contour with the maximum area.

- To find the area of the contours in an image. Contours are defined as the boundaries of an object in an image

5. RemoveBackground()
This method removes the background of the input image by creating a black mask of the same dimensions as the original image and then drawing the contour found in the previous step on the mask. Finally, the mask is applied to the original image using bitwise_and to remove the background.

6. FadeImage()
This method removes the background of the input image using the RemoveBackground method and then applies a fade effect to the image by increasing the alpha value of the RGB channels and decreasing the alpha value of the alpha channel. The image is returned with a new alpha channel containing the fade effect.

7. FadedToRmoveBlackBackground()
This method removes the black background of the faded image by creating a mask where black pixels have a value of 0 and non-black pixels have a value of 255. The original image is then merged with the mask to remove the black background.

8. PasteOnBackground(background_path)
This method pastes the traffic sign image onto a random location on a background image. The method takes the path of the background image as an argument. The method first loads the background image and then calls the FadedToRmoveBlackBackground method to remove the black background of the faded image. A random location is generated to paste the image, and a mask is created for the image. The image is blended with the background using the mask to create a final image. The final image is then returned.

# steps

## Gray
![Gray](https://github.com/AbdullahaJ2000/forme/blob/main/steps/gray.png?raw=true)
### 2)Gray_blur
![Gray_blur](https://github.com/AbdullahaJ2000/forme/blob/main/steps/gray_blur.png?raw=true)
### 3)Edges
![Edges](https://github.com/AbdullahaJ2000/forme/blob/main/steps/edges.png?raw=true)
## 4)Dilated_edges
![Dilated_edges](https://github.com/AbdullahaJ2000/forme/blob/main/steps/dilated_edges.png?raw=true)
## 5)Thinning
![Thinning](https://github.com/AbdullahaJ2000/forme/blob/main/steps/thinned_img.png?raw=true)
## 6)mask
![mask](https://github.com/AbdullahaJ2000/forme/blob/main/steps/mask.png?raw=true)
## 7)RemoveBackground
![RemoveBackground](https://github.com/AbdullahaJ2000/forme/blob/main/steps/RemoveBackground.png?raw=true)
## 8)FadedToRmoveBlackBackground
![FadedToRmoveBlackBackground](https://github.com/AbdullahaJ2000/forme/blob/main/steps/FadedToRmoveBlackBackground.png?raw=true)
## 9)Faded_Img
![Faded_Img](https://github.com/AbdullahaJ2000/forme/blob/main/steps/faded_img.png?raw=true)
## 10) Past_on_background_image 
![Past_on_background_image](https://github.com/AbdullahaJ2000/forme/blob/main/Final_output/final_result.png?raw=true)

# Recommendations 

In this class we only focused on Image processing approach but we can find better way using machine/deep learning approach or if we have image for all traffic signs such as :

- If we have data then we can train a CNN , DNN to detect the traffic sign from image.

- Using pre-training model as " Haar Cascade " which its learn and detect objects in an image.

- If we have clear images for all traffic sign then when we detect the traffic sign we can crop it then using Image Similarity then classify it by the ratio value.

- If we have an "file.xml" that have the details for all traffic sign then we can use it to find it.

- using "rembg" which is a Python library used for removing image backgrounds using machine learning models. It is based on a deep learning algorithm and is capable of accurately removing the background of images.

# References 

- https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html#ga397ae87e1288a81d2363b61574eb8cab
- https://docs.opencv.org/3.4/da/d5c/tutorial_canny_detector.html
- https://docs.opencv.org/3.4/d1/d10/classcv_1_1ximgproc_1_1ThinningLayer.html
- https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
- https://docs.opencv.org/3.4/d2/de8/group__core__array.html#ga60b4d04b251ba5eb1392c34425497e14
- https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#gaa9e58d2860d4afa658ef70a9b1115576
- https://www.tensorflow.org/tutorials/images/classification
- https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html
- https://www.youtube.com/watch?v=onWJQY5oFhs&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&start_radio=1&rv=onWJQY5oFhs&t=246
- https://www.youtube.com/watch?v=4pYyD2uSeko&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&index=2
- https://www.youtube.com/watch?v=G8yp6f9V_6c&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&index=15
- https://www.youtube.com/watch?v=hUC1uoigH6s&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&index=30
- https://www.youtube.com/watch?v=3VkkDd0rEoE&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&index=48
- https://www.youtube.com/watch?v=XRBc_xkZREg&list=RDCMUCf0WB91t8Ky6AuYcQV0CcLw&index=50




