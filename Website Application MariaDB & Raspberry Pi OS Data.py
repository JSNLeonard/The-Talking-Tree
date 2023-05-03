# Import the required modules for the code to work, these modules are MariaDB, OS, Flask, Request, and Time.
import mariadb
import os
from flask import Flask, request
import time

# Initialize a new Flask application instance.
app = Flask(__name__, template_folder='/home/xampp/htdocs')

# Create a new route for handling POST requests.
@app.route('/send_info', methods=['POST'])
def send_info():
    # Retrieve the values of the form fields.
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    question = request.form['question']
    photo = request.files['photo']
    timestamp = int(time.time())
    
    # Create a unique filename for the uploaded photo.
    photo_filename = f"{first_name}_{last_name}_{timestamp}.png"
    photo_folder = "/home/pi/Documents/The-Talking-Tree/Images"
    photo_path = os.path.join(photo_folder, photo_filename)
    
    # Create the folder to store the uploaded photo if it doesn't already exist.
    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)
    
    try:
        # Save the uploaded photo to the specified folder.
        photo.save(photo_path)
        print('File Saved:', photo_path)
    except Exception as e:
        print('Error Saving File:', e)
    
    try:
        # Connect to the MariaDB database and insert the form data into the 'user_data' table.
        conn = mariadb.connect(
            user="root",
            password="TalkingTree2023",
            host="localhost",
            port=3306,
            database="TalkingTree"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO user_data (first_name, last_name, question, image, timestamp) VALUES (?, ?, ?, ?, NOW())", (first_name, last_name, question, photo_filename))
        conn.commit()
        print("Data Inserted Into Database")
    except Exception as e:
        print("Error Inserting Data Into Database:", e)
    finally:
        # Close the database connection.
        conn.close()

    # Return a message to indicate that the form was successfully submitted.
    return "Thank You For Your Submission!"

# Run the Flask application.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)