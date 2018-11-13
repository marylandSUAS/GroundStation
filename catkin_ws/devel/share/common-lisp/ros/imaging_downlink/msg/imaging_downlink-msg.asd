
(cl:in-package :asdf)

(defsystem "imaging_downlink-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "uav_image_Msg" :depends-on ("_package_uav_image_Msg"))
    (:file "_package_uav_image_Msg" :depends-on ("_package"))
  ))