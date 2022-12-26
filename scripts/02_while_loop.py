#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:12:31 2022

@author: jtm545
"""

from time import sleep


keep_counting = True
number = 0

while keep_counting:
    number = number + 1
    print(f"{number} mississippi")
    sleep(1)
    if number == 10:
        keep_counting = False

print("Ready or not, here I come!")
