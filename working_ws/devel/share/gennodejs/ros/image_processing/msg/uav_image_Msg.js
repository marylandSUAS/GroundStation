// Auto-generated. Do not edit!

// (in-package image_processing.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class uav_image_Msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.image = null;
      this.pos = null;
      this.hdg = null;
      this.type = null;
      this.shape = null;
      this.background_color = null;
      this.alpha = null;
      this.alpha_color = null;
    }
    else {
      if (initObj.hasOwnProperty('image')) {
        this.image = initObj.image
      }
      else {
        this.image = new sensor_msgs.msg.Image();
      }
      if (initObj.hasOwnProperty('pos')) {
        this.pos = initObj.pos
      }
      else {
        this.pos = new geometry_msgs.msg.Point();
      }
      if (initObj.hasOwnProperty('hdg')) {
        this.hdg = initObj.hdg
      }
      else {
        this.hdg = 0.0;
      }
      if (initObj.hasOwnProperty('type')) {
        this.type = initObj.type
      }
      else {
        this.type = '';
      }
      if (initObj.hasOwnProperty('shape')) {
        this.shape = initObj.shape
      }
      else {
        this.shape = '';
      }
      if (initObj.hasOwnProperty('background_color')) {
        this.background_color = initObj.background_color
      }
      else {
        this.background_color = '';
      }
      if (initObj.hasOwnProperty('alpha')) {
        this.alpha = initObj.alpha
      }
      else {
        this.alpha = '';
      }
      if (initObj.hasOwnProperty('alpha_color')) {
        this.alpha_color = initObj.alpha_color
      }
      else {
        this.alpha_color = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type uav_image_Msg
    // Serialize message field [image]
    bufferOffset = sensor_msgs.msg.Image.serialize(obj.image, buffer, bufferOffset);
    // Serialize message field [pos]
    bufferOffset = geometry_msgs.msg.Point.serialize(obj.pos, buffer, bufferOffset);
    // Serialize message field [hdg]
    bufferOffset = _serializer.float32(obj.hdg, buffer, bufferOffset);
    // Serialize message field [type]
    bufferOffset = _serializer.string(obj.type, buffer, bufferOffset);
    // Serialize message field [shape]
    bufferOffset = _serializer.string(obj.shape, buffer, bufferOffset);
    // Serialize message field [background_color]
    bufferOffset = _serializer.string(obj.background_color, buffer, bufferOffset);
    // Serialize message field [alpha]
    bufferOffset = _serializer.string(obj.alpha, buffer, bufferOffset);
    // Serialize message field [alpha_color]
    bufferOffset = _serializer.string(obj.alpha_color, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type uav_image_Msg
    let len;
    let data = new uav_image_Msg(null);
    // Deserialize message field [image]
    data.image = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset);
    // Deserialize message field [pos]
    data.pos = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset);
    // Deserialize message field [hdg]
    data.hdg = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [type]
    data.type = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [shape]
    data.shape = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [background_color]
    data.background_color = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [alpha]
    data.alpha = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [alpha_color]
    data.alpha_color = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.Image.getMessageSize(object.image);
    length += object.type.length;
    length += object.shape.length;
    length += object.background_color.length;
    length += object.alpha.length;
    length += object.alpha_color.length;
    return length + 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'image_processing/uav_image_Msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '80f79040cac03c9f8cbab283c780ba9a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensor_msgs/Image image
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new uav_image_Msg(null);
    if (msg.image !== undefined) {
      resolved.image = sensor_msgs.msg.Image.Resolve(msg.image)
    }
    else {
      resolved.image = new sensor_msgs.msg.Image()
    }

    if (msg.pos !== undefined) {
      resolved.pos = geometry_msgs.msg.Point.Resolve(msg.pos)
    }
    else {
      resolved.pos = new geometry_msgs.msg.Point()
    }

    if (msg.hdg !== undefined) {
      resolved.hdg = msg.hdg;
    }
    else {
      resolved.hdg = 0.0
    }

    if (msg.type !== undefined) {
      resolved.type = msg.type;
    }
    else {
      resolved.type = ''
    }

    if (msg.shape !== undefined) {
      resolved.shape = msg.shape;
    }
    else {
      resolved.shape = ''
    }

    if (msg.background_color !== undefined) {
      resolved.background_color = msg.background_color;
    }
    else {
      resolved.background_color = ''
    }

    if (msg.alpha !== undefined) {
      resolved.alpha = msg.alpha;
    }
    else {
      resolved.alpha = ''
    }

    if (msg.alpha_color !== undefined) {
      resolved.alpha_color = msg.alpha_color;
    }
    else {
      resolved.alpha_color = ''
    }

    return resolved;
    }
};

module.exports = uav_image_Msg;
