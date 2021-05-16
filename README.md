# VehicleSecuritySystemProject
Vision Based Vehicle Security Project
                                 Present By := SARANG TAMRAKAR

Problem Statement :- To make an automatic Vision Based Vehicle Surveillance system , which will surveillance the all vehicle on road that whether they are maintaining safest distance or not..
Vehicles to detect:- Car , Truck , Bus , Auto , Bike & Cycle(total 6 classes)


Solution :-  We will going to follow certain strategy for this solution:

1.	As of now we know that all of these classes already in COCO DATASET so we can use Pretrained model for these classes.
2.	We want our Inference in real time so we will select our model such that gives us real time response.
3.	That’s why we will using SSD MOBILE NET (it is already trained on coco dataset)

Procedure:- For the complete solution we are going to follow certain procedure-

•	We will take the live video from streaming then we will  take the images from the video.

•	We will pass the image to the pretrained model SSD MOBILE NET & we will get the result as (Bounding boxes,  Scores , CLASS ID) for all the classes.

•	Then we will filter out the (classes , bounding boxes,scores ) for our problem statement.

•	Then we will take the each bounding boxes & calculate their centroid so that we can calculate the actual distance from all the directions.

•	Then we will find out all the possible permutation of all the centroid.

•	Then we will calculate the distance from each centroid to all & we will draw the line to each boxes.

Difficulty faced :-

•	We have to take care of unnecessary calculating the distance (it means once we find the distance from A TO B , we will not find the distance from B TO A again.)
•	We have faced the difficulty with live motion in video.
•	Different angle problem for calculating distance.
