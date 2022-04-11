import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class LED_CONTROLLER:
  LEDS = []
  keyPressed = False
  __mode = 0
  __brightness = 0
  __brightnesses = []
  __currentLED = 1
  __changeBy = -1
  __krIncriment = 0.05
  __krBrightness = 9.95
  __clickIncriment = 0.001
  __breathIncriment = 0.003
  __breathBrightness = 10
  
  def __init__(self, pins):
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT)
      pwm = GPIO.PWM(pin, 500) 
      pwm.start(100)
      self.LEDS.append(pwm)
      self.__brightnesses.append(100)

    self.__ledMode = {
      0: self.__variableBrightness,
      1: self.__onPressMode,
      2: self.__breath,
      3: self.__KnightRider,
      4: self.__off
    }

  # sets LED mode
  def setMode(self, mode):
    self.__mode = mode

  # gets current LED mode
  def getMode(self):
    return self.__mode

  # method for turning a LED on when a button is pressed
  def setOneLedBrightness(self, index, brightnessVal):
    self.__brightnesses[index] = brightnessVal

  # method for settingled brightness for variable brightness mode
  def setLedBrightness(self, brightnessVal):
    self.__brightness = brightnessVal

  # get the current brightness lever for variable brightness
  def getLedBrightness(self):
    return self.__brightness

  # make LED do work
  def shineOn(self):
    self.__ledMode[self.__mode]()

  # cleanup GPIO 
  def cleanup(self):
    for led in self.LEDS:
      led.stop()
    GPIO.cleanup()

  # LED off mode
  def __off(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(100)

  # variable LED brightness mode
  def __variableBrightness(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(self.__brightness)

  # LED breathing mode
  def __breath(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(self.__breathBrightness)
    self.__breathBrightness = self.__breathBrightness + self.__breathIncriment
    if self.__breathBrightness <= 0.005 or self.__breathBrightness >=  99.995:
      self.__breathIncriment = -self.__breathIncriment

  # light up LED for the button pressed
  def __onPressMode(self):
    for num, brightness in enumerate(self.__brightnesses, start=0):
      self.LEDS[num].ChangeDutyCycle(self.__brightnesses[num])
      if brightness < 100.0 and not self.keyPressed:
        self.__brightnesses[num] = self.__brightnesses[num] + self.__clickIncriment

  # Knight rider!!!!!!
  def __KnightRider(self):
    self.LEDS[self.__currentLED].ChangeDutyCycle(self.__krBrightness)
    if (self.__krBrightness >= 99.95):
      self.__krIncriment = -self.__krIncriment
      if (self.__currentLED >= 4 or self.__currentLED <= 0):
        self.__changeBy = -self.__changeBy
      self.__currentLED = self.__currentLED + self.__changeBy
    elif (self.__krBrightness <= 0.05):
      self.__krIncriment = -self.__krIncriment
    self.__krBrightness = self.__krBrightness + self.__krIncriment
    