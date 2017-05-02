# import RPi.GPIO as gpio
#
# LED_PIN = 11
#
# gpio.setmode(gpio.BOARD)
# gpio.setup(LED_PIN, gpio.OUT)
import bot

def toggle_led(on):
    #gpio.output(LED_PIN, on)
    print "toggle is called : " + str(on)
    return 1

#recieving message
def send_message(text):
    print "messsage is : " + str(text)
    bot.executeParser(text)


#sending message
# def receive_message():
