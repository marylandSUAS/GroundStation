# Imaging


# interop_server.py
 - Runs communicates between the interop server and the ground processes
being worked on

# done
image_reciever.py
recieves images from plane and saves them to location

# image_reset.py
 - all images in current working space are moved to storage area and submission pictures are deleted
needs to also move the GPS/Hdg

# image_opencv.py
 - processes/classifies images to be submitted to judges server
needs rework

# image_distribution.py
 - reads images from files and distributes to files that request to process 
needs to grab the additional data from


ALL NEED TESTING

# uav_image_msgs
geometry_msgs/Point pos 
float32 hdg
String type
String shape
String background_color
String alpha
String alpha_color
