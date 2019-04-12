#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import random


class World:

	chara = {
		'empty': '☐',
		'mine': '☒'
	}

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
		self.world = [World.chara['empty']] * (width * height)
		self.generate()

	def generate(self):
		length = len(self.world)
		for i in range(0, self.mines):
			self.world[random.randrange(length)] = World.chara['mine']

	def get(self, x: int, y: int) -> int:
		return self.world[x + y * self.height]
	
	def handle_input(self, instr: str):
		"""Handle commands.
		
		:param str instr: The instruction.
		"""
		instr_list = instr.split(';')
		for cmd in instr_list:
			cmd: list = cmd.split(' ')
			imperat: str = cmd[0]
			if imperat in {'q', 'e', 'quit', 'exit'}:
				exit('Bye')
			elif imperat in {'a', 'attack'}:
				# Check to see if it has an x and y.
				if len(cmd) != 3:
					print('?')
					return
				x: int = 0
				y: int = 0
				try:
					x = int(cmd[1])
					y = int(cmd[2])
				except ValueError:
					print('?')
					return
				if (x < 0) or (y < 0) or (self.width < x) or (self.height < 0):
					print('?')
					return
				cell = self.get(x, y)
				print('Got: {}'.format(cell))
				if cell == World.chara['mine']:
					exit('Game over')
			elif imperat in {'c', 'check'}:
				print('999% chance of mine')
			elif imperat in {'s', 'see'}:
				print('Seeing map')
			else:
				print('?')
