import os
import shutil


def create_directories(base_dir):
    # Define directory structure
    structure = {
        'app': [
            '__init__.py',
            'models',
            'routes',
            'services',
            'utils',
            'static',
            'templates',
            'main.py',
            'settings.py'
        ],
        'app/models': [
            '__init__.py',
            'asset.py',
            'user.py'
        ],
        'app/routes': [
            '__init__.py',
            'assets.py',
            'users.py'
        ],
        'app/services': [
            '__init__.py',
            'asset_service.py',
            'user_service.py'
        ],
        'app/utils': [
            '__init__.py',
            'database.py',
            'auth.py'
        ],
        'scripts': [],
        'tests': [],
        'migrations': [],
    }

    try:
        for dir_path, files in structure.items():
            full_dir_path = os.path.join(base_dir, dir_path)

            if not os.path.exists(full_dir_path):
                os.makedirs(full_dir_path)
                print(f"Created directory: {full_dir_path}")

            for file in files:
                if file.endswith('.py'):
                    open(os.path.join(full_dir_path, file), 'a').close()
                    print(f"Created file: {os.path.join(full_dir_path, file)}")
                else:
                    os.makedirs(os.path.join(full_dir_path, file))
                    print(f"Created directory: {os.path.join(full_dir_path, file)}")

        print("Directory structure creation completed successfully!")

    except Exception as e:
        print(f"Error creating directory structure: {e}")


if __name__ == "__main__":
    base_dir = "/home/anonymous/Documents/FixedAssets/FixedAssets_BE"
    create_directories(base_dir)
