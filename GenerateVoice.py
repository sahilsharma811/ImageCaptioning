import os
from subprocess import call
from subprocess import call
import os

def speak(message):
	os.system('espeak "{}"'.format(message))
	os.system('espeak "{}" -w caption.wav'. format(message))

if __name__ == '__main__':
	speak('This is a Sample Voice.')	
