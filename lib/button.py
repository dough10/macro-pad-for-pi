import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def millis():
    return round(time.time() * 1000)

class Button:
  def __init__(self, pin, leds, index, __function_state, key):
    self.pin = pin
    GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    self.debounceTime = 50
    self.lastPressed = 0
    self.LEDS = leds
    self.index = index
    self.key = key
    self.__pressed = False
    self.__function_state = __function_state

  def __press(self, state):
    # limit key spam
    now = millis();
    if now - self.lastPressed < self.debounceTime:
      return
    self.lastPressed = now

    # only run is state has changed
    if state == self.__pressed:
      return
    self.__pressed = state
    self.LEDS.keyPressed = state

    # light up the button pressed when in onPress mode
    if state and self.LEDS.mode == 1:
      try:
        self.LEDS.brightnesses[self.index] = 0
      except IndexError:
        pass

    # check for led to determine if button or encoder was pressed
    try:  
      self.LEDS.LEDS[self.index] ## checking if there is a led tied to the button index (ie. is it the encoder button)
      # set led mode to index of key pressed if encoder is depressed
      if self.__function_state[0]:
        self.LEDS.mode = self.index
        return

      ## actual key press command here
      keyboard.press(Key[self.key]) if state else keyboard.release(Key[self.key])
      # print("Button: ", self.pin, ", LED: ", self.LEDS.LEDS[self.index], ", Key: " + self.key + ", Pressed") if state else print("Button: ", self.pin, ", LED: ", self.LEDS.LEDS[self.index], ", Key: " + self.key +  ", Released")
      # print('')
      ##
    # encoder was pressed
    except IndexError:
      self.__function_state[0] = state
      return

  def isPressed(self):
    return self.__pressed

  def update(self):
    self.__press(not GPIO.input(self.pin))