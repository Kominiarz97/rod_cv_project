import cv2
import imutils
import requests
from datetime import datetime
import report
from report import report_obstacle
from db_conn import db_connect
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import edit_image, downsize
from on_rails_anomaly_detection import rails_mask, rails_area, rails_anomaly
from gps import get_position



def detect_1(original, edited, rails_org):

