import mariadb
import os
from flask import Flask, request
import time

app = Flask(__name__, template_folder='C:/xampp/htdocs')

@app.route('/send_info', methods=['POST'])
def send_info():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    question = request.form['question']
    photo = request.files['photo']
    timestamp = int(time.time())
    
    photo_filename = f"{first_name}_{last_name}_{timestamp}.png"
    photo_folder = "C:/Users/Jason/Documents/College Year 4/Final Year Project/WebApp/Images/"
    photo_path = os.path.join(photo_folder, photo_filename)
    if not os.path.exists(photo_folder):
        os.makedirs(photo_folder)
    try:
        photo.save(photo_path)
        print('File saved:', photo_path)
    except Exception as e:
        print('Error saving file:', e)
    
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
    except Exception as e:
        print("Error inserting data into database:", e)
    finally:
        conn.close()
        
    return "Thank you for your submission!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)