#!/usr/bin/env python3
import sys
import rospy
import cv2
import message_filters
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class detection:

	def __init__(self):
		self.bridge = CvBridge()
		self.img_sub = rospy.Subscriber('/usb_cam/image_raw', Image, self.img_callback, queue_size = 1)
		self.april_pub = rospy.Publisher('/april_img', Image, queue_size = 10, latch=True)
		self.yolo_pub = rospy.Publisher('/yolo_img', Image, queue_size = 10, latch=True)

	def img_callback(self, img):
		try:
			cv_img = self.bridge.imgmsg_to_cv2(img, "bgr8")
		except CvBridgeError as e:
			print(e)


def main(args):
	rospy.init_node('detector', anonymous=True)
	det = detection()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
		
if __name__ == '__main__':
	main(sys.argv)
