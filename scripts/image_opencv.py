#!/usr/bin/env python

import time
import os
import cv2
import imutils
import numpy as np

import rospy
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image, CameraInfo
from imaging_msgs.msg import uav_image



	
	
# Returns cropped img dictleep
def click_crop():
	print("<Cropping>")
	cv2.setMouseCallback("image",crop_callback)
	cv2.imshow("image",cv2.imread(image['path']))

	while True:
		key = cv2.waitKey(1) & 0xFF
		if key == ord("c"):
			print('<Finished Cropping>')
			cv2.setMouseCallback("image",lambda *args : None)
			break


	# Use src img dict as template, but change path to be accurate for cropped img.
	cropped_path = "./manual_registered/cropped/" + image['name']
	cropped = image
	cropped['path'] = cropped_path
	return cropped



def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
 
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)





def find_position(pos,heading,theta,dim,point):
	Xfov = 53.94*pi/180;
	Yfov = 41.85*pi/180;
	image_shape = [4640 3480]

	Xskew = 0 # meters
	Yskew = 0 # meters
	Rskew = 0 # degrees
	Xdist = 1
	Ydist = 1


	alt = pos[2]
	
	rad_Earth = 20909000.0
	dlng = (pi/180)*rad_Earth*cos(pos[0]*pi/180);
	dlat = (pi/180)*rad_Earth

	target_heading = pi+heading+theta;

	pixel_offset_X = point[0]-.5*image_shape[0]
	pixel_offset_Y = point[1]-.5*image_shape[1]

	fov = [Xdist*.5*Xfov*(pixel_offset_X)/image_shape[0],
    	Ydist*.5*Yfov*(pixel_offset_Y)/image_shape[1]]

	d_pos = (alt*sin(fov[0])+Xskew,alt*sin(fov[1])+Yskew)
	pos_rot = pi-heading + Rskew
	
	rotated_pos = [cos(pos_rot)*d_pos[0]+sin(pos_rot)*d_pos[1], -sin(pos_rot)*d_pos[0]+cos(pos_rot)*d_pos[1]]
	GPS_pos = [rotated_pos[1]*dlat,rotated_pos[0]*dlng]
	
	finalGPS = [pos[0]+rotated_pos[0],pos[1]+rotated_pos[1]]
	
	return pos,target_heading



def crop(img, loc, size):
	xsize = img.shape[0]
	ysize = img.shape[1]
	
	x1 = loc[0]-size/2
	y1 = loc[1]-size/2
	x2 = loc[0]+size/2
	y2 = loc[1]+size/2
	
	if(x1 < 0):
		x1 = 0
		x2 = size
	elif(x2 > xsize):
		x1 = xsize-2*size
		x2 = xsize
	if(y1 < 0):
		y1 = 0
		y2 = 2*size
	elif(y2 > ysize):
		y1 = ysize-2*size
		y2 = ysize

	return img[y1:y2,x1:x2]


def recrop(img,point,size,theta):
	img_crop1 = crop(img,point,size*1.5)
	img_temp = imutils.rotate(img_crop1,theta)
	return crop(img_temp,img_temp.size/2,size)
 

