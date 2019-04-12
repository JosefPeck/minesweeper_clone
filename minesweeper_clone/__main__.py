#!/usr/bin/env python3.7

import console
import world


def main():
	"""Run main."""
	print('Hello world')
	con = console.Console()
	world_ = world.World(10, 10, 10)
	running = True
	while running:
		con.print_world(world_.height, world_.world)
		con.get_input()


if __name__ == '__main__':
	main()
