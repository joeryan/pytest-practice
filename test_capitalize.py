# test_capitalize.py
# simple test cases using pytest

import pytest

def capital_case(x):
  if not isinstance(x, str):
    raise TypeError('Please provide a string argument')
  return x.capitalize()

def test_captial_case():
  assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
  with pytest.raises(TypeError):
    capital_case(9)
