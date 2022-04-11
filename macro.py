from lib.LEDS import LED_CONTROLLER
from lib.button_controller import BUTTON_CONTROLLER
from lib.knob import KNOB
from lib.encoder import ENCODER
import config

leds = LED_CONTROLLER(config.led_pins)
buttons = BUTTON_CONTROLLER(config.button_pins, leds, config.keys)

ENCODER(config.encoder_pins, KNOB(leds, buttons, config.encKeys).turned)

try:
  while True:
    leds.shineOn()
    buttons.checkIfPressed()

except KeyboardInterrupt:
  leds.cleanup()
