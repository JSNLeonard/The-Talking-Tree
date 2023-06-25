# The Talking Tree Final Year Project

My final year project was part of a larger project overall known as the Talking Tree. My obective was to create an interactive system that allows users to submit information such as their first name, last name, question/story and a selfie of their face through a web application. This information is processed, stored in a MariaDB database, and their image is stored locally on a Raspberry Pi 4 through an embedded Python application. The system uses a Raspberry Pi 4 along with both a Camera Module V2 and a Pan-Tilt HAT Kit by Pimoroni to detect user's facial locations and adjust the camera position to focus and track the recognised face of a user. After the interaction, the system securely deletes the user's information.

The final product will be an interactive entity "Talking Tree", that will combine being able to follow a user's face and speak to them using a speech service, which will answer the user's question or read out their story.

The rationale for this project is to build upon a previous iteration that successfully showcased a similar concept. The previous iteration, developed by members of the TU Dublin team, was featured in the Dublin Maker Fair. It involved an interactive entity with a face and a manual speech service so that an individual controlling the “entity” could engage with user’s when they approached it. Building upon this foundation, the Talking Tree project aims to explore the possibilities of using modern technology to create an even more immersive and captivating experience for users.

# YouTube Video Description

Short Video Description: https://www.youtube.com/watch?v=SqtavO1BXxg

Long Video Description: https://www.youtube.com/watch?v=pRr75gRfAX0

# Hardware Used

Raspberry Pi 4

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/e306a698-b34c-4d45-a5bf-bcc6d528b88d)

The Raspberry Pi 4 is a powerful, low-cost single-board computer that has gained popularity in recent years due to its versatility and ease of use. It features a quad-core 64-bit ARM Cortex-A72 CPU, up to 8GB of RAM, and various input/output ports, making it ideal for a wide range of applications, from hobby projects to commercial products. In my project, I am using the Raspberry Pi 4 as the main computing platform to run my face recognition and detection software along with running an embedded Flask Python application to receive user information from the web application. This is because the Raspberry Pi 4 offers a cost-effective and flexible solution that can handle the processing requirements of my project while being small and easy to integrate into the overall system design. Additionally, the Raspberry Pi 4 has a large and supportive community that provided me with a wealth of resources and tutorials to help get me started and troubleshoot any issues that had risen during development.

Camera Module V2

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/49892a29-7812-4f58-9ef4-b4bfb36b5bc1)

The Camera Module V2 is another key technology that I am using in my project. This camera module is specifically designed for the Raspberry Pi 4 and provides high-quality image and video capture capabilities. It is compact in size and can be easily integrated with the Raspberry Pi 4, making it an ideal choice for my project. The camera module features an 8-megapixel Sony IMX219 image sensor that supports 1080p video at 30 frames per second and 720p at 60 frames per second. With the Camera Module V2, I am able to capture clear and accurate images of faces, which is essential for my face recognition and detection software.

Pan-Tilt HAT Kit by Pimoroni

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/fe7052b9-ece9-4f4d-a837-a9fc1e4b4d97)

The Pan-Tilt HAT Kit by Pimoroni is a hardware add-on for the Raspberry Pi 4 that allows users to control the orientation of a camera or other device. It features two servo motors that can be used to pan and tilt a camera with precision and accuracy. The kit also comes with a mounting plate and screws, making it easy to attach to the Raspberry Pi 4 and camera module of my choice.

In my project, I have integrated the Pan-Tilt HAT Kit to work alongside the Camera Module V2. I have programmed the HAT to move the camera towards a face when it has been detected by the camera. This allows for the camera to track a person's movements, keeping them in frame and in focus. The integration of these two components allows for greater functionality and flexibility in my project, as it enables the camera to move in response to a detected face, acting as the “eye” of the entity, providing a more immersive and interactive experience.

# Main Algorithms/Software Solutions Used

OpenCV Python Image Processing Library

OpenCV (Open-Source Computer Vision) is a popular open-source computer vision and image processing library that is widely used in various applications, including robotics, surveillance systems, and self-driving cars. It provides a wide range of functions and algorithms for image and video analysis, such as image filtering, segmentation, feature extraction, object detection, and recognition. OpenCV is written in C++ and has bindings for various programming languages, including Python, which makes it accessible to developers with different backgrounds.

In this project, I am using the OpenCV Python library to perform face detection and recognition tasks with the help of the Camera Module V2 and Pan-Tilt HAT Kit by Pimoroni. OpenCV has built-in algorithms that can detect faces, such as the Haar Cascade and Local Binary Pattern Histogram (LBPH) algorithm. These algorithms are highly effective and widely used in the computer vision community for face detection tasks, making them a natural choice for my project. With OpenCV, I am able to easily implement these algorithms and integrate them with the Camera Module V2 and the Pan-Tilt HAT Kit, allowing my system to accurately detect and track faces in real time.

