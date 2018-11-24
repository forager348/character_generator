### Character generation class
### 
### Author: forager348
### Last updated: 11/23/2018
import random


def generate_sequence(chars):
  pseudo_sequence = ''
  if chars != None and isinstance(chars, int):
    while chars > 0:
      pseudo_bit = random.randint(0, 6)
      if pseudo_bit == (0 or 1):
        pseudo_number = chr(random.randint(48, 57))
        pseudo_sequence += pseudo_number
      elif pseudo_bit == (2 or 3):
        pseudo_big_alpha = chr(random.randint(65, 90))
        pseudo_sequence += pseudo_big_alpha
      elif pseudo_bit == (4 or 5):
        pseudo_small_alpha = chr(random.randint(97, 122))
        pseudo_sequence += pseudo_small_alpha
      elif pseudo_bit == 6:
        pseudo_symbol = chr(random.randint(33, 47))
        pseudo_sequence += pseudo_symbol
      else:
        pseudo_small_alpha = chr(random.randint(97, 122))
        pseudo_sequence += pseudo_small_alpha
      chars -= 1
  print(pseudo_sequence)
