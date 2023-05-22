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

    <!-- GDPR Modal -->
    <div id="gdpr-modal" class="modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>  <!-- Close button symbol (X) -->
            <h2>GDPR Policy</h2>
            <p>This app collects and utilizes data as follows:</p>
            <p><b>1. To personalize user experiences.</b></p>
            <p><b>2. To identify users through camera detection.</b></p>
            <p>By using this application, you consent to the data collection and usage in accordance with this policy.</p>
            <p>Your data will be promptly deleted after 12 hours or when the Talking Tree responds to your question or story.</p>
            <div>
                <input type="checkbox" id="consent-checkbox">  <!-- Checkbox for giving consent (16 years or older) -->
                <label for="consent-checkbox">I give my consent (if you are 16 years or older)</label>
            </div>
            <br>
            <div>
                <input type="checkbox" id="consent-checkbox-child">  <!-- Checkbox for giving assent (under 16 years old) -->
                <label for="consent-checkbox-child">I give my assent (if you are under 16 years old)</label>
            </div>
            <br>
            <div id="parent-name-container" style="display: none;">  <!-- Container for parent's name (hidden by default) -->
                <label for="parent-first-name">Parent's First Name:</label>
                <input type="text" id="parent-first-name" required>  <!-- Input field for parent's first name -->
                <br>
                <br>
                <label for="parent-last-name">Parent's Last Name:</label>
                <input type="text" id="parent-last-name" required>  <!-- Input field for parent's last name -->
            </div>
            <br>
            <button id="consent-btn" disabled>Continue</button>  <!-- Button to continue (disabled by default) -->
        </div>
    </div>

    <!-- Text overlay and buttons -->
    <div class="text-overlay" style="z-index: 1;">
        <h1>Welcome to the "Talking Tree"</h1>
        <h5>Select an Option Below to Begin</h5>
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true' || localStorage.getItem('consentChild') === 'true') { window.location.href = 'Question.php'; } else { modal.style.display = 'block'; }" value="Ask A Question">
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true' || localStorage.getItem('consentChild') === 'true') { window.location.href = 'Story.php'; } else { modal.style.display = 'block'; }" value="Tell A Story">
        <br>
        <input type="submit" class="frosty-btn" onclick="if (localStorage.getItem('consent') === 'true' || localStorage.getItem('consentChild') === 'true') { window.location.href = 'About.php'; } else { modal.style.display = 'block'; }" value="About">
    </div>

    <!-- JavaScript code -->
    <script>

        // Getting the required elements.
        var modal = document.getElementById("gdpr-modal");
        var closeBtn = document.getElementsByClassName("close-btn")[0];
        var consentBtn = document.getElementById("consent-btn");
        var consentCheckbox = document.getElementById("consent-checkbox");
        var consentCheckboxChild = document.getElementById("consent-checkbox-child");
        var parentNameContainer = document.getElementById("parent-name-container");
        var parentFirstNameInput = document.getElementById("parent-first-name");
        var parentLastNameInput = document.getElementById("parent-last-name");
        
        // Check if consent has been given previously.
        if (localStorage.getItem("consent") === "true" || localStorage.getItem("consentChild") === "true") {
            modal.style.display = "none"; // Hide the GDPR modal if consent has been given.
        } else {
            modal.style.display = "block"; // Display the GDPR modal if consent has not been given.
        }

        // Close modal when close button is clicked.
        closeBtn.onclick = function() {
            modal.style.display = "none";
        };

        // Enable/disable consent button based on checkbox states and display parent name fields if necessary.
        consentCheckbox.onchange = function() {
            consentBtn.disabled = !(consentCheckbox.checked || consentCheckboxChild.checked);
            parentNameContainer.style.display = consentCheckboxChild.checked ? "block" : "none";
            if (!consentCheckboxChild.checked) {
                parentFirstNameInput.value = "";
                parentLastNameInput.value = "";
            }
        };
        
        // Enable/disable assent button based on checkbox states and display parent name fields if necessary.
        consentCheckboxChild.onchange = function() {
            consentBtn.disabled = !(consentCheckbox.checked || consentCheckboxChild.checked);
            parentNameContainer.style.display = consentCheckboxChild.checked ? "block" : "none";
            if (!consentCheckboxChild.checked) {
                parentFirstNameInput.value = "";
                parentLastNameInput.value = "";
            }
        };

        // Handle consent button click event.
        consentBtn.onclick = function() {
            modal.style.display = "none";

            if (consentCheckbox.checked) {
                localStorage.setItem("consent", "true"); // Store consent status in local storage.
            }

            if (consentCheckboxChild.checked) {
                var parentFirstName = parentFirstNameInput.value.trim();
                var parentLastName = parentLastNameInput.value.trim();
                if (parentFirstName === "" || parentLastName === "") {
                    alert("Please enter both the parent's first name and last name.");
                    return;
                }
                localStorage.setItem("consentChild", "true"); // Store child's consent status inn local storage.
                localStorage.setItem("parentFirstName", parentFirstName); // Store parent's first name in local storage.
                localStorage.setItem("parentLastName", parentLastName); // Store parent's last name in local storage.
            }

            // Redirect to the index.php page.
            window.location.href = 'index.php';
        };
    </script>
</body>
</html>