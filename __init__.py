from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
import serial
import time
import subprocess
import decimal

class introSkill(MycroftSkill):

    def __init__(self):
        super().__init__()
        self.learning = True

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    @intent_handler('intro.intent')
    def handle_not_are_you_intent(self, message):
        serA = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        serA.flush()
        serA.write(b"intro")
        serB = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        serB.flush()
        serB.write(b"intro")        
        serC = serial.Serial('/dev/ttyACM2', 9600, timeout=1)
        serC.flush()
        serC.write(b"intro")
        serD = serial.Serial('/dev/ttyACM3', 9600, timeout=1)
        serD.flush()
        serD.write(b"intro")
        time.sleep(1.5)
        self.speak_dialog("hello kurt, these are the people who made me.  ")
        self.speak_dialog("We have billy who oversaw project management budgeting and CAD")
        self.speak_dialog("Lindsay who also worked on CAD as well as my electrical system")
        self.speak_dialog("Tyler and rye lee who designed several of my armor pieces.")
        self.speak_dialog("Sintia helped create the voice assistant")
        self.speak_dialog(" Brandon wrote the code that allowed me to move, and ash ton helped connect the voice assistant and motors together")
      

    def stop(self):
        pass

def create_skill():
    return introSkill()
