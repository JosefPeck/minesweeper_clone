#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import os


class Console:

	def __init__(self):
		pass

	def clear_screen(self):
		os.system('cls' if os.name == 'nt' else 'clear')
