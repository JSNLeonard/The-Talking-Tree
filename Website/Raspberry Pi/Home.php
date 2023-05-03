<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="StyleEdit.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <div class="video-background">
        <video autoplay loop muted>
            <source src="Trees.mp4" type="video/mp4">
        </video>
    </div>
    <div id="gdpr-modal" class="modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2>GDPR Data Usage Policy</h2>
            <p>This application collects and uses data in the following ways:</p>
            <p><b>1. To create a unique experience for each individual.</b></p>
            <p><b>2. To identify who the user is when the camera detects them.</b></p>
            <p>By using this application, you consent to the collection and use of your data in accordance with this policy.</p>
            <p>Your data will be immediately deleted after the Tree answers your question or reads out your story.</p>
            <div>
                <input type="checkbox" id="consent-checkbox">
                <label for="consent-checkbox">I give my consent</label>
            </div>
            <br>
            <button id="consent-btn" disabled>Continue</button>
        </div>
    </div>
    <div class="text-overlay" style="z-index: 1;">
        <h1>Welcome to the "Talking Tree"</h1>
        <h5>Select an Option Below to Begin</h5>
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true') { window.location.href = 'Question.php'; } else { modal.style.display = 'block'; }" value="Ask A Question">
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true') { window.location.href = 'Story.php'; } else { modal.style.display = 'block'; }" value="Tell A Story">
        <br>
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true') { window.location.href = 'About.php'; } else { modal.style.display = 'block'; }" value="About">
    </div>
    <script>
        var modal = document.getElementById("gdpr-modal");
        var closeBtn = document.getElementsByClassName("close-btn")[0];
        var consentBtn = document.getElementById("consent-btn");
        var consentCheckbox = document.getElementById("consent-checkbox");
        if (localStorage.getItem("consent") === "true") {
            modal.style.display = "none";
        } else {
            modal.style.display = "block";
        }
        closeBtn.onclick = function() {
            modal.style.display = "none";
        };
        consentCheckbox.onchange = function() {
            consentBtn.disabled = !consentCheckbox.checked;
        };
        consentBtn.onclick = function() {
            modal.style.display = "none";
            localStorage.setItem("consent", "true");
            window.location.href = 'Home.php';
        };
    </script>
</body>
</html>