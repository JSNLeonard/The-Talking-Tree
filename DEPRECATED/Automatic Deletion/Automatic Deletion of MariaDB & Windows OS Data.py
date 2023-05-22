# Name: Jason Leonard

# Project Name: Talking Tree

# File Name: Automatic Deletion of MariaDB & Windows OS Data.py

# File Description: This code is a Python script that monitors a directory for files older than 12 hours and deletes them.
# ################# It also deletes records from a MariaDB database table older than 12 hours.

# Importing OS, Time, Datetime, and MariaDB libraries.
import os
import time
import datetime
import mariadb

# Connect to the MariaDB database.
try:
    conn = mariadb.connect(
        user="root",
        password="TalkingTree2023",
        host="localhost",
        port=3306,
        database="TalkingTree"
    )
    cur = conn.cursor()
    print("Connected to the database!")
    
# Catches any exceptions that occur while connecting to the database.
except Exception as e:
    print("Error connecting to the database:", e)
    exit()

# Set the path of the directory to monitor for deletion.
directory_path = "C:/Users/Jason/Documents/College Year 4/Final Year Project/The-Talking-Tree/Images/"

# Runs an infinite while loop while the following is true.
while True:
    try:

        # Get the current date and time.
        now = datetime.datetime.now()

        # Subtract 12 hours from the current date and time.
        time_threshold = now - datetime.timedelta(hours=12)

        # Loop through the files in the directory.
        for file_name in os.listdir(directory_path):

            # Skip the "Default.jpg" file.
            if file_name == "Default.jpg":
                continue
            file_path = os.path.join(directory_path, file_name)

            # Get the last modification time of the file.
            modified_time = os.path.getmtime(file_path)

            # Convert the modified time to a datetime object.
            modified_time = datetime.datetime.fromtimestamp(modified_time)

            # Check if the file is older than 12 hours.
            if modified_time < time_threshold:

                # Delete the file.
                os.remove(file_path)
                print(f"{file_name} deleted from the directory.")

        # Construct a SQL query to delete records older than the time threshold.
        sql = "DELETE FROM user_data WHERE timestamp < %s"
        values = (time_threshold,)

        # Execute the query and commit the changes.
        cur.execute(sql, values)
        conn.commit()

        # Print the number of rows deleted.
        print(f"{cur.rowcount} rows deleted from the database.")

        # Sleep for 1 hour before checking again.
        time.sleep(60 * 60) # Sleep for 1 hour.
        
    # Catch keyboard interrupt to stop the script gracefully.
    except KeyboardInterrupt:
        break
    
    # Catch all other exceptions and print an error message.
    except Exception as e:
        print("An error occurred. Retrying in 10 seconds...")
        print(e)
        time.sleep(10)

# Close the database connection.
cur.close()
conn.close()