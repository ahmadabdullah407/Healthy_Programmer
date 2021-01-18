#Healthy Programmer
# Water - water.mp3(3.5 litres)-input(drank) log generate
# Eyes - eyes.mp3 - Input(EyDone) (ever 30 minutes) log generate
# Physical Activity - pysical.mp3 (Every 45 minutes) Input (Exdone) log generate
# Rules: Pygame module to play audio
import time
from pygame import mixer
mixer.init()
inwater = int(time.time())
ineyes = inwater
inex = inwater
tt = inwater + 28800 # (total 8 hours (8*60*60=28800s)
rounds = 15 # 15 times in 8 hours 234 ml each time 3.5 litre in 8 hours
def waterfun():
    global inwater
    global rounds
    fwater = int(time.time())
    play1 = int((tt - inwater) / rounds)
    if fwater - inwater > play1:
        mixer.music.load('water.mp3') # add water drinking mp3 reminder file name here
        mixer.music.play(loops=-1)
        while True:
            drank = input('Write drank if you drank water\n')
            if drank == 'drank':
                mixer.music.stop()
                with open('water.txt', 'a') as f:
                    wtime = str(time.asctime(time.localtime(time.time())))
                    f.write(f'  Water drank at:    {wtime} \n')
                    rounds -= 1
                    if rounds == 0:
                        print("Congratulation you drank your targeted water\n")
                        break
                break
            else:
                print('Wrong input Try again')
                continue
        inwater = int(time.time())
    elif tt <= inwater:
        print('timeout')
        # break
def eyefun():
    global ineyes
    feyes = int(time.time())
    if feyes - ineyes > 1800: # Every 30 minutes (30*60 = 1800)
        mixer.music.load('eye.mp3') # add eye exercise mp3 reminder file here
        mixer.music.play(loops=-1)
        while True:
            eyeex = input('Write eydone if you did eye exercise\n')
            if eyeex == 'eydone':
                mixer.music.stop()
                with open('eyerec.txt', 'a') as f:
                    eytime = str(time.asctime(time.localtime(time.time())))
                    f.write(f' You did Eye Exercise at: {eytime}\n')
                break
            else:
                print('Wrong input Try again')
                continue
        ineyes = int(time.time())
def exfun():
    global inex
    fex = int(time.time())
    if fex - inex > 2700: #Every 45 minutes (45*60= 2700s)
        mixer.music.load('titanium.mp3') #add physical exercise mp3 reminder file name here
        mixer.music.play(loops=-1)
        while True:
            exex = input('Write exdone if you did physical exercise\n')
            if exex == 'exdone':
                mixer.music.stop()
                with open('exrec.txt', 'a') as f:
                    extime = str(time.asctime(time.localtime(time.time())))
                    f.write(f' You did physical exercise at: {extime}\n')
                break
            else:
                print('Wrong input Try again')
                continue
        inex = int(time.time())
while True:
    if rounds != 0:
        waterfun()
    eyefun()
    exfun()




