# Contanct-Angle
Determining Contact angle of a drop

Problem: The input is an image of a drop we want it's right and left angle
Solution:
1. Read in Gray Scale 
<img src="./result_steps/gray.jpg" alt="Gray Image" width="200"/>
2. Edge Detection : Using Canny Algorithm
<img src="./result_steps/edges.jpg" alt="Edges Image" width="200"/>
3. Crop : Using hough algorithm the finest circle(drop) will be detect and it will be cropped with a pad
<img src="./result_steps/cropped.jpg" alt="Cropped Image" width="200"/>
4. Surface Detection : Using hough algorithm the largest line will be detected as surface
<img src="./result_steps/surface.jpg" alt="Surface Detected Image" width="200"/>
5. Under Surface Removal
<img src="./result_steps/drop.jpg" alt="Under Surface Removed Image" width="200"/>
6. Drop Contact Points Detection : the farest points on the surface will be considered as drop contact points
<img src="./result_steps/dropEdge.jpg" alt="Drop Contance Points Image" width="200"/>
7. Tangent Lines Detection
<img src="./result_steps/tangent.jpg" alt="Tangent Lines Image" width="200"/>
8. Contact Angle Calculation: using tangent lines's slop angles is calculated
<img src="./output1.jpg" alt="Angles Image" width="200"/>
