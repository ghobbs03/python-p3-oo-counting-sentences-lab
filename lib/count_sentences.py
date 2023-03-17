#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
      self._value = value

  def get_value(self):
    return self._value

  def set_value(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value, )
  
  def is_sentence(self):
    if (self._value[-1] == '.'):
      return True
    else:
      return False

  def is_question(self):
    if (self._value[-1] == '?'):
      return True
    else:
      return False
      
    
  def is_exclamation(self):
    if (self._value[-1] == "!"):
      return True
    else:
      return False

  def count_sentences(self):
    str_val = self._value
    print("value: ", str_val)
    count = 0
    if (self._value == ""):
      return count

    for i in range(len(str_val)-2):
      if (str_val[i:i+2] == '. ' or str_val[i:i+2] == '? ' or str_val[i:i+2] == '! ' ):
        count += 1
      
    if (str_val[-1] == '.' or str_val[-1] == '?' or str_val[-1] == '!'):
      count += 1
         
    return count

   
  


