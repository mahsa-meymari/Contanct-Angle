# Contanct-Angle
Determining Contact angle of a drop

Problem: The input is an image of a drop we want it's right and left angle
Solution:
1. Read in Gray Scale
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
2. Edge Detection
![Edge_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/edges.jpg?raw=true)
3. Crop
![Crop_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/cropped.jpg?raw=true)
4. Surface Detection
![Surface_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/surface.jpg?raw=true)
5. Under Surface Removal
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
6. Drop Contact Surface Detection
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
7. Tangent Lines Detection
![Tangent_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/tangent.jpg?raw=true)
8. Contact Angle Calculation
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
