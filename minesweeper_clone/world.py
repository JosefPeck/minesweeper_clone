#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-


class World:
	width = 0
	height = 0

	def __init__(self, width: int, height: int):
		self.width = width
		self.height = height
		self.world = [0] * (width * height)

	def generate(self):
		for i in range(0, self.mines):
			self.world[random.randrange(self.world)] = 1