#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image, CameraInfo
from imaging_downlink.msg import uav_image_Msg


import cv2
from cv_bridge import CvBridge
import numpy as np
import time
import signal


def signal_handler(signal, frame):
    sys.exit(0)


def callback(data):

    img = bridge.imgmsg_to_cv2(data.image.data, desired_encoding=data.image.encoding)
    cv2.imwrite('Images/'+data.image.header.frame_id,img)
    with open('Images/'+data.image.header.frame_id+'.txt','w') as writer:
    	writer.write(str(data.pos.x))
    	writer.write(str(data.pos.y))
    	writer.write(str(data.pos.z))
    	writer.write(str(data.hdg))

    pub.publish()


       
def main():
    signal.signal(signal.SIGINT, signal_handler)

    rospy.init_node('reciever_node', anonymous=True)
    
    bridge = CvBridge()

    rospy.Subscriber("/Plane_image", Image, callback)
    
    pub = rospy.Publisher('ImageConfirm', Empty, queue_size=1)  

    rospy.spin()


if __name__ == '__main__':
    main()
