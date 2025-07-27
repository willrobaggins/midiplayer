import shutil
from datetime import datetime
import os
import sys

def copy_and_archive_file(username):
    source_file_path = "output.mid"
    output_folder = "output_archive"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_file_path = os.path.join(output_folder, f"{username + "_" + timestamp}.mid")

    try:
        shutil.copy2(source_file_path, destination_file_path)
        print(f"File copied successfully to {destination_file_path}")
    except FileNotFoundError:
        print(f"Error: The source file '{source_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = " ".join(sys.argv[1:])
    copy_and_archive_file(username)