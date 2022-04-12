from pynput.keyboard import Key, Controller

class KNOB:
  __lastval = 0;
  __keyboard = Controller()
  __ran = 0

  def __init__(self, leds, buttons, keys):
    self.__LEDS = leds
    self.__buttons = buttons
    self.__keys = keys

  def __pressArrayKeys(self, index):
    # press all keys
    for ndx, key in enumerate(self.__keys[index], start=0):
      self.__keyboard.press(Key[self.__keys[index][ndx]])
    # release all keys
    for ndx, key in enumerate(self.__keys[index], start=0):
      self.__keyboard.release(Key[self.__keys[index][ndx]])

  def turned(self, val, dir):
    # no change in value
    if val == self.__lastval:
      # is the early return needed? does this ever run?
      self.__ran + 1
      print('unneeded code has run ' + self.__ran + ' times')
      return
    # led function mode
    # a lot of unnessacery code for things I might do later
    elif self.__buttons.function_state[0]:
      currentMode = self.__LEDS.getMode()
      # variable brightness adjustment
      if currentMode == 0:
        currentBrightness = self.__LEDS.getLedBrightness()
        if val < self.__lastval and currentBrightness >= 100:
          self.__LEDS.setLedBrightness(currentBrightness + 1)
        elif val > self.__lastval and currentBrightness <= 0:
          self.__LEDS.setLedBrightness(currentBrightness - 1)
      # on press (adjust speed)
      elif currentMode == 1:
        pass
      # breath (adjust speed)
      elif currentMode == 2:
        pass
      # knight rider (maybe adjust spped or brightness)
      elif currentMode == 3:
        pass
      # off (nothing to adjust)
      elif currentMode == 4:
        pass
    # knob turned no modifier
    else:
      if val < self.__lastval:
        # check if key[0] is an array of button names
        if isinstance(self.__keys[0], list):
          self.__pressArrayKeys(0)
        else:
          self.__keyboard.press(Key[self.__keys[0]])
          self.__keyboard.release(Key[self.__keys[0]])
      elif val > self.__lastval:
        if isinstance(self.__keys[1], list):
          self.__pressArrayKeys(1)
        else:
          self.__keyboard.press(Key[self.__keys[1]])
          self.__keyboard.release(Key[self.__keys[1]])
    self.__lastval = val;
    print(dir)