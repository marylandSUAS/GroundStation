#!/usr/bin/env python
import Tkinter
import rospy
from PIL import Image,ImageTk
import ttk
from GroundStation.msg import uav_image_Msg
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, PoseStamped, PointStamped, Point
from std_msgs.msg import Empty, Int32, Float32

import cv2
import numpy as np
import time
import sys
from cv_bridge import CvBridge, CvBridgeError
# import cv2
# import random

#TODO: Fix directory situation
#TODO: Fix implementation of multiple computers? Necessary?


class AutoScrollbar(ttk.Scrollbar):
    ''' Hides scrollbar when not in use '''
    def set(self, lo, hi):
        ''' Set auto hiding of scrollbar '''
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
            # self.Tkinter.call("grid", "remove", self)
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        ''' Raise error if widget cannot be packed '''
        raise Tkinter.TclError('Cannot use pack with this widget')

    def place(self, **kw):
        ''' Raise error if widget cannot be placed '''
        raise Tkinter.TclError('Cannot use place with this widget')

class Classify(Tkinter.Toplevel):
    ''' Classify and save ROI '''
    def __init__(self,image,ref):
        
        # Initialize Toplevel window
        self.toplevel = Tkinter.Toplevel.__init__(self)
        self.title('Image Classifier')
        self.image = image
        self.ref = ref
        # Create labels for user entry
        Tkinter.Label(self,text="Shape Type").grid(row=0)
        Tkinter.Label(self,text="Shape Color").grid(row=1)
        Tkinter.Label(self,text="Alphanumeric Type").grid(row=2)
        Tkinter.Label(self,text="Alphanumeric Color").grid(row=3)
        Tkinter.Label(self,text="Alphanumeric Orientation").grid(row=4)
        
        # Create user entry widget
        self.shape_type = Tkinter.Entry(self)
        self.shape_color = Tkinter.Entry(self)
        self.alphanumeric_type = Tkinter.Entry(self)
        self.alphanumeric_color = Tkinter.Entry(self)
        self.orientation = Tkinter.Entry(self)
        self.shape_type.grid(row=0,column=1)
        self.shape_color.grid(row=1,column=1)
        self.alphanumeric_type.grid(row=2,column=1)
        self.alphanumeric_color.grid(row=3,column=1)
        self.orientation.grid(row=4,column=1)
        
        # Create button to save classified image 
        Tkinter.Button(self,text='Save',command=self.save).grid(row=5,column=1,sticky='w',pady=4)
    
    def save(self):
        ''' Saves the classified image '''
        shape_type = self.shape_type.get()
        shape_color = self.shape_color.get()
        alphanumeric_type = self.alphanumeric_type.get()
        alphanumeric_color = self.alphanumeric_color.get()
        orientation = self.orientation.get()
        filename = shape_type + '%' + shape_color +'%' + alphanumeric_type + '%' + alphanumeric_color + '%' + orientation +'.jpg'
        self.image.save(filename)
        self.destroy()
        self.ref.next_image()
        
