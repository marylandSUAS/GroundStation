#!/usr/bin/env python

import cv2
import sys
import pynput
from pynput.keyboard import Key, Listener
import os
import time
import imutils
import numpy as np

import re

import rospy
from std_msgs.msg import Empty, Int32, Float32
from sensor_msgs.msg import Image, CameraInfo


CROP_WIDTH = 400 # half width
CROP_HEIGHT = 400 # half heigth
SCALE = 2 # by how much to blow up cropped image

PPM = 1 # PIXELS PER METER
F = 1 # Focal length
M_TO_LAT = 1 # Meters to lon
M_TO_LON = 1 # Meters to lat
image_queue = []

def insert():
	for item in image_list:
		newImg = {'name':item,'time':os.path.getmtime(item),'path':"./manual_registered/"+item}
		os.rename(item,newImg['path'])
		image_queue.append(newImg)

# Returns img dict
def dequeue():
	min_value = float("inf")
	min_file = ""
	min_img = None
	for elem in image_queue:
		if(elem['time']<min_value):
			min_value = elem['time']
			min_file = elem['name']
			min_img = elem
	if(min_value < float("inf")):
		image_queue.remove(min_img)
	# print(image_queue)
	return min_img

def crop_callback(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONUP:
		global croppedImg, pic_loc, offset_x, offset_y
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		# print(xsize)
		# print(ysize)
		# print(zsize)
		centerPt = (x, y)
		pic_loc = (x + offset_x, y+offset_y)
		x1 = centerPt[0]-CROP_WIDTH
		y1 = centerPt[1]-CROP_HEIGHT
		x2 = centerPt[0]+CROP_WIDTH
		y2 = centerPt[1]+CROP_HEIGHT
		if(x1 < 0):
			x1 = 0
			x2 = 2*CROP_WIDTH
		elif(x2 > xsize):
			x1 = xsize-2*CROP_WIDTH
			x2 = xsize
		if(y1 < 0):
			y1 = 0
			y2 = 2*CROP_HEIGHT
		elif(y2 > ysize):
			y1 = ysize-2*CROP_HEIGHT
			y2 = ysize
		offset_x += x1
		offset_y += y1



		# # draw a rectangle around the region of interest
		# cv2.rectangle(image, upLeft, downRight, (0, 255, 0), 2)
		# cv2.imshow("image", image)

		# Crop the image
		croppedImg = croppedImg[y1:y2,x1:x2]
		croppedImg = cv2.resize(croppedImg,(0,0),fx=SCALE,fy=SCALE)
		cv2.imshow("image",croppedImg)

		# Save cropped
		cropped_path = "./manual_registered/cropped/" + image['name']
		cv2.imwrite(cropped_path,croppedImg)

# Returns cropped img dictleep
def crop():
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

# Returns image array
def orient():
	print("<Orienting>")
	workingImg = cv2.imread(cropped['path'])

	angle = 0
	rotated = imutils.rotate_bound(workingImg, angle)
	while True:
		key = cv2.waitKey(0)
		if key == 113: # q
			angle = angle - 5
			rotated = imutils.rotate_bound(workingImg, angle)
		elif key == 101: # e
			angle = angle + 5
			rotated = imutils.rotate_bound(workingImg, angle)
		elif key == 13: # Enter
			oriented_path = "./manual_registered/cropped/oriented/" + image['name']
			cv2.imwrite(oriented_path,rotated)
			print("<Finished Orienting>")
			break
		cv2.imshow("image",rotated)


	# print("test3")
	oriented_path = "./manual_registered/cropped/oriented/" + image['name']
	oriented = cropped
	oriented['path'] = oriented_path
	return oriented, angle

def classify():
	print("Classifying")
	popup = np.ones([1000,800,3],dtype=np.uint8)*255
	cv2.imshow("Classification",popup)

	# char - ascii:
	# 0 - 48, 1 - 49, ..., 9 - 57
	# a - 97, b - 98, ..., z - 122
	shapes = {48:'circle',49:'semicircle',50:'quarter_circle',51:'triangle',52:'square',
	53:'rectangle',54:'trapezoid',55:'pentagon',56:'hexagon',57:'heptagon',
	97:'octagon',98:'star',99:'cross'}
	colors = {48:'white',49:'black',50:'gray',51:'red',52:'blue',53:'green',54:'yellow'
	,55:'purple',56:'brown',57:'orange'}

	# Counter for which stat is being clasified (can be reverted with backspace key)
	stat_counter = 0

	# Default Values
	shape_color = 'white'
	shape = 'circle'
	alpha_color = 'white'
	alpha = 'a'
	shift = False
	while True:
		key = cv2.waitKey(0)
		if key == 8:
			print("Redo " + str(stat_counter) +":")
			stat_counter = stat_counter - 1 if stat_counter > 0 else 0
		elif key == 13:
			if stat_counter >= 4:
				print("Finished Classifying")
				break
		else:
			if stat_counter == 0:
				shape_color = colors.get(key,'white')
				stat_counter += 1
				print(str(stat_counter) + ": " + shape_color)
			elif stat_counter == 1:
				shape = shapes.get(key,'circle')
				stat_counter += 1
				print(str(stat_counter) + ": " + shape)
			elif stat_counter == 2:
				alpha_color = colors.get(key,'white')
				stat_counter += 1
				print(str(stat_counter) + ": " + alpha_color)
			elif stat_counter == 3:
				if key == 226:
					shift = True
				else:
					if shift:
						shift = False
						alpha = str(chr(key))
						alpha = alpha.upper()
						stat_counter += 1
						print(str(stat_counter) + ": " + alpha)
					else:
						alpha = str(chr(key))
						stat_counter += 1
						print(str(stat_counter) + ": " + alpha)


	# debug_string = shape_color + " " + shape + ", " + alpha_color + " " + alpha
	# print(debug_string)

	return shape,shape_color,alpha,alpha_color

	#Shape - circle, semicircle, quarter_circle, triangle, square, rectangle, trapezoid, pentagon
	#	   - hexagon, heptagon, octagon, star, cross
	#Color - white, black, gray, red, blue, green, yellow, purple, brown, orange
	#Letter - a-z 0-9

# Input in radians
def Rz(th):
	c, s = np.cos(th), np.sin(th)
	r1 = (c,s,0)
	r2 = (-s,c,0)
	r3 = (0,0,1)
	Rx = (r1,r2,r3)
	return np.array(Rx)

# Input in radians
def Ry(th):
	c, s = np.cos(th), np.sin(th)
	r1 = (c,0,-s)
	r2 = (0,1,0)
	r3 = (s,0,c)
	Ry = (r1,r2,r3)
	return np.array(Ry)

# Input in radians
def Rx(th):
	c, s = np.cos(th), np.sin(th)
	r1 = (1,0,0)
	r2 = (0,c,s)
	r3 = (0,-s,c)
	Rz = (r1,r2,r3)
	return np.array(Rz)

def find_position():
	print("<Locating>")
	lat = 0
	lon = 0
	direction = 'n'
	with open('image_data.txt','r') as data:
		for line in data.readlines():
			# print("line: " + line)
			# "(\d+\.\d+)"+" "+"(\d+\.\d+)"+" "+"(\d+\.\d+)"+" "+
			img_name = image['name'][:-4]
			# print("img: " + img_name)
			expression = img_name+"\.jpg (-?\d+\.\d+ ?)(-?\d+\.\d+ ?)(-?\d+\.\d+ ?)(-?\d+\.\d+ ?)(-?\d+\.\d+ ?)(-?\d+\.\d+ ?)"
			# pattern = re.compile(expression)
			# print(pattern.match(line))
			# print(re.findall(expression,line))
			groups = re.match(expression,str(line))
			# print("groups: " + str(groups))
			if(not groups == None):
				alt = float(groups.group(1))
				lat = float(groups.group(2))
				lon = float(groups.group(3))
				yaw = float(groups.group(4))
				pitch = float(groups.group(5))
				roll = float(groups.group(6))
				Ryaw, Rpitch, Rroll = Rz(np.radians(yaw)), Rx(np.radians(pitch)), Ry(np.radians(roll))
				R = np.matmul(Ryaw,np.matmul(Rpitch,Rroll))
				# print(R)
				target_loc_img_plane_x = (pic_loc[0]-xsize/2)/PPM
				target_loc_img_plane_y = (ysize/2-pic_loc[1])/PPM
				target_loc_img_plane = np.array((target_loc_img_plane_x,target_loc_img_plane_y))
				target_loc = np.array((target_loc_img_plane[0]*alt/F,target_loc_img_plane[1]*alt/F,-alt))
				# print(target_loc)

				rotated_loc = np.matmul(R,target_loc)
				target_lat = rotated_loc[0]*M_TO_LAT
				target_lon = rotated_loc[1]*M_TO_LON

				direction = np.floor(((90-yaw + angle)%360 + 22.5)/45) # IN DEGREES
				print(str(yaw)+", "+str(angle)+", "+str(direction))
				direction = direction_lookup[direction]

				return 0,0,direction




def kill():
	print('exiting')
	cv2.destroyAllWindows()
	sys.exit()




def callback(data)
	img = bridge.imgmsg_to_cv2(data.image.data, desired_encoding=data.image.encoding)
	    

	croppedImg = cv2.imread(image['path'])
	ysize,xsize,zsize = croppedImg.shape
	pic_loc = (0,0)
	offset_x = 0
	offset_y = 0
	cropped = crop() # Cropped img dict
	oriented,angle = orient() # Oriented img dict
	shape,shape_color,alpha,alpha_color = classify() 
	lat,lon,direction = find_position()
	uav_image()
	print("")

	
	output_im = bridge.cv2_to_imgmsg(img, encoding="8UC1")
	
    submit_pub.publish(output_im)

# cv2.namedWindow("image")
# popupwindow = cv2.namedWindow("Classification")

direction_lookup = {0:'n',1:'ne',2:'e',3:'se',4:'s',5:'sw',6:'w',7:'nw'}



def main():

	computer_num = 1
	node_name = 'reciever_node'+str(computer_num)
	pub_name = '/ask_'+str(computer_num)
	sub_name = '/image_ask_'+str(computer_num)

	rospy.init_node(node_name, anonymous=True)

    rospy.Subscriber(sub_name, Image, callback)
    asking_pub = rospy.Publisher(pub_name, Empty, queue_size=1)
    submit_pub = rospy.Publisher('/interop_submission', uav_image, queue_size=1)
    
    bridge = CvBridge()

	global image_recieved
	image_recieved = False    

    while True:
    	key = cv2.waitKey(0)
    	if key == 'space':
    		msg = Empty()
    		asking_pub.publish(msg)

    		image_recieved = False
    		time.sleep(5)
    		if image_recieved == True:
    			while True:
    				if image_recieved == False:
    					break
    					time.sleep(.5)


    		




    	elif key == 'q':
    		break








if __name__ == '__main__':
    main()