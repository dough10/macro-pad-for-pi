import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller
from time import time

keyboard = Controller()

def millis():
    return round(time() * 1000)

class Button:
  __debounceTime = 50
  __lastPressed = 0
  __pressed = False

  def __init__(self, pin, leds, index, __function_state, key):
    self.__pin = pin
    self.LEDS = leds
    self.__index = index
    self.__key = key
    self.__function_state = __function_state
    GPIO.setup(self.__pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def __press(self, state):
    # limit key spam
    now = millis();
    if now - self.__lastPressed < self.__debounceTime:
      return
    self.__lastPressed = now

    # only run is state has changed
    if state == self.__pressed:
      return
    self.__pressed = state

    # light up the button pressed when in onPress mode
    if state and self.LEDS.getMode() == 1:
      try:
        self.LEDS.setOneLedBrightness(self.__index, 0)
      except IndexError:
        pass

    # check for led to determine if button or encoder was pressed
    try:  
      self.LEDS.LEDS[self.__index] ## checking if there is a led tied to the button index (ie. is it the encoder button)
      self.LEDS.keyPressed = state  # only set state of led.keyPressed if the key pressed is not the encoder
      # set led mode to index of key pressed if encoder is held depressed
      if self.__function_state[0]:
        self.LEDS.setMode(self.__index)
        return

      ## actual key press command here
      keyboard.press(Key[self.__key]) if state else keyboard.release(Key[self.__key])
      # print("Button: ",  self.__pin, ", LED: ", self.LEDS.LEDS[self.__index], ", Key: " + self.__key + ", Pressed") if state else print("Button: ",  self.__pin, ", LED: ", self.LEDS.LEDS[self.__index], ", Key: " + self.__key +  ", Released")
      # print('')
      ##
    # encoder was pressed
    except IndexError:
      self.__function_state[0] = state
      return

  def isPressed(self):
    return self.__pressed

  def update(self):
    self.__press(not GPIO.input( self.__pin))