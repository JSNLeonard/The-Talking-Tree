<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="StyleEdit.css">
    <script src="https://cdn.jsdelivr.net/npm/@capacitor/core@3.5.0/dist/capacitor.js"></script>
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

    <!-- Form to submit questions and take a selfie -->
    <form method="post" action="http://192.168.0.46:5000/send_story" enctype="multipart/form-data" onsubmit="submitFormOnce(this); return false;">
        <div class="form-group">
            <h1>Talking Tree (Story)</h1>
            <h5>Enter Your First & Last Name, Share A Story & Take A Selfie Below</h5>
            <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Enter Your First Name" required>
            <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Enter Your Last Name" required>
        </div>
        <div class="form-group">
            <input type="text" class="form-control" name="story" id="story" placeholder="Share A Story" required>
        </div>
        <div class="form-group">
            <input type="file" accept="image/*" capture="camera" id="photo-upload-input" name="photo" required>
            <button type="submit">Upload Information</button>
        </div>
        <div class="form-group">
            <input type="button" class="frosty-btn" onclick="window.location.href = 'index.php';" value="Home">
            <input type="button" class="frosty-btn" onclick="window.location.href = 'About.php';" value="About">
        </div>
    </form>
    <script>

        // JavaScript code to handle taking a photo and submitting the form.
        error_reporting(E_ALL);
        ini_set('display_errors', 1);
        const { Camera } = Capacitor.Plugins;

        // Function to take a photo using the device's camera.
        async function takePhoto() {
            try {
                const image = await Camera.getPhoto({
                    quality: 90,
                    allowEditing: false,
                    resultType: Capacitor.CameraResultType.DataUrl,
                    source: Capacitor.CameraSource.Camera,
                });
                return image.dataUrl;
            } catch (error) {
                console.error(error);
            }
        }
        const photoUploadForm = document.querySelector('form');

        // Event listener for the form submission.
        photoUploadForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const photoUploadInput = document.getElementById('photo-upload-input');
            const file = photoUploadInput.files[0];
            if (file) {

                // Take a photo and get the data URL.
                const photoDataUrl = await takePhoto();

                // Create a FormData object to send the form data.
                const formData = new FormData();
                formData.append('photo', photoDataUrl);

                // Send a POST request with the form data.
                const response = await fetch('http://192.168.0.46:5000/send_story', {
                    method: 'POST',
                    body: formData,
                });
                console.log(response);
            }
        });
    </script>
</body>
</html>
<?php

// PHP code to handle MQTT communication and form data processing.
error_reporting(E_ALL);
ini_set('display_errors', 1);
require("C:/xampp/htdocs/phpMQTT.php");

// Define MQTT broker information.
$broker = 'a40883bf34564fb493b81df755dd41cb.s2.eu.hivemq.cloud';
$port = 8883;
$message_topic = 'Message';
$image_topic = 'Image';
$client_id = 'php-mqtt-' . mt_rand(0, 1000);
$username = 'JasonLeonard';
$password = '2!fP5zqS$hf8Qw';

// Function to send form data as a message to MQTT.
function sendFormDataToMQTT($first_name, $last_name, $story, $image_filename)
{
    global $broker, $port, $message_topic, $image_topic, $client_id, $username, $password;

    // Create an MQTT client instance.
    $mqtt = new phpMQTT($broker, $port, $client_id);
    if ($mqtt->connect(true, NULL, $username, $password)) {

        // Publish the form data as a message.
        $payload = "$first_name,$last_name,$story,$image_filename";
        $mqtt->publish($message_topic, $payload, 1);

        // Send the image over MQTT.
        sendImageToMQTT($first_name, $last_name, $image_filename);
        $mqtt->close();
    }
}

// Function to send the image over MQTT.
function sendImageToMQTT($first_name, $last_name, $image_filename)
{
    global $broker, $port, $image_topic, $client_id, $username, $password;

    // Check if the image file exists.
    if (file_exists($image_filename)) {

        // Read the image data.
        $image_data = file_get_contents($image_filename);

        // Generate a new image filename with a timestamp.
        $new_image_filename = $first_name . '_' . $last_name . '_' . time() . '.jpg';

        // Create an MQTT client instance.
        $mqtt = new phpMQTT($broker, $port, $client_id);
        if ($mqtt->connect(true, NULL, $username, $password)) {

            // Publish the image data to the image topic.
            $mqtt->publish($image_topic, $image_data, 1, false, [
                'responseTopic' => 'ImageReceived',
                'correlationData' => $new_image_filename
            ]);

            // Rename the image file.
            rename($image_filename, 'Images/' . $new_image_filename);
            $mqtt->close();
        }
    } else {
        echo "Image file not found: $image_filename";
    }
}

// Get the form data.
$first_name = isset($_POST['first_name']) ? $_POST['first_name'] : '';
$last_name = isset($_POST['last_name']) ? $_POST['last_name'] : '';
$story = isset($_POST['story']) ? $_POST['story'] : '';
$image_filename = isset($_FILES['photo']['tmp_name']) ? $_FILES['photo']['tmp_name'] : '';

// Send the form data to MQTT.
sendFormDataToMQTT($first_name, $last_name, $story, $image_filename);

// Redirect back to the home page.
exit();
?>