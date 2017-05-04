#import RPi.GPIO as GPIO
import bot
import datetime
import time

#devices['device1','device2','device3','device4']
action=['switch','turn','press']

def extractState(sentence):
    print "called"
    for i in range(len(sentence)):
        if sentence[i].strip() in action:
        #word = sentence[i].strip()
            if sentence[i+1].strip()=="on" or sentence[i].strip()=="On" or sentence[i].strip()=="ON":
                return "on"
            elif sentence[i+1].strip()=="off" or sentence[i].strip()=="Off" or sentence[i].strip()=="OFF":
                return "off"


def extractDevice(sentence):
    for word in sentence:
        word=word.strip()
        if word=='fan':
            return "17"
        elif word=="light":
            return "27"
        elif word=="tv":
            return "22"
        elif word=="motor":
            return "10"

def extractDuration(sentence):
    #t_minutes=0
    #t_hours=0
    t_sec=5000
    for i in range(len(sentence)):
        #word = sentence[i].strip()
        if sentence[i].strip()=="for":
            if sentence[i+2].strip()=="minutes" or sentence[i+2].strip()=="minute":
                if sentence[i+1].strip()=="half":
                    t_sec=30
                else:
                    t_sec=int(sentence[i+1])*60
            elif sentence[i+2].strip()=="hours" or sentence[i+2].strip()=="hour":
                if sentence[i+1].strip()=="half":
                    t_sec=30*60
                else:
                    t_sec=int(sentence[i+1])*60*60
    return t_sec

def Time(sentence):
    requested_time = datetime.datetime.now().time()
    for i in range(len(sentence)):
        if sentence[i].strip()=="at":
            requested_time = bot.extractTime(sentence)
    return requested_time


def led_on(pinx,durationx,timex):
    pin=pinx
    #GPIO.setup(pin, GPIO.OUT)

    # while True:
    #     time_now=datetime.datetime.now().strftime("%H:%M")
    #     if time_now==timex:
    #         #GPIO.output(pin, True)
    #         time.sleep(durationx)
    #         #GPIO.output(pin, False)
    #     time.sleep(0.030)


def led_off(pinx,durationx,timex):
    pin=pinx
    #GPIO.setup(pin, GPIO.OUT)

    # while True:
    #     time_now=datetime.datetime.now().strftime("%H:%M")
    #     if time_now==timex:
    #         #GPIO.output(pin, False)
    #         time.sleep(durationx)
    #         #GPIO.output(pin, True)
    #     #time.sleep(0.030)



def executeDevices(text):
     st=text.replace(":"," ").split()
     state=extractState(st)
     pin=extractDevice(st)
     duration=extractDuration(st)
     time_for=Time(st)
     print state
     print pin
     print duration
     print time_for
    #  if state=="on":
    #      led_on(pin,duration,time_for)
    #  elif state=="off":
    #     led_off(pin,duration,time_for)

if __name__ == "__main__":
    print "ok"
    executeDevices("turn on device4 at 6 in morning")
    executeDevices("turn on device4 at 7 pm")
    executeDevices("turn off device2 for 3 minutes")
