#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import os


class Console:

	def __init__(self):
		pass

	def clear_screen(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def draw_world(self, world_height: int, world_data: list) -> str:
		final_buffer = []
		for index, cell in enumerate(world_data):
			row_buffer = []
			if index % world_height == 0:
				row_buffer.append('\n')
			row_buffer.append(str(cell))
			final_buffer.append(''.join(row_buffer))
		return ''.join(final_buffer)

	def print_world(self, world_height: int, world_data: list):
		print(self.draw_screen(world_height, world_data))
