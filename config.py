import customtkinter
import json
import os

from keyauth import api
import sys
import time
import platform
import os
import hashlib
import colorama
from time import sleep
from colorama import Fore

colorama.init()

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo -n -e "\033]0;Python Example\007"''')  # change title

print(Fore.LIGHTBLACK_EX + "Initializing")
time.sleep(0.9)
print(Fore.LIGHTBLACK_EX + "connecting")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


keyauthapp = api(
    name = "SLAYY",
    ownerid = "91id0HD1i4",
    secret = "c391c003a2d235ece87fb4fcd14e3f39c67c5b8b80124dcd40d8b3bdfe5beeb5",
    version = "1.0",
    hash_to_check = getchecksum()
)
def answer():
    try:
        print(Fore.LIGHTMAGENTA_EX + """
███████╗██╗      █████╗ ██╗   ██╗██╗   ██╗     █████╗ ██╗███╗   ███╗
██╔════╝██║     ██╔══██╗╚██╗ ██╔╝╚██╗ ██╔╝    ██╔══██╗██║████╗ ████║
███████╗██║     ███████║ ╚████╔╝  ╚████╔╝     ███████║██║██╔████╔██║
╚════██║██║     ██╔══██║  ╚██╔╝    ╚██╔╝      ██╔══██║██║██║╚██╔╝██║
███████║███████╗██║  ██║   ██║      ██║       ██║  ██║██║██║ ╚═╝ ██║
╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝             
""")

        time.sleep(2)

        print(Fore.LIGHTMAGENTA_EX + "[Slayy Aim] " + Fore.RESET + "Welcome to Slayy Aim")
        time.sleep(0.5)

        key = input("Enter your license key password: ")
        keyauthapp.license(key)
            
    except KeyboardInterrupt:
        os._exit(1)


answer()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("SLAYY AIM")
app.iconbitmap("Icon.ico")
app.attributes("-topmost", True)
padding = 10

try:
    config_file = "config.json"

    with open("localv.json", "r") as file:
        data8 = json.load(file)
        language = data8["language"]

    # Read the lang.json file
    with open("lang.json", "r", encoding='utf-8') as file:
        data5 = json.load(file)
        # Modify the English field in the answer field
        useranswer = data5["language"].get(language, {}).get("answers", {}).get("1", "")

    def questions(list):
        with open("lang.json", "r", encoding='utf-8') as file:
            question = json.load(file)
        text = question["language"][language]["text"]
        text = text[list]
        return text

    # def toggle_window():
    #     if app.state() == "withdrawn":
    #         app.deiconify()
    #     else:
    #         app.state("withdrawn")

    # guikeyentry = customtkinter.CTkEntry(app, placeholder_text=questions(0), width=240)
    # guikeyentry.pack(pady=padding, padx=padding, anchor="w")

    # def guikeyfunc():
    #     key = guikeyentry.get()
    #     data = {"gui_key": key}
    #     with open("config.json", "r+") as file:
    #         data = json.load(file)
    #         data["gui_key"] = key
    #         file.seek(0)
    #         json.dump(data, file)
    #         file.truncate()
    #     print("Set gui key")
    #     guikeyentry.delete(0, 'end')  # Clear the guikey entry

    # guikeybutton = customtkinter.CTkButton(app, text=questions(1), command=guikeyfunc)
    # guikeybutton.pack(pady=padding, padx=padding, anchor="w")

    # def get_gui_key():
    #     try:
    #         with open("config.json", "r") as file:
    #             data = json.load(file)
    #             return data.get("gui_key", "")
    #         # If key is not found, do something
    #     except:
    #         with open("config.json", "w") as file:
    #             data = {"gui_key": "o"}
    #             json.dump(data, file)
    #         print("Set gui key")
    #         return "o"

    # keyboard.on_press_key(get_gui_key(), lambda _: toggle_window())

    def rpcfunc():
        option = rpcswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["rpc"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want aimbot or a triggerbot? (1/2):"
    rpcvar = customtkinter.StringVar(value="")
    rpcswitch = customtkinter.CTkSwitch(app, text=questions(13), command=rpcfunc, variable=rpcvar, onvalue=True, offvalue=False)
    rpcswitch.pack(pady=padding, padx=padding, anchor="w")

    def trigbot():
        option = aimbotswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["aimbot"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want aimbot or a triggerbot? (1/2):"
    aimbotvar = customtkinter.StringVar(value="")
    aimbotswitch = customtkinter.CTkSwitch(app, text=questions(2), command=trigbot, variable=aimbotvar, onvalue=True, offvalue=False)
    aimbotswitch.pack(pady=padding, padx=padding, anchor="w")

    def detection():
        option = detectionswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["detection"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want it to shoot? (y/n):"
    detectionvar = customtkinter.StringVar(value="on")
    detectionswitch = customtkinter.CTkSwitch(app, text=questions(11), variable=detectionvar,command=detection, onvalue=True, offvalue=False)
    detectionswitch.pack(pady=padding, padx=padding, anchor="w")

    def pinned():
        option = pinnedswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["pinned"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want the detection window to be pinned on top? (y/n):"
    pinnedvar = customtkinter.StringVar(value="on")
    pinnedswitch = customtkinter.CTkSwitch(app, text=questions(3), variable=pinnedvar, command=pinned, onvalue=True, offvalue=False)
    pinnedswitch.pack(pady=padding, padx=padding, anchor="w")


    def shoot():
        option = shootswitch.get()
        with open("config.json", "r+") as file:
            data = json.load(file)
            data["shoot"] = option
            file.seek(0)
            json.dump(data, file)
            file.truncate()

    # Create a switch for "Do you want it to shoot? (y/n):"
    shootvar = customtkinter.StringVar(value="on")
    shootswitch = customtkinter.CTkSwitch(app, text=questions(4), variable=shootvar,command=shoot, onvalue=True, offvalue=False)
    shootswitch.pack(pady=padding, padx=padding, anchor="w")

    # Create a switch for "Press the key you want to use to aim:"
    aimkeyentry = customtkinter.CTkEntry(app, placeholder_text=questions(5), width=190)
    aimkeyentry.pack(pady=padding, padx=padding, anchor="w")

    def aimkeyfunc():
        key2 = aimkeyentry.get()
        data2 = {"gui_key": key2}
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["aimkey"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()
        aimkeyentry.delete(0, 'end')  # Clear the guikey entry

    aimkeybutton = customtkinter.CTkButton(app, text=questions(10), command=aimkeyfunc)
    aimkeybutton.pack(pady=padding, padx=padding, anchor="w")



    # Create a switch for "Smoothness? (1-10):"
    def slider_event(value):
        key2 = value
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["side"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    sidelabel = customtkinter.CTkLabel(app, text=questions(6), fg_color="transparent")
    sidelabel.pack(pady=padding, padx=padding, anchor="w")
    sideslider = customtkinter.CTkSlider(app, from_=1, to=3,number_of_steps=2, command=slider_event)
    sideslider.pack(pady=padding, padx=padding, anchor="w")

    # Create a switch for "Smoothness? (1-10):"
    def slider_event(value):
        key2 = value
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["smoothness"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    sliderlabel = customtkinter.CTkLabel(app, text=questions(7), fg_color="transparent")
    sliderlabel.pack(pady=padding, padx=padding, anchor="w")
    smoothslider = customtkinter.CTkSlider(app, from_=1, to=10,number_of_steps=9, command=slider_event)
    smoothslider.pack(pady=padding, padx=padding, anchor="w")

    # Create a switch for "Smoothness? (1-10):"
    def fov_event(value):
        key2 = value
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["fov"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()

    fovlabel = customtkinter.CTkLabel(app, text=questions(12), fg_color="transparent")
    fovlabel.pack(pady=padding, padx=padding, anchor="w")
    fovslider = customtkinter.CTkSlider(app, from_=1, to=10,number_of_steps=9, command=fov_event)
    fovslider.pack(pady=padding, padx=padding, anchor="w")


    # Create a switch for "Enter the key you want to use to activate the triggerbot:"
    trigkeyentry = customtkinter.CTkEntry(app, placeholder_text=questions(8), width=290)
    trigkeyentry.pack(pady=padding, padx=padding, anchor="w")

    def trigkeyfunc():
        key2 = trigkeyentry.get()
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["trigkey"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()
        trigkeyentry.delete(0, 'end')  # Clear the guikey entry

    trigkeybutton = customtkinter.CTkButton(app, text=questions(10), command=trigkeyfunc)
    trigkeybutton.pack(pady=padding, padx=padding, anchor="w")

    # Create a switch for "Enter the key you want to use to activate the triggerbot:"
    trigdelayentry = customtkinter.CTkEntry(app, placeholder_text=questions(9), width=300)
    trigdelayentry.pack(pady=padding, padx=padding, anchor="w")


    def trigdelayfunc():
        key2 = trigdelayentry.get()
        with open("config.json", "r+") as file:
            data2 = json.load(file)
            data2["trigdelay"] = key2
            file.seek(0)
            json.dump(data2, file)
            file.truncate()
        trigdelayentry.delete(0, 'end')  # Clear the guikey entry

    trigdelaybutton = customtkinter.CTkButton(app, text=questions(10), command=trigdelayfunc)
    trigdelaybutton.pack(pady=padding, padx=padding, anchor="w")


    app.mainloop()


except KeyboardInterrupt:
    exit()
