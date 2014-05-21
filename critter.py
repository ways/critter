import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
eyes = [7, 11]
verbose = True

def set(property, value):
  try:
    f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
    f.write(value)
    f.close()	
  except:
    print("Error writing to: " + property + " value: " + value)


def blink (duration = 0.2):
  pass


def look (state = True):
  for eye in eyes:
    #GPIO.setup(eye, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(eye, GPIO.OUT)
    GPIO.output(eye, state)
    if verbose:
      #print "Setting eye", eye, " to ", GPIO.gpio_function(eye)
      print "Setting eye", eye, " to ", state


def shiver (repeat = 1):
  delay_period = 0.01
  if verbose:
    print "Shivering for", repeat, "times."

  for num in range(1,repeat):
    for angle in range(0, 10):
      setServo(angle)
      time.sleep(delay_period)

    for angle in range(0, 10):
      setServo(180 - angle)
      time.sleep(delay_period)


def setServo(angle):
  set("servo", str(angle))
  set("delayed", "0")
  set("mode", "servo")
  set("servo_max", "180")
  set("active", "1")


# main
while True:
  look (True)
  time.sleep (2)
  look (False)
  time.sleep (.1)
  look (True)
  time.sleep (1)

  shiver (2)
  time.sleep (3)
