; Auto-generated. Do not edit!


(cl:in-package imaging_downlink-msg)


;//! \htmlinclude uav_image_Msg.msg.html

(cl:defclass <uav_image_Msg> (roslisp-msg-protocol:ros-message)
  ((image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (pos
    :reader pos
    :initarg :pos
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (hdg
    :reader hdg
    :initarg :hdg
    :type cl:float
    :initform 0.0)
   (type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (shape
    :reader shape
    :initarg :shape
    :type cl:string
    :initform "")
   (background_color
    :reader background_color
    :initarg :background_color
    :type cl:string
    :initform "")
   (alpha
    :reader alpha
    :initarg :alpha
    :type cl:string
    :initform "")
   (alpha_color
    :reader alpha_color
    :initarg :alpha_color
    :type cl:string
    :initform ""))
)

(cl:defclass uav_image_Msg (<uav_image_Msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <uav_image_Msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'uav_image_Msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name imaging_downlink-msg:<uav_image_Msg> is deprecated: use imaging_downlink-msg:uav_image_Msg instead.")))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:image-val is deprecated.  Use imaging_downlink-msg:image instead.")
  (image m))

(cl:ensure-generic-function 'pos-val :lambda-list '(m))
(cl:defmethod pos-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:pos-val is deprecated.  Use imaging_downlink-msg:pos instead.")
  (pos m))

(cl:ensure-generic-function 'hdg-val :lambda-list '(m))
(cl:defmethod hdg-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:hdg-val is deprecated.  Use imaging_downlink-msg:hdg instead.")
  (hdg m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:type-val is deprecated.  Use imaging_downlink-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'shape-val :lambda-list '(m))
(cl:defmethod shape-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:shape-val is deprecated.  Use imaging_downlink-msg:shape instead.")
  (shape m))

(cl:ensure-generic-function 'background_color-val :lambda-list '(m))
(cl:defmethod background_color-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:background_color-val is deprecated.  Use imaging_downlink-msg:background_color instead.")
  (background_color m))

(cl:ensure-generic-function 'alpha-val :lambda-list '(m))
(cl:defmethod alpha-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:alpha-val is deprecated.  Use imaging_downlink-msg:alpha instead.")
  (alpha m))

(cl:ensure-generic-function 'alpha_color-val :lambda-list '(m))
(cl:defmethod alpha_color-val ((m <uav_image_Msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader imaging_downlink-msg:alpha_color-val is deprecated.  Use imaging_downlink-msg:alpha_color instead.")
  (alpha_color m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <uav_image_Msg>) ostream)
  "Serializes a message object of type '<uav_image_Msg>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pos) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'hdg))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'type))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'shape))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'shape))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'background_color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'background_color))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'alpha))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'alpha))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'alpha_color))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'alpha_color))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <uav_image_Msg>) istream)
  "Deserializes a message object of type '<uav_image_Msg>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pos) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'hdg) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'shape) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'shape) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'background_color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'background_color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'alpha) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'alpha) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'alpha_color) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'alpha_color) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<uav_image_Msg>)))
  "Returns string type for a message object of type '<uav_image_Msg>"
  "imaging_downlink/uav_image_Msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'uav_image_Msg)))
  "Returns string type for a message object of type 'uav_image_Msg"
  "imaging_downlink/uav_image_Msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<uav_image_Msg>)))
  "Returns md5sum for a message object of type '<uav_image_Msg>"
  "80f79040cac03c9f8cbab283c780ba9a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'uav_image_Msg)))
  "Returns md5sum for a message object of type 'uav_image_Msg"
  "80f79040cac03c9f8cbab283c780ba9a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<uav_image_Msg>)))
  "Returns full string definition for message of type '<uav_image_Msg>"
  (cl:format cl:nil "sensor_msgs/Image image~%geometry_msgs/Point pos ~%float32 hdg~%string type~%string shape~%string background_color~%string alpha~%string alpha_color~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'uav_image_Msg)))
  "Returns full string definition for message of type 'uav_image_Msg"
  (cl:format cl:nil "sensor_msgs/Image image~%geometry_msgs/Point pos ~%float32 hdg~%string type~%string shape~%string background_color~%string alpha~%string alpha_color~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <uav_image_Msg>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pos))
     4
     4 (cl:length (cl:slot-value msg 'type))
     4 (cl:length (cl:slot-value msg 'shape))
     4 (cl:length (cl:slot-value msg 'background_color))
     4 (cl:length (cl:slot-value msg 'alpha))
     4 (cl:length (cl:slot-value msg 'alpha_color))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <uav_image_Msg>))
  "Converts a ROS message object to a list"
  (cl:list 'uav_image_Msg
    (cl:cons ':image (image msg))
    (cl:cons ':pos (pos msg))
    (cl:cons ':hdg (hdg msg))
    (cl:cons ':type (type msg))
    (cl:cons ':shape (shape msg))
    (cl:cons ':background_color (background_color msg))
    (cl:cons ':alpha (alpha msg))
    (cl:cons ':alpha_color (alpha_color msg))
))
