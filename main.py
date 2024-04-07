from datetime import datetime
import time


# Part 1
def clock(n: int) -> None:
    """
    shows the time and updates it once every second, for n number of seconds.

    Parameter
    ---------
    n: int
        number of seconds to run the clock for

    Returns
    -------
    None
    """
    # Your code here
    while n > 0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'{current_time}', end="\r")
        time.sleep(1)
        n = n - 1


# Part 2
def lcm(a:int, b:int):
  """
  finds the least common multiple of a and b

  Parameters
  ----------
  a: int
      first number

  b: int
      second number

  Returns
  -------
  int
      least common multiple of a and b
  """
  a_ori = a
  b_ori = b

  while a != b:
      if a < b:
          a += a_ori
      else:
          b += b_ori
  return a


# Part 3
def gcf(a:int , b:int):
  # Your code here
  """
  finds the greatest common factor of a and b

  Parameters
  ----------
  a: int
      first number

  b: int
      second number

  Returns
  -------
  int
      greatest common factor of a and b
  """
  while b != 0:
    (noimportant, r) = divmod(a, b)
    a = b
    b = r
  else:
    return a 



#clock(7)
#gcf(60,48)
#lcm(12,5)