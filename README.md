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

Camera Module V2

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/49892a29-7812-4f58-9ef4-b4bfb36b5bc1)

Pan-Tilt HAT Kit by Pimoroni

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/fe7052b9-ece9-4f4d-a837-a9fc1e4b4d97)

# Algorithms Used

Local Binary Pattern Histogram (LBPH)

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/5eb9b23b-273c-42cb-aa2a-afe2a4f4d98b)

Face_Recognition 128-Dimensional Feature Vectors

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/1ce77ceb-8ff1-4493-b0f1-192bc60c0374)

# Design of System

Block Diagram

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/b80353e9-1b82-42d5-94c2-a5f424a5d403)

Circuit Diagram

![image](https://github.com/JSNLeonard/The-Talking-Tree/assets/48300764/62dc1504-7ad4-4ea4-a3ab-ef8703bfa54c)

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
