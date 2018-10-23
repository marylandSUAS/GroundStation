# Imaging


# being worked on
interop_server.py
Runs communicates between the interop server and the ground processes

# done
image_reciever.py
recieves images from plane and saves them to location

# done
image_reset.py
all images in current working space are moved to storage area and submission pictures are deleted

# needs rework
image_opencv.py
processes/classifies images to be submitted to judges server

#done
image_distribution.py
reads images from files and distributes to files that request to process


# ALL NEED TESTING

# uav_image msgs
geometry_msgs/Point pos 
float32 hdg
String type
String shape
String background_color
String alpha
String alpha_color
