from lib.LEDS import LED_CONTROLLER
from lib.button_controller import BUTTON_CONTROLLER
import config

leds = LED_CONTROLLER(config.led_pins)
buttons = BUTTON_CONTROLLER(config.button_pins, leds, config.keys)

try:
  while True:
    leds.shineOn()
    buttons.checkIfPressed()

except KeyboardInterrupt:
  leds.cleanup()
  