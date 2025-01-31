Hand Gesture Volume Control

Description

This project allows users to control their system volume using hand gestures detected via a webcam. It leverages OpenCV for computer vision, MediaPipe for hand tracking, and Pycaw to manipulate system audio levels. By measuring the distance between the thumb and index finger, the volume level is adjusted in real-time.

Features

Uses a webcam to track hand movements.

Detects thumb and index finger positioning.

Calculates the distance between fingers to set system volume.

Provides visual feedback via OpenCV.

Displays real-time FPS and volume percentage.

Requirements

Python 3.x

OpenCV (cv2)

NumPy

Pycaw (for audio control)

HandTrackingModule (custom module for hand detection)

MediaPipe (for hand tracking)

Installation

Clone this repository:

git clone <https://github.com/prakriti82/Volumecontroller>

Navigate to the project directory:

cd hand-gesture-volume-control

Install dependencies:

pip install opencv-python numpy comtypes pycaw mediapipe

Usage

Run the script:

python main.py

Place your hand in front of the camera.

Adjust the volume by moving your thumb and index finger closer or farther apart.

Press 'q' to exit.

How It Works

The script captures frames from the webcam.

MediaPipe detects the hand and identifies key landmarks.

The distance between the thumb tip and index finger tip is calculated.

This distance is mapped to the system volume range using pycaw.

The volume level is updated dynamically as the user moves their fingers.



A sample demonstration can be found here (add your demo video link).

License

This project is open-source and available under the MIT License.