def do_image(img,GPS,hdg):
	while True:
		key = cv2.waitKey(0)
		if key == 32:
			# begin classifying

			img_temp = img
			zoom_level = 200
			point = img.size/2	
			while True:
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)

				if key == 43:
					zoom_level = zoom_level - 5
					img_temp = zoom(img,zoom_level,point)
				elif key == 45:
					zoom_level = zoom_level + 5
					img_temp = zoom(img,zoom_level,point)
				
				elif chr(key) == 'w':
					point = [point[1],point[2]+5]
					img_temp = zoom(img,zoom_level,point)
				elif chr(key) == 's':
					point = [point[1],point[2]-5]
					img_temp = zoom(img,zoom_level,point)
				elif chr(key) == 'd':
					point = [point[1]+5,point[2]]
					img_temp = zoom(img,zoom_level,point)
				elif chr(key) == 'a':
					point = [point[1]-5,point[2]]
					img_temp = zoom(img,zoom_level,point)
				
				elif key == 8:
					img_temp = img
				elif key == 32:
					break
				elif key == 27:
					return None
			

			theta = 0
			img_cropped = img_temp
			while True:
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)

				elif chr(key) == 'd':
					theta = theta-5
					img_temp = imutils.rotate(img_cropped,theta)
				elif chr(key) == 'a':
					theta = theta+5
					img_temp = imutils.rotate(img_cropped,theta)

				elif key == 8:
					img_temp = img_cropped
				elif key == 32:
					break
				elif key == 27:
					return None


			target_pos,target_heading = find_position(GPS,hdg,theta,img.shape,point)


			img_submit = recrop(img,point,size,theta)
			img_class = cv2.resize(img_submit,(0,0),fx=4,fy=4)

			shapes = {48:'circle',49:'semicircle',50:'quarter_circle',51:'triangle',52:'square',53:'rectangle',54:'trapezoid'
									,55:'pentagon',56:'hexagon',57:'heptagon',97:'octagon',98:'star',99:'cross'}
			colors = {48:'white',49:'black',50:'gray',51:'red',52:'blue',53:'green',54:'yellow',55:'purple',56:'brown',57:'orange'}
							
				
			# CLASSIFY ALPHA
			alpha = 'Alphanumeric'
			while True:
				img_temp = img_class
				cv2.putText(img_temp, alpha, (230, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)


				if key == 32:
					break
				elif key == 27:
					return None
				else:
					alpha = str(chr(key)).upper()

			# CLASSIFY ALPHA COLOR
			alpha_color = 'Alpha color'
			while True:
				img_temp = img_class
				cv2.putText(img_temp, alpha_color, (230, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)


				if key == 32:
					break
				elif key == 27:
					return None
				else:
					alpha_color = colors.get(key,'white')

			# CLASSIFY BACKGROUND COLOR
			color = 'Color'
			while True:
				img_temp = img_class
				cv2.putText(img_temp, color, (230, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)

				if key == 32:
					break
				elif key == 27:
					return None
				else:
					color = colors.get(key,'white')


			# CLASSIFY SHAPE
			shape = 'Shape'
			while True:
				img_temp = img_class
				cv2.putText(img_temp, shape, (230, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
				cv2.imshow('image',img_temp)
				key = cv2.waitKey(0)

				if key == 32:
					break
				elif key == 27:
					return None
				else:
					shape = shapes.get(key,'circle')

	return img_submit, target_pos, target_heading, alpha, alpha_color, color, shape



def callback(data)
	global image_recieved
	image_recieved = True


	imag = bridge.imgmsg_to_cv2(data.image.data, desired_encoding=data.image.encoding)

	img_submit, target_pos, target_heading, alpha, alpha_color, color, shape = do_image(imag,[data.pos.x,data.pos.y,data.pos.z],data.hdg)

	submit_msg = uav_image()
	submit_msg.image = bridge.cv2_to_imgmsg(img_submit, encoding="8UC1")
	
	submit_pos = Point()
	submit_pos.x = target_pos[0]
	submit_pos.y = target_pos[1]

	submit_msg.hdg = target_heading
	submit_msg.type = data.type
	submit_msg.shape = shape
	submit_msg.background_color = color
	submit_msg.alpha = alpha
	submit_msg.alpha_color = alpha_color
	
    submit_pub.publish(output_im)



def main():

	computer_num = 1
	node_name = 'reciever_node'+str(computer_num)
	pub_name = '/ask_'+str(computer_num)
	sub_name = '/image_ask_'+str(computer_num)

	rospy.init_node(node_name, anonymous=True)

    rospy.Subscriber(sub_name, uav_image, callback)
    asking_pub = rospy.Publisher(pub_name, Empty, queue_size=1)
    submit_pub = rospy.Publisher('/interop_submission', uav_image, queue_size=1)
    
    bridge = CvBridge()

	global image_recieved
	image_recieved = False    

	while True:
		key = os.input('Press enter for another image'+str(time.time()))
		
    	msg = Empty()
    	asking_pub.publish(msg)

    	image_recieved = False
    	time.sleep(5)
    	if image_recieved == True:
    		while True:
    			if image_recieved == True:
    					time.sleep(.5)
    			else:
    				break


		


if __name__ == '__main__':
    main()