from mutagen.mp3 import MP3
from pygame import mixer
from time import sleep as wait
mixer.init()
savefile = open("save.txt", "r")
save = savefile.readlines()
savefile.close()
savefile = open("save.txt", "w")
def length(file):
    return MP3(file).info.length
def saveEnd(ending):
    if f"{ending}\n" in save:
        pass
    else:
        save.append(f"{ending}\n")
def play(sound):
    mixer.music.load(sound)
    mixer.music.play()
play("assets/sounds/welcome.mp3")
ans = input()
if ans.lower() == "chase":
    play("assets/sounds/chase.mp3")
    ans = input()
    if ans.lower() == "scratch":
        play("assets/sounds/scratch.mp3")
        ans = input()
        if ans.lower() == "key":
            play("assets/sounds/key.mp3")
            ans = input()
            if ans.lower() == "storage":
                play("assets/sounds/storage.mp3")
                ans = input()
                if ans.lower() == "controller":
                    play("assets/sounds/controller.mp3")
                    wait(length("assets/sounds/controller.mp3"))
                    saveEnd("OMGGAMER")
                elif ans.lower() == "vent":
                    play("assets/sounds/vent.mp3")
                    saveEnd("You Need To Be Sus, Muffin")
                    wait(length("assets/sounds/controller.mp3"))
            elif ans.lower() == "stairs":
                play("assets/sounds/stairs.mp3")
                wait(length("assets/sounds/stairs.mp3"))
                saveEnd("Off to the Dogs!")
        elif ans.lower() == "tackle":
            play("assets/sounds/tackle.mp3")
            ans = input()
            if ans.lower() == "hide":
                play("assets/sounds/hide.mp3")
                wait(length("assets/sounds/hide.mp3"))
                saveEnd("Tuna Can Cravings")
            elif ans.lower() == "escape":
                play("assets/sounds/escape.mp3")
                wait(length("assets/sounds/escape.mp3"))
                saveEnd("Caught Red Handed")
    elif ans.lower() == "elevator":
        play("assets/sounds/elevator.mp3")
        ans = input()
        if ans.lower() == "top":
            play("assets/sounds/top.mp3")
            ans = input()
            if ans.lower() == "bonk":
                play("assets/sounds/bonk.mp3")
                wait(length("assets/sounds/bonk.mp3"))
                saveEnd("Bonk N' Bash")
            elif ans.lower() == "window":
                play("assets/sounds/window.mp3")
                wait(length("assets/sounds/window.mp3"))
                saveEnd("Window Walker")
        elif ans.lower() == "basement":
            play("assets/sounds/basement.mp3")
            ans = input()
            if ans.lower() == "tank":
                play("assets/sounds/tank.mp3")
                ans = input()
                if ans.lower() == "hijack":
                    play("assets/sounds/hijack.mp3")
                    wait(length("assets/sounds/hijack.mp3"))
                    saveEnd("Hijacking Hero")
                elif ans.lower() == "drive":
                    play("assets/sounds/drive.mp3")
                    wait(length("assets/sounds/drive.mp3"))
                    saveEnd("Approved Driver")
            elif ans.lower() == "vent":
                play("assets/sounds/vent.mp3")
                wait(length("vent.mp3"))
                saveEnd("You Need To Be Sus, Muffin")
elif ans.lower() == "wait":
    play("assets/sounds/wait.mp3")
    wait(length("wait.mp3"))
    saveEnd("Good Person")
for i in save:
    savefile.write(i)
play("assets/sounds/end.mp3")
