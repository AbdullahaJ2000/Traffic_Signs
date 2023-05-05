import cv2
import numpy as np
import os
import random

class trffic_signs():

    def __init__(self,filename):
        # loads the input image and resizes it if necessary.
        self.img = cv2.imread(filename,cv2.IMREAD_UNCHANGED)

        if self.img.size <= 250000:
            self.img = cv2.resize(self.img, (450, 450))
        else:
            self.img = cv2.resize(self.img, (900, 900))

    def ToGray(self):
        # converts the input image to grayscale.
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        return gray

    def FindEdges(self):
        #applies Canny edge detection on the grayscale image to detect edges.
        gray_blur = cv2.GaussianBlur(self.ToGray(), (5, 5), 1)
        cv2.imwrite("steps/gray_blur.png", gray_blur)
        edges = cv2.Canny(gray_blur, 200, 200)

        # Define a kernel for dilation and erosion operations
        kernel = np.ones((5,5), np.uint8)

        # Dilate the edges using the kernel
        dilated_edges = cv2.dilate(edges, kernel, iterations=1)

        return dilated_edges

    def Thinning(self):
        # applies thinning to the edges to reduce their thickness.
        thinned_img = cv2.ximgproc.thinning(self.FindEdges())

        return thinned_img

    def FindContoursArea(self):
        #Finds the contour with the maximum area from the thinned image.
        contours, hierarchy = cv2.findContours(self.Thinning(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        max_area_contour = max(contours, key=cv2.contourArea)

        return max_area_contour

    def RemoveBackground(self):
        # removes the background from the input image using the maximum area contour found in the previous step.
        # Create a black mask with the same dimensions as the original image

        mask = np.zeros_like(self.img)
        # Draw the contour on the mask
        cv2.drawContours(mask, [self.FindContoursArea()], 0, (255, 255, 255), -1)

        # Apply the mask to the original image
        result = np.bitwise_and(self.img, mask)
        return result

    def FadedToRmoveBlackBackground(self):
        #removes the black background from the faded image by generating a mask
        #that separates the black pixels from the non-black pixels.
        result=self.FadeImage()
        mask = np.zeros((result.shape[0], result.shape[1]), dtype=np.uint8)
        mask[np.all(result[:, :, :3] == [0, 0, 0], axis=-1)] = 0
        mask[np.all(result[:, :, :3] != [0, 0, 0], axis=-1)] = 255
        result = cv2.merge((result[:, :, 0], result[:, :, 1], result[:, :, 2], mask))
        return result

    def FadeImage(self):
        # fades the input image by applying an alpha mask to the image
        # then multiplying each color channel with a given alpha value.
        # This method is used to reduce the intensity of the traffic sign and blend it better with the background.

        alpha=3.5
        result = self.RemoveBackground()
        mask = np.zeros((result.shape[0], result.shape[1]), dtype=np.uint8)
        mask[np.all(result[:, :, :3] == [0, 0, 0], axis=-1)] = 0
        mask[np.all(result[:, :, :3] != [0, 0, 0], axis=-1)] = 255

        # Check if image has an alpha channel
        if result.shape[2] == 4:
            b, g, r, a = cv2.split(result)
        else:
            b, g, r = cv2.split(result)
            a = np.ones_like(b) * 255  # create an alpha channel with full opacity


        b=cv2.multiply(b,alpha)
        g = cv2.multiply(g, alpha)
        r = cv2.multiply(r, alpha)
        a = cv2.subtract(a,2)
        faded_img = cv2.merge((b, g, r, a))
        faded_img = cv2.bitwise_and(faded_img, faded_img, mask=mask)
        return faded_img


    def PasteOnBackground(self, background_path):
        # pastes the image with the removed background onto a random background image by blending the two images together.

        # Load the background image and the image with the removed background
        background = cv2.imread(background_path,cv2.IMREAD_UNCHANGED)
        removed_bg_img = self.FadedToRmoveBlackBackground()
        removed_bg_img=cv2.resize(removed_bg_img,(150,150))
        # Get the dimensions of the background and the image
        bg_height, bg_width, _ = background.shape
        img_height, img_width, _ = removed_bg_img.shape

        # Generate a random location to paste the image
        x = random.randint(0, bg_width - img_width)
        y = random.randint(0, bg_height - img_height)

        # Create a mask for the image
        mask = removed_bg_img[:, :, 3] / 255

        # Blend the image with the background
        for c in range(3):
            background[y:y + img_height, x:x + img_width, c] = (1 - mask) * background[y:y + img_height,
                                                                            x:x + img_width, c] + mask * removed_bg_img[
                                                                                                         :, :, c]
        return background


def __main__():
    #Generates a random traffic sign image and a random background image from the respective directories.
    #It then creates an object of the trffic_signs class with the traffic sign image and calls the PasteOnBackground method
    #to paste the image onto the background.
    #Finally, it displays the resulting image using OpenCV.

    trafficPath = 'Traffic_signs_images'
    trafficImages=os.listdir(trafficPath)
    trafficImage = os.path.join(trafficPath, random.choice(trafficImages))

    backgrounPath = 'background_images'
    backgroundImages = os.listdir(backgrounPath)
    backgroundImage = os.path.join(backgrounPath, random.choice(backgroundImages))

    #creat object
    ts = trffic_signs(trafficImage)
    finalImage=ts.PasteOnBackground(backgroundImage)
    cv2.imshow("final_result",finalImage)
    cv2.waitKey(0)
    cv2.imwrite("Final_output/final_result.png",finalImage)


if __name__ == '__main__':
    __main__()
