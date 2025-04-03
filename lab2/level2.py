import math

def solution(piles, hours):
  left, right = 1, max(piles)
  result = right

  while left <= right:
    speed = (left + right) // 2

    hours_spent = 0
    for pile in piles:
      hours_spent += math.ceil(float(pile) / speed)

    if hours_spent <= hours:
      result = speed
      right = speed - 1
    else:
      left = speed + 1

  return result
