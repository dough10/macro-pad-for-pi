# 5 gpio pins using BCM numbering method
led_pins = [
  13,
  6,
  19,
  21,
  26
] 


# 6 gpio pins using BCM gpio numbering
button_pins = [
  20,
  16,
  12,
  25,
  24,
  23
] 

encoder_pins = [
  27,
  22
]


# here are all the attrebutes of pynput.keyboard.Key 
__commands = [
  'alt', 'backspace', 'cmd', 'ctrl', 'delete', 'down', 'end', 'enter',
  'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18',
  'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'home',
  'insert','left', 'menu', 'pause', 'right', 'shift', 'space', 'tab', 'up'
]


# 5 entrys
# strings or arrays
keys = [
  'up',
  'down',
  'left',
  'right',
  ['alt','f4']
] 

# 2 key names to bind to encoder left encKeys[0] right encKeys[1]
encKeys = [
  'left',
  'right'
]