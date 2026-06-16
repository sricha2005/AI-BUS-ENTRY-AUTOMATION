import streamlit as st
import cv2

st.set_page_config(page_title="Bus Entry System")

st.title("AI Bus Entry Automation System")

if st.button("Start Camera"):

    cap = None

    for i in range(5):
        temp = cv2.VideoCapture(i)
        if temp.isOpened():
            cap = temp
            st.success(f"Camera Found at Index {i}")
            break

    if cap is None:
        st.error("Camera Not Detected")
    else:
        frame_window = st.image([])

        while True:
            ret, frame = cap.read()

            if not ret:
                st.error("Cannot Read Camera")
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_window.image(frame)

        cap.release()