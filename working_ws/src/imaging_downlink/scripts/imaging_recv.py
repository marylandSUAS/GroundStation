#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, PoseStamped, PointStamped, Point
from std_msgs.msg import Empty, Int32, Float32
from imaging_downlink.msg import uav_image_Msg

import cv2
import numpy as np
import time
import signal
import sys
from cv_bridge import CvBridge, CvBridgeError


pub = rospy.Publisher('ImageConfirm', Empty, queue_size=1)	


def sigterm_handler(signal, frame):
    # save the state here or do whatever you want
    print('booyah! bye bye')
    sys.exit(1)


signal.signal(signal.SIGINT, sigterm_handler)


class receiver:


	def image_receiver(self, data):
		bridge = CvBridge()

		try:
			cv_image = bridge.imgmsg_to_cv2(data.image, "bgr8")
			cv2.imwrite('/home/imaging/GroundPics/Picture' + str(self.count) + '.jpeg',  cv_image)
			pub.publish()
			self.count = self.count + 1

		except CvBridgeError as e:
			print(e)


	

	def listener(self):
		rospy.init_node('listener', anonymous=True)
		rospy.Subscriber('ImageSender', uav_image_Msg, self.image_receiver)
		rospy.spin()


	def __init__(self):
		self.count = 1

		self.listener()

receiver()


