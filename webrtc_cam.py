import streamlit as st 
import cv2
from streamlit_webrtc import webrtc_streamer 
import numpy as np
import av 

class VideoProcessor:
    def recv(self,frame):
        image = frame.to_ndarray(format = "bgr24")
        edging = cv2.cvtColor(cv2.Canny(image, 100, 100), cv2.COLOR_GRAY2BGR)
        return av.VideoFrame.from_ndarray(edging,format = "bgr24")
    
webrtc_streamer(key = "key",  rtc_configuration={
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    },video_processor_factory= VideoProcessor)
