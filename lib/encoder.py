
# https://github.com/nstansby/rpi-rotary-encoder-python

import RPi.GPIO as GPIO


class ENCODER: 
  __value = 0
  __state = '00'
  __direction = None

  def __init__(self, pins, callback=None):
    self.__leftPin = pins[0]
    self.__rightPin = pins[1]
    self.__callback = callback
    GPIO.setup(self.__leftPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(self.__rightPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.__leftPin, GPIO.BOTH, callback=self.__transitionOccurred)  
    GPIO.add_event_detect(self.__rightPin, GPIO.BOTH, callback=self.__transitionOccurred) 

  def __transitionOccurred(self, channel):
    p1 = GPIO.input(self.__leftPin)
    p2 = GPIO.input(self.__rightPin)
    newState = "{}{}".format(p1, p2)

    if self.__state == "00": # Resting position
      if newState == "01": # Turned right 1
        self.__direction = "R"
      elif newState == "10": # Turned left 1
        self.__direction = "L"

    elif self.__state == "01": # R1 or L3 position
      if newState == "11": # Turned right 1
        self.__direction = "R"
      elif newState == "00": # Turned left 1
        if self.__direction == "L":
          self.__value = self.__value - 1
          if self.__callback is not None:
            self.__callback(self.__value, self.__direction)

    elif self.__state == "10": # R3 or L1
      if newState == "11": # Turned left 1
        self.__direction = "L"
      elif newState == "00": # Turned right 1
        if self.__direction == "R":
          self.__value = self.__value + 1
          if self.__callback is not None:
            self.__callback(self.__value, self.__direction)

    else: # self.__state == "11"
      if newState == "01": # Turned left 1
        self.__direction = "L"
      elif newState == "10": # Turned right 1
        self.__direction = "R"
      elif newState == "00": # Skipped an intermediate 01 or 10 state, but if we know direction then a turn is complete
        if self.__direction == "L":
          self.__value = self.__value - 1
          if self.__callback is not None:
            self.__callback(self.__value, self.__direction)
          elif self.__direction == "R":
            self.__value = self.__value + 1
            if self.__callback is not None:
              self.__callback(self.__value, self.__direction)
              
    self.__state = newState
  
  def getValue(self):
    return self.__value