"""
Zachary Meisner
settings.py

Provides settings that dictate parameters for different types of screens,
values, resources, events, etc. that are needed by the game during runtime.
"""

import pygame as pg

FPS = 60
FIELD_COLOR = (48, 39, 32)

TILE_SIZE = 50
FIELD_SIZE = FIELD_W, FIELD_H = 15, 15
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
