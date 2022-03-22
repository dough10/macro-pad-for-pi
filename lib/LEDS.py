import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class LED_CONTROLLER:
  def __init__(self, pins):
    self.LEDS = []
    self.brightnesses = []
    self.mode = 3
    self.keyPressed = False
    self.brightness = 0
    self.__currentLED = 1
    self.__krIncriment = 0.05
    self.__krBrightness = 10 - self.__krIncriment
    self.__changeBy = -1
    self.__clickIncriment = 0.001
    self.__breathIncriment = 0.003
    self.__breathBrightness = 10
    self._selectMode = {
      0: self.__variableBrightness,
      1: self.__onPressMode,
      2: self.__breath,
      3: self.__KnightRider,
      4: self.__off
    }
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT)
      pwm = GPIO.PWM(pin, 500) 
      pwm.start(100)
      self.LEDS.append(pwm)
      self.brightnesses.append(100)

  def setMode(self, mode):
    self.mode = mode

  def shineOn(self):
    self._selectMode[self.mode]()

  def cleanup(self):
    for led in self.LEDS:
      led.stop()
    GPIO.cleanup()

  def __off(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(100)

  def __variableBrightness(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(self.brightness)

  def __breath(self):
    for led in self.LEDS:
      led.ChangeDutyCycle(self.__breathBrightness)
    self.__breathBrightness = self.__breathBrightness + self.__breathIncriment
    if self.__breathBrightness <= 0.005 or self.__breathBrightness >=  99.995:
      self.__breathIncriment = -self.__breathIncriment

  def __onPressMode(self):
    for num, brightness in enumerate(self.brightnesses, start=0):
      self.LEDS[num].ChangeDutyCycle(self.brightnesses[num])
      if brightness < 100.0 and not self.keyPressed:
        self.brightnesses[num] = self.brightnesses[num] + self.__clickIncriment

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