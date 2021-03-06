# import important packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import scipy
from scipy import spatial

# main class for edge detection script
class edge_detection:

    # function for Locating the closest point on the edge using KNN
    def get_min(self, result, test_row, num_neighbors):
        '''
        result : filtered image after applying convolution
        test_row : given point by the user
        num_neighbors : no of neighbours to consider for the KNN algorithm
        '''
        distances = []   # distances is list of tuples where first item : coordinate, second item : distance
        rows, cols = len(result), len(result[0])
        # looping over the entire image
        for i in range(rows):
            for j in range(cols):
                    # only calculate distance if there is edge detected at that point
                    if result[i][j]:
                        # euclidean distance calculation
                        dist = scipy.spatial.distance.euclidean(test_row, [j, i])
                        distances.append(([j, i], dist))
        # sorting the distances list on the basis of distance between given point and the corresponding point on image
        distances.sort(key=lambda tup: tup[1])
        # calculating only the first neighbour, the first closest edge
        neighbors = []
        if len(distances):
                neighbors.append((distances[0][0], distances[0][1]))

        # return the first closest edge
        return neighbors

    # function for applying filter over the image
    def filter(self, gray):
        '''
        gray : grayscaled image
        '''
        # apply opencv convolution using canny edge detection
        output = cv2.Canny(gray, 100, 200)
        return output

    # function for main driver
    def main(self, image_path, y):
        '''
        image_path : Actual complete path of the image
        y : given point by the user in the image
        '''
        image = cv2.imread(image_path)  # read the image

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # changing image to gray scale , that means now the channel is 1
        print(f"Image read , shape of image is {image.shape}")
        # calling for applying filters and plotting the output images
        result_img = self.filter(gray)
        closest_edges = self.get_min(result_img, y, 1)
        # printing closest edges
        print(closest_edges)
        start_point = (y[0], y[1])
        end_point =  (closest_edges[0][0][0], closest_edges[0][0][1])
        color = (255, 0, 0)
        thickness = 20
        # drawing a line from start to end
        cv2.line(image, start_point, end_point, color, thickness)
        cv2.line(gray, start_point, end_point, color, thickness)
        cv2.line(result_img, start_point, end_point, color, thickness)
        # cv2.imshow('filtered image', result_img)
        # print("Outputting the final images...")
        # Wait for Esc key to stop
        print(f"The closest edge distance is {closest_edges[0][1]}")
        fig=plt.figure(figsize=(30, 30))
        fig.add_subplot(1, 3, 1)
        plt.imshow(image)
        fig.add_subplot(1, 3, 2)
        plt.title('Gray scaled image')
        plt.imshow(gray, cmap='gray')
        fig.add_subplot(1, 3, 3)
        plt.title('Detected edges')
        plt.imshow(result_img, cmap='gray')
        plt.show()

# main driver function
if __name__ == '__main__':
    print("WELCOME TO EDGE DETECTION !")
    parser = argparse.ArgumentParser(description='EDGE DETECTION', epilog='Happy Detection :)')
    parser.add_argument('Image_path', type=str, help='Path of the Image')
    parser.add_argument('X', type=int, help='X coordinate')
    parser.add_argument('Y', type=int, help='Y coordinate')
    args = parser.parse_args()
    o = edge_detection()
    o.main(args.Image_path, [args.X, args.Y])
