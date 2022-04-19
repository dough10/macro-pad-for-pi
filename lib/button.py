from array import array
import RPi.GPIO as GPIO
from pynput.keyboard import Key, Controller
from time import time


def millis():
    return round(time() * 1000)

class Button:
  __debounceTime = 50
  __lastPressed = 0
  __pressed = False
  __keyboard = Controller()

  def __init__(self, pin, leds, index, function_state, key):
    self.__pin = pin
    self.__LEDS = leds
    self.__index = index
    self.__key = key
    self.__function_state = function_state
    GPIO.setup(self.__pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  def __pressArrayKeys(self, state):
    # press all keys
    if state: 
      for index, key in enumerate(self.__key, start=0):
        self.__keyboard.press(Key[self.__key[index]])
    # release all keys
    else:
      for index, key in enumerate(self.__key, start=0):
        self.__keyboard.release(Key[self.__key[index]])

  def __press(self, state):
    # limit key spam
    now = millis();
    if now - self.__lastPressed < self.__debounceTime:
      return
    self.__lastPressed = now

    # only run if state has changed
    if state == self.__pressed:
      return
    self.__pressed = state

    # light up the button pressed when in onPress LED mode
    if state and self.__LEDS.getMode() == 1:
      try:
        self.__LEDS.setOneLedBrightness(self.__index, 0)
      except IndexError:
        pass

    # check for led to determine if button or encoder was pressed
    try:  
      self.__LEDS.LEDS[self.__index] ## checking if there is a led tied to the button index (ie. is it the encoder button)
      self.__LEDS.keyPressed = state  # only set state of led.keyPressed if the key pressed is not the encoder
      # set led mode to index of key pressed if encoder button (function button) is held depressed
      if self.__function_state[0]:
        self.__LEDS.setMode(self.__index)
        return

      ## actual key press commands here
      if isinstance(self.__key, list):
        self.__pressArrayKeys(state)
      else:
        self.__keyboard.press(Key[self.__key]) if state else self.__keyboard.release(Key[self.__key])
  
    # encoder was pressed (function state matchs button state)
    except IndexError:
      self.__function_state[0] = state

  def isPressed(self):
    return self.__pressed

  # because I wired something backwards in my pcb it has to have reversed logic?
  def update(self):
    self.__press(not GPIO.input(self.__pin))