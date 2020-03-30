import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse
import scipy
from scipy import spatial

class object_detection:

    # Locate the closest point on the edge using KNN
    def get_min(self, result, test_row, num_neighbors):
        distances = []
        rows, cols = len(result), len(result[0])
        for i in range(rows):
            for j in range(cols):
                    if result[i][j]:
                        dist = scipy.spatial.distance.euclidean(test_row, [j, i])
                        distances.append(([j, i], dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = []
        if len(distances):
                neighbors.append((distances[0][0], distances[0][1]))
        return neighbors

    def filter(self, gray):
        # apply opencv convolution canny edge detection
        output = cv2.Canny(gray, 100, 200)
        return output


    def main(self, image_path, y):

        image = cv2.imread(image_path)
        # changing image to gray scale , that means now the channel is 1
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
        plt.imshow(gray, cmap='gray')
        fig.add_subplot(1, 3, 3)
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
    o = object_detection()
    o.main(args.Image_path, [args.X, args.Y])
