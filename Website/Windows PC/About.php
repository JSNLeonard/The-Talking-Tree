<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="StyleEdit.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

    <!-- Styling for the background image -->
    <style>
        body {
            background-image: url('Forest.jpg');
            background-size: cover;
        }
    </style>
    <div>
        <div class="about-section" style="z-index: 1;">
            <h2>What is the Talking Tree Project?</h2>
            <p class="justify" style="z-index: 1;">This project is an interactive exhibit that aims to engage visitors in STEM
                (science, technology, engineering, and mathematics) concepts through outdoor interactions.
                The exhibit is located on the Grangegorman campus and features an animatronic "entity"
                (Talking Tree) that has been designed to "look" at the person it is talking to.
                The student working on the project used a Raspberry Pi 4 to create a system that controls a camera.
                This camera will be able to pan, tilt, and zoom (PTZ) so that the "eye" of the "entity"
                always points towards a person when given images of that person as a reference. The goal of the project is to
                create an immersive and interactive experience that encourages visitors to learn more about STEM
                and the technology behind it.</p>
            <p><b>Made by:</b> Jason Leonard</p>
            <p><b>Course Code:</b> TU819/4</p>
            <p><b>Year:</b> 2023</p>
            <input type="submit" class="frosty-btn-about" onclick="window.location.href = 'index.php';" value="Home">
        </div>
    </div>
</body>
</html>