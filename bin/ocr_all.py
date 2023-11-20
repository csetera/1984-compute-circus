import os
from os.path import abspath, basename, dirname, join, splitext
import subprocess

def ocr(path, config_file, data):
    base, ext = splitext(path)
    print("Processing " + path)
    subprocess.run(["tesseract", path, base, "--psm", "6", "--tessdata-dir", data, config_file])
    os.rename(base + ".txt", base + ".bas")

def main():
    if os.environ['TESSDATA_BEST'] is None:
        print("TESSDATA_BEST not set")
        exit(1)

    data = os.environ['TESSDATA_BEST']

    script_path = abspath(__file__)
    script_dir = dirname(script_path)
    config_file = join(script_dir, "ocr_config.txt")

    root_dir = dirname(script_dir)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".png"):
                ocr(join(root, file), config_file, data)

if __name__ == "__main__":
    main()
