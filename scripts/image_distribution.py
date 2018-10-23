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


def callback(data,args):
    if queue+1 > len(total_files):
        return

    num = queue
    queue = queue+1

    image = total_files[num]

    # rgb = bridge.imgmsg_to_cv2(data, desired_encoding=data.encoding)

    os.rename("Images/"+image, "Sent/"+image)
    
    img = cv2.imread('Sent/'+image,1)

    output_im = bridge.cv2_to_imgmsg(img, encoding="8UC1")
    
    if args == 1:
        ask_pub_1.publish(output_im)
    elif args == 2:
        ask_pub_2.publish(output_im)
    elif args == 3:
        ask_pub_3.publish(output_im)
    elif args == 4:
        ask_pub_4.publish(output_im)
            

       
def main():
    signal.signal(signal.SIGINT, signal_handler)

    rospy.init_node('distribution_node', anonymous=True)

    queue = 0
    total_files = [f for f in os.listdir('/Images') if os.path.isfile(f)]

    print 'Found ',len(total_files), ' images'
    
    ask_pub_1 = rospy.Publisher("/image_ask_1", Image, queue_size=1)
    ask_pub_2 = rospy.Publisher("/image_ask_2", Image, queue_size=1)
    ask_pub_3 = rospy.Publisher("/image_ask_3", Image, queue_size=1)
    ask_pub_4 = rospy.Publisher("/image_ask_4", Image, queue_size=1)

    bridge = CvBridge()

    rospy.Subscriber("/ask_1", Empty,ask_callback,1)
    rospy.Subscriber("/ask_2", Empty,ask_callback,2)
    rospy.Subscriber("/ask_3", Empty,ask_callback,3)
    rospy.Subscriber("/ask_4", Empty,ask_callback,4)


    # file_list = os.listdir('.')
    # image_list = []
    # # print(file_list)
    # for item in file_list:
    #     if item.endswith(".jpg"):
    #         image_list.append(item)
    
    while(True):
        current_files = [f for f in os.listdir('/Images') if os.path.isfile(f)]
        for f in current_files:
            if f not in total_files:
                total_files.append(f)
                print 'Found image ',f

        time.sleep(.5)



if __name__ == '__main__':
    main()
