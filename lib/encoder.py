
class ENCODER: 
  def __init__(self, pins, leds, function_state):
    self.__knob = '''RotaryIRQ(
      pin_num_clk=pins[0],
      pin_num_dt=pins[1],
      min_val=0,
      max_val=65025,
      reverse=False,
      range_mode=RotaryIRQ.RANGE_UNBOUNDED,
      pull_up=True)'''
    # self.__value = self.__knob.value()
    self.__function_state = function_state
    self.LEDS = leds

  def checkIfTurned(self):
    # newVal = self.__knob.value()
    # if newVal > self.__value:
    #   if self.__function_state[0]:
    #     if self.LEDS.getLedBrightness() < 0.05 and self.LEDS.getMode() == 0:
    #       self.LEDS.setBrightness(self.LEDS.getBrightness() - 5)
    #       # print(self.LEDS.brightness)
    #   else :
    #     print('up')
    # elif newVal < self.__value:
    #   if self.__function_state[0]:
    #     if self.LEDS.getLedBrightness() < 99.95 and self.LEDS.getMode() == 0:
    #       self.LEDS.setBrightness(self.LEDS.getBrightness() + 5)
    #       # print(self.LEDS.brightness)
    #   else :
    #     print('down')
    # self.__value = newVal
    print('')