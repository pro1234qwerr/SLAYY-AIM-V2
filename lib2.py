import os
import json
import time
import shutil
import zipfile
import subprocess
import urllib.request

try:
    newest_version = "https://raw.githubusercontent.com/pro1234qwerr/SLAYY-AIM-V2/main/current_version.txt"
    req = urllib.request.Request(newest_version, headers={'Cache-Control': 'no-cache'})
    response = urllib.request.urlopen(req)
    remote_version = response.read().decode().strip()

    file_paths = [
        "./library.py",
        "./yolo.cfg",
        "./yolo.weights",
        "./req.txt",
        "./LICENSE",
        "./README.md",
        "./current_version.txt",
        "./lang.json",
        "./Icon.ico"
        "./keyauth.py"
    ]

    localv_path = "localv.json"
    config_path = "config.json"

    if not os.path.exists(localv_path) or not os.path.exists(config_path) or not os.path.exists(file_paths[1]):
        local_version = "0.0.0"
        data = {
            "version": remote_version,
            "pip": False,
            "python": False,
            "language": "english",
            "first_launch": True,
            "activated": True
        }
        with open(localv_path, "w") as file:
            json.dump(data, file)
        config = {
            "aimbot": True,
            "detection": True,
            "pinned": True,
            "shoot": True,
            "aimkey": "e",
            "trigkey": "e",
            "trigdelay": "50",
            "side": 3.0,
            "smoothness": 5.0,
            "fov": 3,
            "rpc": True,
        }
        with open(config_path, "w") as configfile:
            json.dump(config, configfile)
    else:
        with open(localv_path, "r") as file:
            data = json.load(file)
            local_version = data["version"]

    with open("localv.json", "r") as file:
        data2 = json.load(file)
        first_launch = data["first_launch"]

    if first_launch is not True:
        with open("localv.json", "r") as file:
            data2 = json.load(file)
            pip = data["pip"]

        if pip is not True:
            print("Installing required modules...")
            os.system("pip install -r req.txt")
            os.system("pip3 install -r req.txt")
            with open("localv.json", "w") as file:
                data2["pip"] = True
                json.dump(data2, file)
            os.remove(file_paths[3])

    if remote_version != local_version:

        print("Deleting old files...")
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error occurred while removing {file_path}: {e}")

        print("Downloading SLAYY AIM...")
        # Download the zip file
        url = "https://github.com/pro1234qwerr/SLAYY-AIM-V2/archive/refs/heads/main.zip"
        response = urllib.request.urlopen(url)
        zip_content = response.read()

        # Save the zip file
        with open("ai-aimbot-main.zip", "wb") as file:
            file.write(zip_content)

        print("Unzipping...")
        # Unzip the file
        with zipfile.ZipFile("ai-aimbot-main.zip", "r") as zip_ref:
            zip_ref.extractall("ai-aimbot-main")
        os.remove("ai-aimbot-main.zip")

        print("Moving files...")
        # Move files from ai-aimbot/ to current directory
        for root, dirs, files in os.walk("ai-aimbot-main"):
            for file in files:
                shutil.move(os.path.join(root, file), os.path.join(".", file))

        # Remove ai-aimbot-testing/ directory
        shutil.rmtree("ai-aimbot-main")

        os.remove(file_paths[4])
        os.remove(file_paths[5])

        with open("localv.json", "w") as file:
            data["version"] = remote_version
            json.dump(data, file)

        with open(localv_path, "r") as file:
            data = json.load(file)
            python = data["python"]

        if python is not True:
            print("Downloading python...")
            # Download the python
            url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
            filename = "pythoninstaller.exe"
            urllib.request.urlretrieve(url, filename)

            print("Installing python...")
            subprocess.run([filename, "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"])

            with open("localv.json", "w") as file:
                data["python"] = True
                json.dump(data, file)

            os.remove(filename)

        with open("localv.json", "w") as file:
            data["first_launch"] = False
            json.dump(data, file)
        print("Please relaunch SLAYY AIM...")
        time.sleep(5)
        exit()

    def clear_terminal():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    clear_terminal()
    option = True if input("Do you want to launch SLAYY AIM or change your config? (1/2): ").lower() == "1" else False
    if option:
        subprocess.run(["python", "library.py"])
    else:
        subprocess.run(["python", "config.py"])

except KeyboardInterrupt:
    exit()
