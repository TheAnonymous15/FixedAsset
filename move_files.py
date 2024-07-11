import os
import shutil


def move_files():
    base_dir = "/home/anonymous/Documents/FixedAssets/FixedAssets_BE"

    # Dictionary mapping file extensions to destination directories
    file_types = {
        ".py": "app",  # Python scripts go to the app directory
        ".html": "app/templates",  # HTML templates go to app/templates directory
        ".sqlite3": "app",  # SQLite database goes to app directory
        # Add more file types and their respective directories as needed
    }

    for root, _, files in os.walk(base_dir):
        for filename in files:
            source_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1]

            if file_extension in file_types:
                destination_dir = os.path.join(base_dir, file_types[file_extension])
                destination_path = os.path.join(destination_dir, filename)

                try:
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)

                    shutil.move(source_path, destination_path)
                    print(f"Moved {filename} to {destination_path}")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")


if __name__ == "__main__":
    move_files()
