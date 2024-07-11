import os
import shutil


def move_files():
    base_dir = "/home/anonymous/Documents/FixedAssets/FixedAssets_BE"

    # Mapping of files to their destination directories
    file_mappings = {
        "__init__.py": "app",
        "main.py": "app",
        "settings.py": "app",
        "requirements.txt": base_dir,
        ".env": base_dir,
        "db.sqlite3": "app",
        "manage.py": "app",
        "scripts": base_dir,
        "migrations": base_dir,
        "tests": base_dir
    }

    # File extensions and their destination directories
    file_types = {
        ".py": "app",
        ".html": "app/templates",
        ".sqlite3": "app",
    }

    for root, _, files in os.walk(base_dir):
        for filename in files:
            source_path = os.path.join(root, filename)
            destination_dir = None

            if filename in file_mappings:
                destination_dir = os.path.join(base_dir, file_mappings[filename])
            else:
                file_ext = os.path.splitext(filename)[1]
                if file_ext in file_types:
                    destination_dir = os.path.join(base_dir, file_types[file_ext])

            if destination_dir:
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
