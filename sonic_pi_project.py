from sense_hat import SenseHat
from psonic import *
from time import sleep
import random

sense = SenseHat()
sense.clear()

def pitch_change(pitch_value):
    if pitch_value >= 0 and pitch_value < 180:
        sense.clear(0,0,255)
        sample(GUIT_HARMONICS)
        #sample(DRUM_CYMBAL_OPEN,attack=0.01,sustain=0.3,release=0.1)
        sleep(0.5)
        sample(GUIT_E_FIFTHS)
    elif pitch_value >= 180 and pitch_value < 360:
        sense.clear(0,255,0) 
        sample(PERC_BELL)
        sample(BASS_THICK_C)
        sample(TABLA_TE2)
        sleep(0.5)
               
def roll_change(roll_value):
    if roll_value >= 0 and roll_value < 180:
        sense.clear(255,0,0)
        sample(SN_ZOME)
        sample(BASS_THICK_C,attack=0.01,sustain=0.3,release=0.1)
        sleep(0.5)
        sense.clear(0,255,0)     
    elif roll_value >= 180 and roll_value <= 360:
        sense.clear(255,255,255)
        sample(DRUM_TOM_MID_HARD)
        sample(VINYL_SCRATCH)
        sleep(0.5)


while True:
    orientation = sense.get_orientation() 
    
    pitch = orientation["pitch"]
    pitch_value = int(abs(round(pitch, 0)))
    print("Pitch Value :", pitch_value)
    pitch_change(pitch_value)
    
    roll = orientation["roll"]
    roll_value= int(abs(round(roll, 0)))
    print("Roll Value :", roll_value)
    
    yaw = orientation["yaw"]
    yaw_value = int(abs(round(yaw, 0)))
    print("Yaw Value :", yaw_value)



    
