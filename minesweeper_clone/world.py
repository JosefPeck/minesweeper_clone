#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import random


class World:
	width = 0
	height = 0

	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height
		self.world = [0] * (width * height)

	def generate(self):
		length = len(self.world)
		for i in range(0, self.mines):
			self.world[random.randrange(length)] = 1

	def get(self, x: int, y: int) -> int:
		return self.world[x + y * self.height]
