;; Auto-generated. Do not edit!


(when (boundp 'image_processing::uav_image_Msg)
  (if (not (find-package "IMAGE_PROCESSING"))
    (make-package "IMAGE_PROCESSING"))
  (shadow 'uav_image_Msg (find-package "IMAGE_PROCESSING")))
(unless (find-package "IMAGE_PROCESSING::UAV_IMAGE_MSG")
  (make-package "IMAGE_PROCESSING::UAV_IMAGE_MSG"))

(in-package "ROS")
;;//! \htmlinclude uav_image_Msg.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass image_processing::uav_image_Msg
  :super ros::object
  :slots (_image _pos _hdg _type _shape _background_color _alpha _alpha_color ))

(defmethod image_processing::uav_image_Msg
  (:init
   (&key
    ((:image __image) (instance sensor_msgs::Image :init))
    ((:pos __pos) (instance geometry_msgs::Point :init))
    ((:hdg __hdg) 0.0)
    ((:type __type) "")
    ((:shape __shape) "")
    ((:background_color __background_color) "")
    ((:alpha __alpha) "")
    ((:alpha_color __alpha_color) "")
    )
   (send-super :init)
   (setq _image __image)
   (setq _pos __pos)
   (setq _hdg (float __hdg))
   (setq _type (string __type))
   (setq _shape (string __shape))
   (setq _background_color (string __background_color))
   (setq _alpha (string __alpha))
   (setq _alpha_color (string __alpha_color))
   self)
  (:image
   (&rest __image)
   (if (keywordp (car __image))
       (send* _image __image)
     (progn
       (if __image (setq _image (car __image)))
       _image)))
  (:pos
   (&rest __pos)
   (if (keywordp (car __pos))
       (send* _pos __pos)
     (progn
       (if __pos (setq _pos (car __pos)))
       _pos)))
  (:hdg
   (&optional __hdg)
   (if __hdg (setq _hdg __hdg)) _hdg)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:shape
   (&optional __shape)
   (if __shape (setq _shape __shape)) _shape)
  (:background_color
   (&optional __background_color)
   (if __background_color (setq _background_color __background_color)) _background_color)
  (:alpha
   (&optional __alpha)
   (if __alpha (setq _alpha __alpha)) _alpha)
  (:alpha_color
   (&optional __alpha_color)
   (if __alpha_color (setq _alpha_color __alpha_color)) _alpha_color)
  (:serialization-length
   ()
   (+
    ;; sensor_msgs/Image _image
    (send _image :serialization-length)
    ;; geometry_msgs/Point _pos
    (send _pos :serialization-length)
    ;; float32 _hdg
    4
    ;; string _type
    4 (length _type)
    ;; string _shape
    4 (length _shape)
    ;; string _background_color
    4 (length _background_color)
    ;; string _alpha
    4 (length _alpha)
    ;; string _alpha_color
    4 (length _alpha_color)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; sensor_msgs/Image _image
       (send _image :serialize s)
     ;; geometry_msgs/Point _pos
       (send _pos :serialize s)
     ;; float32 _hdg
       (sys::poke _hdg (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _type
       (write-long (length _type) s) (princ _type s)
     ;; string _shape
       (write-long (length _shape) s) (princ _shape s)
     ;; string _background_color
       (write-long (length _background_color) s) (princ _background_color s)
     ;; string _alpha
       (write-long (length _alpha) s) (princ _alpha s)
     ;; string _alpha_color
       (write-long (length _alpha_color) s) (princ _alpha_color s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; sensor_msgs/Image _image
     (send _image :deserialize buf ptr-) (incf ptr- (send _image :serialization-length))
   ;; geometry_msgs/Point _pos
     (send _pos :deserialize buf ptr-) (incf ptr- (send _pos :serialization-length))
   ;; float32 _hdg
     (setq _hdg (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _shape
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _shape (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _background_color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _background_color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _alpha
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _alpha (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _alpha_color
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _alpha_color (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get image_processing::uav_image_Msg :md5sum-) "80f79040cac03c9f8cbab283c780ba9a")
(setf (get image_processing::uav_image_Msg :datatype-) "image_processing/uav_image_Msg")
(setf (get image_processing::uav_image_Msg :definition-)
      "sensor_msgs/Image image
geometry_msgs/Point pos 
float32 hdg
string type
string shape
string background_color
string alpha
string alpha_color

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :image_processing/uav_image_Msg "80f79040cac03c9f8cbab283c780ba9a")


