#!/usr/bin/env python

import interop
import rospy
from geometry_msgs.msg import Twist, Pose, PoseStamped, PointStamped, Point
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image, CameraInfo

from visualization_msgs.msg import Marker, MarkerArray


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

class interop_ros:
    def __init__(self):        

        self.mission_pub = rospy.Publisher("/auto/rviz/vehicle", MarkerArray, queue_size=1)

        self.bridge = CvBridge()

        # static_transform_publisher x y z qx qy qz qw frame_id child_frame_id  period_in_ms
        self.tbr = tf.TransformBroadcaster()



        rospy.Subscriber("/auto/gate_detection_gate", Image,self.callback, 'Image')
        rospy.Subscriber("/bebop/image_raw", Image,self.callback, 'Image')
        rospy.Subscriber("/auto/wp_look", WP_Msg, self.callback,'wp_look')
        rospy.Subscriber("/auto/state_auto", Int32, self.callback,'state')
        rospy.Subscriber("/auto/state_auto", Float32, self.callback,'state')







    def callback(self,data,args):
        # rospy.loginfo(rospy.get_caller_id() + "\nI heard %s", data)
         elif args == "state":
            if data.data != self.state_level:
                self.gate_number = self.gate_number+1
                # self.state_level = self.state_level+10

        elif args == "battery":

            # print ' '
            # print 'Battery level: ',data.percent
            # print ' '
            self.battery_level = data.percent
        elif args == "wifi":
            if data.rssi * 2 + 160 < 100.0:
                print 'R: ',(data.rssi * 2 + 160),'  B: ',self.battery_level
            else:
                print 'R: ',(data.rssi * 2 + 160),' B: ',self.battery_level
       
        elif args == 'Image':
            
            rgb = bridge.imgmsg_to_cv2(data, desired_encoding=data.encoding)

  
            # output_im = self.bridge.cv2_to_imgmsg(mask, encoding="8UC1")
            # publisher.publish(output_im)

       
       
def main():
    signal.signal(signal.SIGINT, signal_handler)

    # usern = 'maryland'
    # passw = '5003191261'

    usern = 'testuser'
    passw = 'testpass'

    # youareL = 'http://10.10.130.10:80'
    youareL = 'http://192.168.1.2:8000'
    path = 'Confirmed/'

    client = interop.Client(url=youareL, username=usern, password=passw)
    print('connected to client')




    rospy.init_node('interop_ros', anonymous=True)

    
    
    interop_ros()

    rospy.spin() 

if __name__ == '__main__':
    main()
