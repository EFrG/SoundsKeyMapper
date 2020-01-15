# Eduardo Freyre Gómez
# This small script allows you to automatically map a series of Sounds to a key combination,
# using Autohotkey.
#

import os

audio_extension = []
directory = ""
sounds = []

def loop_sound_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith(audio_extension):
            sounds.append(filename)
        else:
            continue
