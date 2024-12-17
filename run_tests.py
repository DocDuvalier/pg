import os
import subprocess

# Get all Python files in the current directory and subdirectories
def get_all_python_files():
    python_files = []
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def run_python_file(file_path):
    try:
        result = subprocess.run(
            ["python", file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        print(f"Success: {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error in {file_path}: {e.stderr.decode()}")

if __name__ == "__main__":
    python_files = get_all_python_files()
    for file_path in python_files:
        run_python_file(file_path)
#python run_tests.py
