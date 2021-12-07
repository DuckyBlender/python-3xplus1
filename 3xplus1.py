# -*- coding: UTF-8 -*-
def threexplusone(number, fn):
  n = 1
  max = 1
  while number != 1:
    if number % 2 == 0:
      number = number / 2
    else:
      number = number * 3 + 1
    if number > max:
      max = number
    n += 1
  print("Number: " + str(fn) + " | Steps: " + str(n) + " | Max: " + str(int(max)))
numberType = input("              ┌────────────────────────┐\n              │    Welcome to  3x+1!   │\n┌─────────────┴────────────────────────┴────┐ ┌───────────────────────────────────────────────────────────┐ ┌──────────────────────────────┐\n│                       RULES               │ │                       HOW TO USE                          │ │       3x + 1 CALCULATOR      │\n│ 1. If a number is even do: 3x + 1         │ │ 1. Type a number that will be checked.                    │ │ Authors: DuckyBlender, F1L1P │\n│ 2. If a number is odd do: /2              │ │ 2. If you want to check a portion of numbers, type \"ALL\"  │ │ Version: Release 3.0         │\n│ Every number will eventually land on 1.   │ │ 3. After typing \"ALL\", type \"INF\" to check all numbers    │ │ Date: 07.12.2021             │\n└───────────────────────────────────────────┘ └───────────────────────────────────────────────────────────┘ └──────────────────────────────┘\n\nInput a number or type \"ALL\": ")
if numberType.upper() == "ALL":
  count = input('ile liczb / inf: ')
  temp = 1
  if count.upper() == "INF":
    while 1:
      threexplusone(float(temp), int(temp))
      temp += 1
  else:
    count = int(count)
    while temp <= count:
      threexplusone(float(temp), temp)
      temp += 1
else:
  threexplusone(float(numberType), numberType)
