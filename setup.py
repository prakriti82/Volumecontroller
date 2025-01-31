from setuptools import setup, find_packages

setup(
    name="HandVolumeControl",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "mediapipe",
        "pycaw",
        "comtypes"
    ],
    author="Your Name",
    description="A hand tracking based volume control system using OpenCV and Pycaw.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
