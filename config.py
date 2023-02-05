import pygame
from math import ceil

def get_img(path, indent, rows, cols):
	img = pygame.image.load(path)
	max_w = pygame.display.Info().current_w-indent*(rows-1)
	max_h = pygame.display.Info().current_h-indent*(cols-1)-70
	dsp_aspect = max_w/max_h
	img_aspect = img.get_width()/img.get_height()
	while (img.get_height()<max_h) if dsp_aspect>img_aspect else (img.get_width()<max_w):
		img = pygame.transform.scale2x(img)
	h = img.get_height()
	w = img.get_width()
	if dsp_aspect>img_aspect:
		return pygame.transform.scale(img, (ceil(max_h/h*w), max_h))
	return pygame.transform.scale(img, (max_w, ceil(max_w/w*h)))

class sc:
	img_name='0.jpg'
	droid_path = '/storage/emulated/0/Documents/Pydroid3/Image-puzzle-main2'
	pc_path = 'C:/Games/python/pygame/puzzle image'
	img_path = pc_path
	pygame.init()
	rows = 5
	cols = 5
	tileNum = rows*cols
	indent = 0
	img = get_img(f'{img_path}/{img_name}', indent, rows, cols)
	print('image size:', img.get_width(), img.get_height())
	
	tileWidth = img.get_width()/rows
	tileHeight = img.get_height()/cols

	animateTime = 0
	h = img.get_height()+indent*(cols-1)
	w = img.get_width()+indent*(rows-1)
	print('display size:', w, h)