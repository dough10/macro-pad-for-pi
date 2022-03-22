from lib.button import Button

# places button objects in an array 
class BUTTON_CONTROLLER:
  def __init__(self, pins, leds, keys):
    self.buttons = []
    self.function_state = [
      False
    ]
    # enumerate to acquire a index value 
    ## keeps the keys and leds linked by this index value
    for index, pin in enumerate(pins, start=0):
      self.buttons.append(Button(pin, leds, index, self.function_state, keys[index]))

  # checks all of the buttons in the array to see which have been pressed
  def checkIfPressed(self):
    for button in self.buttons:
      button.update()