#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, PoseStamped, PointStamped, Point
from std_msgs.msg import Empty, Int32, Float32
from imaging_downlink.msg import uav_image_Msg

import cv2
import numpy as np
import time
import sys
from cv_bridge import CvBridge, CvBridgeError


pub = rospy.Publisher('ImageConfirm', Empty, queue_size=1)	

def image_receiver(data):
	bridge = CvBridge()

	try:
		cv_image = bridge.imgmsg_to_cv2(data.image, "bgr8")
		cv2.imwrite('gottem.jpeg', cv_image)
		cv2.imwrite('/home/imaging/catkin_ws/src/imaging_downlink/scripts/gottem.jpeg',  cv_image )
		pub.publish()


	except CvBridgeError as e:
		print(e)


	

def listener():
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('ImageSender', uav_image_Msg, image_receiver)
	rospy.spin()

if __name__ == '__main__':
	listener()


