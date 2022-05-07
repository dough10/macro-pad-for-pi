from pynput.keyboard import Key, Controller

keyboard = Controller()

class KNOB:
  __lastval = 0
  __brightnessIncriment = 5
  __KRIncriment = 0.001
  __pressIncriment = 0.001

  def __init__(self, leds, buttons, keys):
    self.__LEDS = leds
    self.__buttons = buttons
    self.__keys = keys
    self.__functionModes = {
      0: self.__variableBrightness,
      1: self.__onPress,
      2: self.__breath,
      3: self.__knightRider,
      4: self.__off
    }

  def __variableBrightness(self, val):
    currentBrightness = self.__LEDS.getLedBrightness()
    if val < self.__lastval and currentBrightness >= 100:
      self.__LEDS.setLedBrightness(currentBrightness + self.__brightnessIncriment)
    elif val > self.__lastval and currentBrightness <= 0:
      self.__LEDS.setLedBrightness(currentBrightness - self.__brightnessIncriment)

  def __onPress(self, val):
    pass

  def __breath(self, val):
    pass

  def __knightRider(self, val):
    currentIncriment = self.__LEDS.getKRIncriment()
    if val < self.__lastval and currentIncriment <= 0.06:
      self.__LEDS.setKRIncriment(currentIncriment - self.__KRIncriment)
    elif val > self.__lastval and currentIncriment >= 0.00:
      self.__LEDS.setKRIncriment(currentIncriment + self.__KRIncriment)

  def __off(self, val):
    pass

  def __pressArrayKeys(self, index):
    # press all keys
    for ndx, key in enumerate(self.__keys[index], start=0):
      keyboard.press(Key[self.__keys[index][ndx]])
    # release all keys
    for ndx, key in enumerate(self.__keys[index], start=0):
      keyboard.release(Key[self.__keys[index][ndx]])

  def __keyPress(self, index):
    keyboard.press(Key[self.__keys[index]])
    keyboard.release(Key[self.__keys[index]])

  def turned(self, val, dir):
    # no change in value
    if val == self.__lastval:
      return
    # led function mode
    elif self.__buttons.function_state[0]:
      self.__functionModes[self.__LEDS.getMode()](val)
    # knob turned no modifier
    else:
      if val < self.__lastval:
        # check if key[0] is an array of button names
        if isinstance(self.__keys[0], list):
          self.__pressArrayKeys(0)
        else:
          self.__keyPress(0)
      elif val > self.__lastval:
        if isinstance(self.__keys[1], list):
          self.__pressArrayKeys(1)
        else:
          self.__keyPress(1)
    self.__lastval = val;
    print(dir)