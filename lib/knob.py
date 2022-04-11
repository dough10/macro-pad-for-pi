from pynput.keyboard import Key, Controller

class KNOB:
  __lastval = 0;
  __keyboard = Controller()

  def __init__(self, leds, buttons, keys):
    self.__LEDS = leds
    self.__buttons = buttons
    self.__keys = keys

  def turned(self, val, dir):
    # no change in value
    if val == self.__lastval:
      return
    # led function mode
    elif self.__buttons.function_state[0]:
      # a lot of unnessacery code for things I might do later
      if self.__LEDS.getMode() == 0:
        if val < self.__lastval:
          if self.__LEDS.getLedBrightness() >= 100:
            self.__LEDS.setLedBrightness(self.__LEDS.getLedBrightness() + 1)
        elif val > self.__lastval:
          if self.__LEDS.getLedBrightness() <= 0:
            self.__LEDS.setLedBrightness(self.__LEDS.getLedBrightness() - 1)
      elif self.__LEDS.getMode() == 1:
        pass
      elif self.__LEDS.getMode() == 2:
        pass
      elif self.__LEDS.getMode() == 3:
        pass
      elif self.__LEDS.getMode() == 4:
        pass
    # knob turned no modifier
    else:
      if val < self.__lastval:
        self.__keyboard.press(Key[self.__keys[0]])
        self.__keyboard.release(Key[self.__keys[0]])
      elif val > self.__lastval:
        self.__keyboard.press(Key[self.__keys[1]])
        self.__keyboard.release(Key[self.__keys[1]])
    self.__lastval = val;
    print(dir)