class ManualClassifierGUI(ttk.Frame):
    ''' GUI to display an image with scroll, zoom and manually classifying functionalities '''
    def __init__(self, window, path):
        
        # ROS Initialization and queue
        rospy.init_node('gui_listener1')
        rospy.Subscriber("Images", uav_image_Msg, self.add_image)
        self.queue = []
        self.count = 0

        # Initialize main frame
        ttk.Frame.__init__(self, master=window)
        self.master.title('Manual Classifier')

        # Create vertical and horizontal scrollbars for canvas
        vertical_bar = AutoScrollbar(self.master, orient='vertical')
        horizontal_bar = AutoScrollbar(self.master, orient='horizontal')
        vertical_bar.grid(row=0, column=1, sticky='ns')
        horizontal_bar.grid(row=1, column=0, sticky='we')
        
        # Create canvas to place image
        self.canvas = Tkinter.Canvas(self.master, highlightthickness=0,xscrollcommand=horizontal_bar.set, yscrollcommand=vertical_bar.set)
        
        # Create a grid geometry manager to fill up the entire canvas
        self.canvas.grid(row=0, column=0, sticky='nswe')
        
        self.canvas.update()
        
        # Place scrollbars to canvas
        vertical_bar.configure(command=self.scroll_y) 
        horizontal_bar.configure(command=self.scroll_x)
        
        # Enable configurable option for the canvas created
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        
        # Bind events to the Canvas
        self.canvas.bind('<Configure>',self.display_image) # Canvas configures to the image size
        # self.canvas.bind('<ButtonPress-1>',self.current) # Get current coordinates for scrolling with mouse
        # self.canvas.bind('<B1-Motion>',self.drag) # Move to a coordinate in the image
        self.canvas.bind('<ButtonPress-1>',self.start) # Get starting point to draw bounding box
        self.canvas.bind('<B1-Motion>',self.drag) # Move to a coordinate in the image
        self.canvas.bind('<ButtonRelease-1>',self.stop) # Get the last point to draw bounding box
        self.canvas.bind('<MouseWheel>',self.scroll_zoom) # Zoom the image by scrolling the image using mouse
        
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.x = 0
        self.y = 0
        
        # Load image
        self.image = Image.open(path)
        self.w, self.h = self.image.size
        
        # Define zoom size 
        self.image_scale = 1.0
        self.zoomsize = 2.0
        
        # Place the image in frame
        self.image_frame = self.canvas.create_rectangle(0, 0, self.w, self.h, width=0)
        self.display_image()
        #rospy.spin()
    #Receives an image message. Saves image to folder. Adds filepath to a queue. An alternative implementation if this proves to be too slow is to add the images to memory but that is asking for trouble in my opinon.
    def add_image(self, uim):
        filepath = '/home/imaging/GroundPics/Picture' + str(self.count) +'.jpg'
        cv2.imwrite(filepath,  cv_image)
        self.queue.append(filepath)
        self.count = self.count+1
        
    
    #Called whenever a user finishes processing an image. Uses next image.
    def next_image(self):
        next_im_path = self.queue.pop(0)
        self.image = Image.open("Picture2.jpeg")
        self.canvas.coords(self.rect, 0, 0, 0, 0)
        self.canvas.delete(self.image_final)
        self.display_image()
              

    def scroll_y(self, *args, **kwargs):
        ''' Scroll canvas vertically '''
        self.canvas.yview(*args, **kwargs)
        self.display_image()

    def scroll_x(self, *args, **kwargs):
        ''' Scroll canvas horizontally '''
        self.canvas.xview(*args, **kwargs)
        self.display_image()

    # def current(self, event):
        # ''' Get current coordinates for scrolling with the mouse '''
        # self.canvas.scan_mark(event.x, event.y)

    # def drag(self, event):
        # ''' Move window to new position '''
        # self.canvas.scan_dragto(event.x, event.y, gain=1)
        # self.display_image() 
        
    def start(self, event):
        ''' Get starting point to draw bounding box '''
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        # create rectangle if not yet exist
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')          

    def drag(self, event):
        ''' Drag and draw the desired bounding box '''
        # Get current mouse event position
        current_x = self.canvas.canvasx(event.x)
        current_y = self.canvas.canvasy(event.y)
        
        # Check if the mouse event is near any of the edges of the canvas in order to determine scroll
        if event.x > 0.9*self.canvas.winfo_width():
            self.canvas.xview_scroll(1, 'units') 
        elif event.x < 0.1*self.canvas.winfo_width():
            self.canvas.xview_scroll(-1, 'units')
        if event.y > 0.9*self.canvas.winfo_height():
            self.canvas.yview_scroll(1, 'units') 
        elif event.y < 0.1*self.canvas.winfo_height():
            self.canvas.yview_scroll(-1, 'units')

        # Increase rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, current_x, current_y) 
        # self.display_image()

    def stop(self, event):
        ''' Get the final point of bounding box and crop the ROI '''
        roi = self.canvas.bbox(self.rect)
        cropped_roi = self.image.crop(roi)
        # cropped_roi.save('cropped.jpg')
        Classify(cropped_roi, self)
        pass  

    def scroll_zoom(self, event):
        ''' Zoom with mouse wheel '''
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        
        # Obtain canvas bounding box coordinates
        image_frame_bounding_box = self.canvas.bbox(self.image_frame)
        
        # Check if mousewheel event is within the image
        if image_frame_bounding_box[0] < x < image_frame_bounding_box[2] and image_frame_bounding_box[1] < y < image_frame_bounding_box[3]: pass  
        else: return
        zoom = 1.0
        # Respond to Windows mousewheel event
        if event.delta == -120:  # scroll down
            limit = min(self.w, self.h)
            if int(limit * self.image_scale) < 25: return  # image is less than 25 pixels
            self.image_scale/= self.zoomsize
            zoom/= self.zoomsize
        if event.delta == 120:  # scroll up
            limit = min(self.canvas.winfo_width(), self.canvas.winfo_height())
            if limit < self.image_scale: return
            self.image_scale *= self.zoomsize
            zoom *= self.zoomsize
        self.canvas.scale('all', x, y, zoom, zoom)  # rescale all canvas objects
        self.display_image()

    def display_image(self, event=None):
        ''' Display image on the Canvas '''
        # Obtain canvas bounding box coordinates
        image_frame_bounding_box = self.canvas.bbox(self.image_frame)
        
        # Convert root window coordinates into canvas coordinates to find scroll region
        window_to_canvas = (self.canvas.canvasx(0),
                            self.canvas.canvasy(0),
                            self.canvas.canvasx(self.canvas.winfo_width()),
                            self.canvas.canvasy(self.canvas.winfo_height()))
        
        # Determine scroll region
        scrollregion = [min(image_frame_bounding_box[0], window_to_canvas[0]), min(image_frame_bounding_box[1], window_to_canvas[1]),  
                        max(image_frame_bounding_box[2], window_to_canvas[2]), max(image_frame_bounding_box[3], window_to_canvas[3])]
        if scrollregion[0] == window_to_canvas[0] and scrollregion[2] == window_to_canvas[2]:
            scrollregion[0] = image_frame_bounding_box[0]
            scrollregion[2] = image_frame_bounding_box[2]
        if scrollregion[1] == window_to_canvas[1] and scrollregion[3] == window_to_canvas[3]:  
            scrollregion[1] = image_frame_bounding_box[1]
            scrollregion[3] = image_frame_bounding_box[3]    
        self.canvas.configure(scrollregion=scrollregion)
        
        # Get image coordinates, convert to PhotoImage and display on canvas
        x_left_topcorner = max(window_to_canvas[0] - image_frame_bounding_box[0], 0)
        y_left_topcorner = max(window_to_canvas[1] - image_frame_bounding_box[1], 0)
        x_right_bottomcorner = min(window_to_canvas[2], image_frame_bounding_box[2]) - image_frame_bounding_box[0]
        y_right_bottomcorner = min(window_to_canvas[3], image_frame_bounding_box[3]) - image_frame_bounding_box[1]
        if int(x_right_bottomcorner - x_left_topcorner) > 0 and int(y_right_bottomcorner - y_left_topcorner) > 0:  
            x = min(int(x_right_bottomcorner/self.image_scale),self.w)   
            y = min(int(y_right_bottomcorner/self.image_scale),self.h)
            image_display = self.image.crop((int(x_left_topcorner/self.image_scale),int(y_left_topcorner/self.image_scale),x,y))
            convert_image = ImageTk.PhotoImage(image_display.resize((int(x_right_bottomcorner - x_left_topcorner),int(y_right_bottomcorner - y_left_topcorner))))
            self.image_final = self.canvas.create_image(max(window_to_canvas[0],image_frame_bounding_box[0]), max(window_to_canvas[1],image_frame_bounding_box[1]),
                                               anchor='nw', image=convert_image)
            
            self.canvas.lower(self.image_final) 
            self.canvas.convert_image = convert_image 

path = 'trees.jpeg' 
root = Tkinter.Tk()
app = ManualClassifierGUI(root, path=path)
root.mainloop()
