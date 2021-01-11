# Contanct-Angle
Determining Contact angle of a drop

Problem: The input is an image of a drop we want it's right and left angle
Solution:
1. Read in Gray Scale
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
2. Edge Detection
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/edges.jpg" alt="Edges image" width="200"/>
3. Crop
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Crop_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/cropped.jpg?raw=true)
4. Surface Detection
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Surface_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/surface.jpg?raw=true)
5. Under Surface Removal
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
6. Drop Contact Surface Detection
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
7. Tangent Lines Detection
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Tangent_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/tangent.jpg?raw=true)
8. Contact Angle Calculation
<img src="https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg" alt="Gray image" width="200"/>
![Gray_image](https://github.com/mahsa-meymari/Contanct-Angle/blob/main/result_steps/gray.jpg?raw=true)