I have decided to use the LBPH algorithm over the more traditional Haar Cascade classifier. LBPH is a more robust face detection algorithm than Haar Cascade because it can handle variations in lighting and facial expressions more effectively. Haar Cascade is known to have difficulty detecting faces under certain lighting conditions or when faces have certain expressions. [32] LBPH is also less computationally expensive than Haar Cascade, which means it can run faster on the Raspberry Pi 4, making it a better fit for real-time face detection and recognition. For these reasons, I have chosen to use LBPH over Haar Cascade in my project.

Local Binary Pattern Histogram (LBPH)

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/5eb9b23b-273c-42cb-aa2a-afe2a4f4d98b)

Local Binary Pattern Histogram (LBPH) is a feature extraction algorithm used in computer vision and image processing to analyse textures in images. It was first proposed in 1990 as a texture spectrum model and has since become a simple yet effective algorithm that characterises the local texture of an image by comparing the intensity of a pixel with its surrounding pixels. The LBPH operator outputs a binary pattern that encodes the texture information of the local region around the pixel being analysed. The LBPH histogram is a global representation of the texture information in the image, which can be used for various applications such as face recognition, object detection, and texture classification. In this project, LBPH is used to detect faces in the video stream captured by the Camera Module V2 and trigger the Pan-Tilt HAT to move towards the detected face.

Face_Recognition 128-Dimensional Feature Vectors

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/1ce77ceb-8ff1-4493-b0f1-192bc60c0374)

The Face_Recognition library is a powerful and easy-to-use open-source library for face recognition that is built using DLIB. It is designed to work with Python and allows developers to build facial recognition systems quickly and easily. The library uses a deep learning model to encode faces into 128-dimensional feature vectors that can be used to compare faces and identify individuals. These feature vectors are highly accurate and can be used to identify faces even in challenging lighting conditions, with facial hair, or when wearing glasses.

I tried other facial recognition methods such as taking multiple images of one individual and passing them into an array. However, I found that nothing came close to the accuracy of the Face_Recognition library. The only caveat of the library is that it is quite slow and requires significant computational power. When I initially attempted to use it for tracking the user's face, it was too slow for the Raspberry Pi 4 to compute. Therefore, I had to find an alternative solution using the LBPH algorithm for real-time face tracking, while using the Face_Recognition library for identifying the individual's face that was passed to the Raspberry Pi 4 via the web application.

# Design of System

Block Diagram

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/b80353e9-1b82-42d5-94c2-a5f424a5d403)

In this block diagram, the Raspberry Pi 4 serves as the main component, powered by a 5V5A power supply. It connects to the Camera Module V2 through the CSI port and the Pan-Tilt HAT through the GPIO pins. The Camera Module V2 captures high-quality images and videos, while the Pan-Tilt HAT enables pan and tilt movements.

Circuit Diagram

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/62dc1504-7ad4-4ea4-a3ab-ef8703bfa54c)

To connect the Raspberry Pi 4 with the Pan-Tilt HAT and the Camera Module V2, there are specific ports that need to be used on each device. First, the Camera Module V2 is connected to the Raspberry Pi 4 using the Camera Serial Interface (CSI) port. The CSI port is located on the Raspberry Pi 4 board, and the Camera Module V2 connects to it through a ribbon cable. The next step is to connect the Pan-Tilt HAT to the Raspberry Pi 4's General-Purpose Input/Output (GPIO) pins. The Pan-Tilt HAT is attached to the GPIO pins using a 40-pin header that comes with the Pan-Tilt HAT, and it is essential to ensure that the header is placed correctly to avoid damaging either the Raspberry Pi 4 or the Pan-Tilt HAT. Once the Pan-Tilt HAT is attached, the servos for the pan and tilt axis can be connected to the Pan-Tilt HAT's servo headers. By correctly connecting the CSI port, GPIO pins, and servo headers, the Raspberry Pi 4, Pan-Tilt HAT, and Camera Module V2 can all be connected and work together seamlessly.

Raspberry Pi 4 with Camera Module V2 and Pan-Tilt HAT Kit by Pimoroni

![IMG_3905](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/413eb071-f864-4b5b-b481-0148cbd95320)

Video of System Operating

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/9624529b-3552-4c25-9cb2-9826aa5ca0e7)

# Design of Web Application

GDPR Modal Prompt

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/8dec9c07-b29c-44bd-86d6-1d07254b5a81)

GDPR Modal Prompt (Consent)

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/a5286d59-823c-493b-964b-b0ac37342e54)

GDPR Modal Prompt (Assent/Parental Consent)

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/dd950cd6-3b62-40e4-b4cb-8e62405c3c05)

Home Page

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/23429696-49c5-47e2-a7fc-0b5af89c3ab2)

Question Page

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/c12c03f9-fb5d-4654-b5e2-7631221703cc)

Story Page

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/215917fe-5039-4321-bcc3-bd9ee6e03d61)

Camera Viewfinder (CapacitorJS)

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/06c66390-4bfa-42a4-905f-23bb1bd08015)

About Page

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/c92584da-4994-4b93-9b5d-762ce4b24ac5)
