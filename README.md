# April Tags vs YOLOv5
- compare performance for both April Tag (id 0) and YOLOv5 model in terms of their detection accuracy, average speed of detection and their memory requirements.

## Equipments
-	The experiments are tested using a logitech webcam C922 (1920x1080 resolution and 30 fps) laptop with specs:
  - i7-1165G7
  - 16GB RAM
  - NVIDIA GeForce MX450
  
## Accuracy vs Distance
### April Tag
- id 0 with size of 0.123m 

| Actual Distance (m) | Measured Distance (m) | Percentage Error (%) |
|-------------|-------------|-------------| 
|1.25|1.225|2| 
|2.50|2.438|2.48|
|3.75|3.674|2.03|
|5.00|4.918|1.64|
|6.25|6.183|1.07|
|7.50|7.440|0.8|
|8.75|7.440|0.81|
|10.00|9.913|0.87|
|10.80 (maximum range)|10.815|0.14|

### YOLOv5
- tested to detect a person

| Actual Distance (m) | Accuracy (1 or 0) | Confidence (%) |
|-------------|-------------|-------------| 
|3.75|1|0.93|
|5.00|1|0.92|
|5.00|1|0.92|
|7.50|1|0.90|
|8.75|1|0.87|
|10.00|1|0.83|
|11.25|1|0.70|
|12.50|1|0.81|
|13.75|1|0.54|
|15.00|1|0.41|
|16.25|1|0.80|
|17.50|1|0.65|
|18.75|1|0.65|
|20.00|1|0.50|
|21.25|1|0.50|
|22.50|1|0.50|
|23.75|1|0.60|
|25.00|1|0.70|
|26.25|1|0.60|

- the limit of the YOLOv5 for detecting a person is pretty far and should be enough for object detection in F1Tenth
- as this experiment is to detect a person and the size of a person is much larger than a F1Tenth car, the limit of detection distance should be shorter

## Average Speed of Detection (Topic Publishing Speed)
### April Tag
- /tag_detections: 13.39Hz

### YOLOv5
- /yolo_result_out: 12.50Hz


## CPU Memory Requirement
### April Tag
- 1.21%

### YOLOv5
- 20.45%
- 1.6GB / 2GB (GPU Memory)

## Possible Modifications
- use stereo camera models so depth information can be obtained using camera
- april tag requires the tag to be printed and attached to all objects for detection, which is not really practical in real-life situation

## Conclusion
- After analyzing the data, we recommend using YOLO as it is more robust with a farther range of detection compared to April Tags. Despite having a 20x memory requirements, a camera sensor can be generalized to work on more tasks other than just object detection. Moreover, we can’t expect to put an April tag on all of our opponent's car so we have decided to use YOLO.


