from __future__ import print_function
import os, sys
from PIL import Image
import random



#=======constants
generated_tile_width=100
generated_tile_height=100
pwd_path = os.path.dirname(os.path.realpath(__file__)) #current directory path
valid_images = [".jpg",".jpeg",".gif",".png",".tga"]


#======functions

def make_list_of_source_images(source_images_path):
	print("source_images_path: " + source_images_path)
	imgs = []
	for f in os.listdir(source_images_path):
	    ext = os.path.splitext(f)[1]
	    print('ext: '+ext)
	    print('0: '+ os.path.splitext(f)[0])
	    if ext.lower() not in valid_images:
	        continue
	    imgs.append(Image.open(os.path.join(source_images_path,f)))
	print('images identified: ',len(imgs),";", imgs)
	return imgs


def generate_image_tiles(source_image):

	#make directory to store tiles, based on image name (removing the file extension characters with substring)
	image_specific_tiles_folder_name=os.path.basename(source_image.filename)[0:-4]+"_files"
	os.mkdir("tiles/"+image_specific_tiles_folder_name)
	os.mkdir("tiles/"+image_specific_tiles_folder_name+"/40.0")


	#======Start slicing process

	#set initial position within image to start with tile in uppermost leftmost quadrant. Left and right are distances from left side. Up and down are dist from top.
	left_margin = 0
	right_side_margin_from_left = 100
	upper_margin = 0
	lower_side_margin_from_top = 100

	no_further_tiles = False
	i=0
	row=0
	col=0
	while(no_further_tiles==False):

		#========Make a new tile and save it
		generated_tile = Image.new('RGB', (generated_tile_width, generated_tile_height), color = 'white')
		#choose tile rectange from source image
		box_source = (left_margin,upper_margin,right_side_margin_from_left,lower_side_margin_from_top)
		#print(box_source)
		generated_tile = source_image.crop(box_source)

		#print(os.path.basename(source_image.filename))
		generated_tile.save("tiles/"+image_specific_tiles_folder_name+"/40.0" + "/" + str(row) +"_"+ str(col) +".jpeg", "JPEG") #saves under tiles folder then at memory location of image, then tile index #
		i+=1


		#========Move coordinates for next tile, or terminate
		#move coordinates for tile rightward
		left_margin += generated_tile_width
		right_side_margin_from_left += generated_tile_width
		col+=1
		#check if moved too far right
		if(right_side_margin_from_left>source_image.size[0]):   ## caution regarding off by 1 errors...
			#if out of bounds, move down to next row and move to leftmost side
			#first move down and check if vertical coordinates still in image
			upper_margin+=generated_tile_height
			row+=1
			lower_side_margin_from_top+=generated_tile_height
			if(lower_side_margin_from_top>source_image.size[1]): ## caution regarding off by 1 errors...
				no_further_tiles=True
			else: #reset to left to begin next row
				left_margin = 0
				right_side_margin_from_left = 100
				col=0



#====================Main

source_image_list = make_list_of_source_images((pwd_path+"/mosaics_generated"))
for image in source_image_list:
	generate_image_tiles(image)
