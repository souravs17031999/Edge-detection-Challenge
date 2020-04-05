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
*  ```KNN algorithm``` :    
k-NN is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until function evaluation.    

Both for classification and regression, a useful technique can be to assign weights to the contributions of the neighbors, so that the nearer neighbors contribute more to the average than the more distant ones.           
[Taken from wikipedia] :  
![knn](/img/knn.png)    
Explanation : test sample (green dot) should be classified either to blue squares or to red triangles. If k = 3 (solid line circle) it is assigned to the red triangles because there are 2 triangles and only 1 square inside the inner circle. If k = 5 (dashed line circle) it is assigned to the blue squares (3 squares vs. 2 triangles inside the outer circle).   
  
* Edge detection in the browser using ```tensorflow.js``` [TODO - Currently in progress]   

# Getting started :
### Real time Flask server hosted :      
* Log on to following URL hosted on pythonanywhere.com using flask server :    
#### [LIVE WEBSITE](https://souravdlboy.pythonanywhere.com/)

### CMD (terminal) solution :     
* We need to install latest version of Opencv.       
[Download here](https://pypi.org/project/opencv-python/)      
* Run the cmd (terminal).      

* Download the project files using following command in the directory from where you need to run the script :     
```
git clone https://github.com/souravs17031999/Edge-detection-Challenge       
```   
* Change directory to ```edge_detect_cmd```.    

* Run the command using the following parameters as shown :    
```
python edge_detection.py <image> <X> <Y>    
``` 
positional arguments:   
| arguments  | details |
| ------------- | ------------- |
| image | Image path |  
| X | x coordinate of user selected point |
| Y | y coordinate of user selected point |      

# Sample runs with outputs :    
Note : closest edges are marked and shown.  
![flask1](/img/flask1.JPG)   

![flask2](/img/flask2.JPG)      

![output1](/img/output1.JPG)
![output2](/img/output2.JPG)
![output3](/img/output3.JPG)
![output4](/img/output4.JPG)



