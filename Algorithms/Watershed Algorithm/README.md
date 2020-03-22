# Computer-Vision-Watershed-Algorithm
An introduction to image segmentation algorithm mostly used in Computer Vision - Watershed algorithm

This is an brief introduction code for the algorithm Watershed using OpenCV. A more detailed algorithm explanation can be found on my Medium post (link in my profile).

The results folder contains some resulting images from the algorithm.
1. Sure background
- This is obtained after performing opening, where after erosion and dilation, the segment left is a sure background

2. Sure foreground
- This is obtained by performing distance transform and then thresholding the resulting image, to get a smaller portion of the object which is a sure foreground

3. Distance Transform
- This is after the distanceTransform() function

4. Unknown
- This is obtained by subtracting sure foreground from sure background, where the unknown usually lies in the object boundary 

5. Result
- The thin red line around the object is the boundary found by the algorithm, useful in detecting objects and segmenting them in object detection

What I Learnt:
- How Watershed algorithm works
- How to implement Watershed using OpenCV

Future Implementation:
- Working on having object detection and image segmentation algorithms(including GrabCut algorithm) to extract written words from pictures taken from a smartphone camera.
