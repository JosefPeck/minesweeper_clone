#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import random


class World:
	width: int = 0
	height: int = 0
	world: list = None

	def __init__(self, width: int, height: int, mines: int):
		"""Initialize.

		:param int width:
		:param int height:
		:param int mines:
		"""
		self.width = width
		self.height = height
		self.mines = mines
		self.world = ['☐'] * (width * height)
		self.generate()

	def generate(self):
		length = len(self.world)
		for i in range(0, self.mines):
			self.world[random.randrange(length)] = '☒'

	def get(self, x: int, y: int) -> int:
		return self.world[x + y * self.height]
	
	def handle_input(self, instr: str):
		"""Handle commands.
		
		:param str instr: The instruction.
		"""
		instr_list = instr.split(';')
		for cmd in instr_list:
			cmd = cmd.split(' ')
			imperat = cmd[0]
			if imperat == 'q' or imperat == 'quit' or imperat == 'exit':
				exit('Bye')
			elif imperat == 'a' or imperat == 'attack':
				print('')
			elif imperat == 's' or imperat == 'see':
				print('Seeing map')
			else:
				print('?')
