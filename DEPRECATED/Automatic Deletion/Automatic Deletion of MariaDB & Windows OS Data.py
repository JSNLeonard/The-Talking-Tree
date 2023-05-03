# Importing OS, Time, Datetime, and MariaDB libraries.
import os
import time
import datetime
import mariadb

# Set the path of the directory to monitor for deletion.
directory_path = "C:/Users/Jason/Documents/College Year 4/Semester 2/Final Year Project/The-Talking-Tree/Images"

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
    
except Exception as e:
    print("Error connecting to the database:", e)
    exit()

while True:
    try:
        # Get the current date and time.
        now = datetime.datetime.now()

        # Subtract 12 hours from the current date and time.
        time_threshold = now - datetime.timedelta(hours=12)

        # Construct a SQL query to delete records older than the time threshold.
        sql = "DELETE FROM user_data WHERE timestamp < %s"
        values = (time_threshold,)

        # Execute the query and commit the changes.
        cur.execute(sql, values)
        conn.commit()

        # Print the number of rows deleted.
        print(f"{cur.rowcount} rows deleted from the database.")

        # Loop through the files in the directory.
        for file_name in os.listdir(directory_path):
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

        # Sleep for 1 hour before checking again.
        time.sleep(60 * 60) # Sleep for 1 hour.

    except KeyboardInterrupt:
        # Catch keyboard interrupt to stop the script gracefully.
        break

    except Exception as e:
        # Catch all other exceptions and print an error message.
        print("An error occurred. Retrying in 10 seconds...")
        print(e)
        time.sleep(10)

# Close the database connection.
cur.close()
conn.close()