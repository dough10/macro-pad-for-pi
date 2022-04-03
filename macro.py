from lib.LEDS import LED_CONTROLLER
from lib.button_controller import BUTTON_CONTROLLER
from lib.encoder import ENCODER
import config

leds = LED_CONTROLLER(config.led_pins)
buttons = BUTTON_CONTROLLER(config.button_pins, leds, config.keys)
knob = ENCODER(config.encoder_pins, leds, buttons.function_state)

try:
  while True:
    leds.shineOn()
    buttons.checkIfPressed()
    # knob.checkIfTurned()

except KeyboardInterrupt:
  leds.cleanup()
