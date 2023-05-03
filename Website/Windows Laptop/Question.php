<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="StyleEdit.css">
    <script src="https://cdn.jsdelivr.net/npm/@capacitor/core@3.5.0/dist/capacitor.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <div class="video-background">
        <video autoplay loop muted>
            <source src="Trees.mp4" type="video/mp4">
        </video>
    </div>
    <form method="post" action="http://192.168.0.41:5000/send_info" enctype="multipart/form-data" onsubmit="submitFormOnce(this); return false;">
        <div class="form-group">
            <h1>Talking Tree (Question)</h1>
            <h5>Enter Your First & Last Name, Ask a Question & Take a Selfie Below</h5>
            <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Enter Your First Name" required>
            <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Enter Your Last Name" required>
          </div>
        <div class="form-group">
            <input type="text" class="form-control" name="question" id="question" placeholder="Ask A Question" required>
        </div>
        <div class="form-group">
            <input type="file" accept="image/*" capture="camera" id="photo-upload-input" name="photo" required>
            <button type="submit">Upload Information</button>
        </div>
        <div class="form-group">
            <input type="submit" class="frosty-btn" onclick="window.location.href = 'Home.php';" value="Home">
            <input type="submit" class="frosty-btn" onclick="window.location.href = 'About.php';" value="About">
        </div>
    </form>
    <script>
    const { Camera } = Capacitor.Plugins;
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
    const photoUploadForm = document.getElementById('photo-upload-form');
    photoUploadForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const photoUploadInput = document.getElementById('photo-upload-input');
      const file = photoUploadInput.files[0];
      if (file) {
        const photoDataUrl = await takePhoto();
        const formData = new FormData();
        formData.append('photo', photoDataUrl);
        const response = await fetch('/api/upload-photo', {
          method: 'POST',
          body: formData,
        });
        console.log(response);
      }
    });
  </script>  
</body>
</html>