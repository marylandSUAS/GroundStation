#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image, CameraInfo

import cv2
from cv_bridge import CvBridge
import numpy as np
import time
import signal


def signal_handler(signal, frame):
    sys.exit(0)


def callback(data):

    img = bridge.imgmsg_to_cv2(data.data, desired_encoding=data.encoding)
    cv2.imwrite('Images/'+data.header.frame_id,img)

       
def main():
    signal.signal(signal.SIGINT, signal_handler)

    rospy.init_node('reciever_node', anonymous=True)
    
    
    bridge = CvBridge()

    rospy.Subscriber("/Plane_image", Image, callback)
    
    rospy.spin()


if __name__ == '__main__':
    main()
