#!/usr/bin/env python

import interop
import rospy
from geometry_msgs.msg import Point 
from std_msgs.msg import Empty, Float32
from sensor_msgs.msg import Image, CameraInfo

# needs to be fixed
from imaging_msgs.msg import uav_image


import cv2
from cv_bridge import CvBridge
import numpy as np
import time
import math
import signal
import sys
import tf


def signal_handler(signal, frame):
    sys.exit(0)

        
# callback is called everytime something is posted to the ROS '/interop_submission' topic
def callback(self,data):
    
    # this converts the image in the message to an opencv file
    rgb = bridge.imgmsg_to_cv2(data, desired_encoding=data.encoding)
   
    #creates a target object for the judges server
    target = interop.Odlc(type=data.type,
    latitude=float(data.pos.y),
    longitude=float(data.pos.x),
    orientation=data.hdg,
    shape=shape,
    background_color=shape_color,
    alphanumeric=alpha,
    alphanumeric_color=alpha_color)

    # posts the target to the server
    target = client.post_odlc(target)
    #submit_image_pointer = open(cropped['path'], 'rb')
    #submit_image = submit_image_pointer.read()

    # matches the submitted target with the corresponding image
    client.put_odlc_image(target.id, rgb)
    print('SUBMITTED '+data.shape_color+' '+data.shape+' '+data.alpha)


        
def main():
    signal.signal(signal.SIGINT, signal_handler)

    # usern = 'maryland'
    # passw = '5003191261'

    usern = 'testuser'
    passw = 'testpass'

    # youareL = 'http://10.10.130.10:80'
    youareL = 'http://192.168.1.2:8000'

    # creates maryland's interop client 
    client = interop.Client(url=youareL, username=usern, password=passw)
    print('connected to client')

    # object to convert images from messages to opencv
    bridge = CvBridge()


    # initialize the node and subscriber within the ros system
    rospy.init_node('interop_ros', anonymous=True)
    rospy.Subscriber('/interop_submission', uav_image,self.callback)
    
    # just keeps the program from exiting
    rospy.spin() 

if __name__ == '__main__':
    main()
