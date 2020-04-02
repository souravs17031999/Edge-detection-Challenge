# Edge-detection-Challenge

# Project Objective : 
Create a page or tool which performs edge detection on a given image and, given a point, returns the distance from that point to the closest edge.    

# Approach :
* Using ```Canny edge detection``` (openCV) + ```KNN``` algorithm run from command line (terminal).
* Using ```Canny edge detection``` (openCV) + ```KNN``` algorithm with ```Flask``` server.       
> Brief introduction :         
* Canny edge detection steps ->   Canny edge detection is a technique to extract useful structural information from different vision objects and dramatically reduce the amount of data to be processed.           
1. Apply Gaussian filter to smooth the image in order to remove the noise      
![1](/img/1.JPG)       
     
     
2. Find the intensity gradients of the image.       
![2](/img/2.JPG)       
3. Apply non-maximum suppression to get rid of spurious response to edge detection     
4. Apply double threshold to determine potential edges        
5. Track edge by hysteresis: Finalize the detection of edges by suppressing all the other edges that are weak and not connected to strong edges.           
* Edge detection in the browser using ```tensorflow.js```    

# Getting started :

# Sample runs with outputs :    
Note : closest edges are marked and shown.    
![output2](/img/output1.JPG)
![output](/img/output.JPG)


