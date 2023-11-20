import os
from os.path import abspath, basename, dirname, join, splitext
import subprocess

def ocr(path):
    base, ext = splitext(path)
    print("Processing " + path)
    subprocess.run(["convert", path, "-bordercolor", "White", "-border", "10x10", path])

def main():
    script_path = abspath(__file__)
    script_dir = dirname(script_path)
    root_dir = dirname(script_dir)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".png"):
                ocr(join(root, file))

if __name__ == "__main__":
    main()
