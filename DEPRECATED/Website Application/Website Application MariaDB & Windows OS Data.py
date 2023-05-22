# Name: Jason Leonard

# Project Name: Talking Tree

# File Name: Automatic Deletion of MariaDB & Windows OS Data.py

# File Description: The web application has two routes, one for submitting questions and one for submitting stories, both of which handle POST requests.
# ################# The script starts by importing the required modules: mariadb, os, Flask, request, and time.
# ################# Then it initializes a new Flask application instance with the name "name" and sets the template folder to "/var/www/html".
# ################# After that, it creates two routes using the @app.route decorator, one for handling POST requests to "/send_question" and one for handling POST requests to "/send_story".
# ################# Each route defines a function to handle the request.
# ################# The function retrieves the values of the form fields submitted in the POST request using the request.form object, and then saves the uploaded image to a specified folder on the server using the os module.
# ################# Next, the function connects to the MariaDB database, inserts the form data into the 'user_data' table, and closes the database connection.
# ################# Finally, the function returns a message to indicate that the form was successfully submitted.

# Import the required modules for the code to work, these modules are MariaDB, OS, Flask, Request, and Time.
import mariadb
import os
from flask import Flask, request
import time

# Initialize a new Flask application instance.
app = Flask(__name__, template_folder='C:/xampp/htdocs')

# Create a new route for handling POST requests.
@app.route('/send_question', methods=['POST'])
def send_question():

    # Retrieve the values of the form fields.
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    question = request.form['question']
    photo = request.files['photo']
    timestamp = int(time.time())
    
    # Create a unique filename for the uploaded photo.
    photo_filename = f"{first_name}_{last_name}_{timestamp}.png"
    photo_folder = "C:/Users/Jason/Documents/College Year 4/Final Year Project/The-Talking-Tree/Images/"
    photo_path = os.path.join(photo_folder, photo_filename)

    # Create the folder to store the uploaded photo if it doesn't already exist.
    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)
    
    # Save the uploaded photo to the specified folder.
    try:
        photo.save(photo_path)
        print('File saved:', photo_path)
    
    # Catch any exception that may occur while saving a file locally.
    except Exception as e:
        print('Error saving file:', e)
    
    # Connect to the MariaDB database and insert the form data into the 'user_data' table.
    try:
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
        print("Data inserted into database")

    # Catch any exception that may occur while inserting data into a database.
    except Exception as e:
        print("Error inserting data into database:", e)
    
    # Close the database connection.
    finally:
        conn.close()
    
    # Return a message to indicate that the form was successfully submitted.
    return "Thank You For Your Submission and Question!"

# Create a new route for handling POST requests.
@app.route('/send_story', methods=['POST'])
def send_story():

    # Retrieve the values of the form fields.
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    story = request.form['story']
    photo = request.files['photo']
    timestamp = int(time.time())
    
    # Create a unique filename for the uploaded photo.
    photo_filename = f"{first_name}_{last_name}_{timestamp}.png"
    photo_folder = "C:/Users/Jason/Documents/College Year 4/Final Year Project/The-Talking-Tree/Images/"
    photo_path = os.path.join(photo_folder, photo_filename)

    # Create the folder to store the uploaded photo if it doesn't already exist.
    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)

    # Save the uploaded photo to the specified folder.
    try:
        photo.save(photo_path)
        print('File saved:', photo_path)
    
    # Catch any exception that may occur while saving a file locally.
    except Exception as e:
        print('Error saving file:', e)
    
    # Connect to the MariaDB database and insert the form data into the 'user_data' table.
    try:
        conn = mariadb.connect(
            user="root",
            password="TalkingTree2023",
            host="localhost",
            port=3306,
            database="TalkingTree"
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO user_data (first_name, last_name, story, image, timestamp) VALUES (?, ?, ?, ?, NOW())", (first_name, last_name, story, photo_filename))
        conn.commit()
        print("Data inserted into database")
    
    # Catch any exception that may occur while inserting data into a database.
    except Exception as e:
        print("Error inserting data into database:", e)
    
    # Close the database connection.
    finally:
        conn.close()

    # Return a message to indicate that the form was successfully submitted.
    return "Thank You For Your Submission and Story!"

# Run the Flask application.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)