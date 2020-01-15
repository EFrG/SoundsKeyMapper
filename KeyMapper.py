# Eduardo Freyre Gómez
# This small script allows you to automatically map a series of Sounds to a key combination,
# using Autohotkey.
#

import os

audio_extension = []
directory = ""
audioFile_list = []

def loop_sound_dir(directory):
    # Loops through a directory, looking for files ending in
    #
    sounds = []
    for filename in os.listdir(directory):
        if filename.endswith(audio_extension):
            sounds.append(filename)
        else:
            continue
        return sounds

def interfaz():
    print("Welcome to Sound Key Mapper!")
    print("""This program allows you to automate the creation of Sound shortcuts.
    It uses Autohotkey, so you need to install it. Sadly it only is avaliable in Windows.
    Please, when requested, introduce complete routes to the files. You can obtain those by
    coping them from the adress bar in the top of the windows file explorer""")
    terminado = False
    while(not terminado):
        directory = input("In what folder are the sounds files you want to be scripted?")
        audioFile_list = loop_sound_dir(directory)
        num_elem = len(audioFile_list)
        print = ("There were "+str(num_elem)+" in the directory "+ directory)
        str_terminado = input("Write \"TRUE\" if the number of files matches what you expected")
        if str_terminado == "TRUE":
            terminado = True

    print(audioFile_list)

