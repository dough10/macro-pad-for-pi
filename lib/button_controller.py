from lib.button import Button

# places button objects in an array 
class BUTTON_CONTROLLER:
  __buttons = []
  function_state = [
    False
  ]
  def __init__(self, pins, leds, keys):
    # enumerate to acquire a index value (keeps the keys and leds linked by this index value)
    for index, pin in enumerate(pins, start=0):
      # the encoder button gets blank string for keybind
      if index != 5:
        self.__buttons.append(Button(pin, leds, index, self.function_state, keys[index]))
      else:
        self.__buttons.append(Button(pin, leds, index, self.function_state, ''))

  # checks all of the buttons in the array to see which have been pressed
  def checkIfPressed(self):
    for button in self.__buttons:
      button.update()