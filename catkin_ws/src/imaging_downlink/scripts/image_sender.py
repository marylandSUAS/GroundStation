#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, PoseStamped, PointStamped, Point
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image
from imaging_downlink.msg import uav_image_Msg

import cv2
import numpy as np
import time
import sys
from cv_bridge import CvBridge, CvBridgeError


booley = True

def confirm(nothing):
	print('confirmed')
	booley = True

	

def image_sender():
	rospy.Subscriber('ImageConfirm', Empty, confirm)	
	pub = rospy.Publisher('ImageSender', uav_image_Msg, queue_size=1)
	rospy.init_node('image_sender', anonymous=True)	
	bridge = CvBridge()
	img = cv2.imread('/home/imaging/catkin_ws/src/imaging_downlink/scripts/trees.jpeg', 1)
	output_im = bridge.cv2_to_imgmsg(img, encoding="bgr8")	

	pois = Point(1,2,3)

	message = uav_image_Msg()
	message.image = output_im
	message.pos = pois

	rospy.loginfo(message)
	booley = False	
	pub.publish(message) 
	
	rospy.spin()


if __name__ == '__main__':
	image_sender()

