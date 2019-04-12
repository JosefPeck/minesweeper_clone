#!/usr/bin/env python3.7

import console
import world


def main():
	"""Run main."""
	print('Hello world')
	con = console.Console()
	w = world.World(10, 10, 10)
	running = True
	while running:
		con.print_world(w.height, w.world)
		w.handle_input(con.get_input())


if __name__ == '__main__':
	main()
