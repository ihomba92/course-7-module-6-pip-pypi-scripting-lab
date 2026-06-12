from datetime import datetime
import os
import requests


    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
def fetch_data():
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        if response.status_code == 200:
            return response.json() 
        return {}  # Return an empty dictionary if the request fails
  
def generate_log(data):
    # STEP 1: Validate input
    if not isinstance(data, list):
        print("Error: Input data must be a list of strings.")
        return

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
# --- Demonstration of the integrated script ---
if __name__ == "__main__":
    # 1. Start with your baseline application logs
    log_entries = ["User logged in", "User updated profile"]
    
    # 2. Fetch external data from the API
    print("Fetching data from API...")
    post_data = fetch_data()
    if post_data:
        log_entries.append("Successfully fetched data from API")
    else:
        log_entries.append("Failed to fetch data from API")
    
    # 3. Extract the title and append it as a new log entry
    post_title = post_data.get("title", "No title found")
    log_entries.append(f"Fetched API Post Title: {post_title}")
    
    # 4. Generate the log file containing both internal and external events
    generate_log(log_entries)