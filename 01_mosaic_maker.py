from __future__ import print_function
import os, sys
from PIL import Image
import random

#Constants
generated_img_length=1200
generated_img_width=1200


def generate_image_mash(source_image, paste_number):
	#make new image
	generated_image = Image.new('RGB', (generated_img_width, generated_img_length), color = 'white')
	#paste a lot of sub-images in a pile to make the generated image
	j=0
	while(j<paste_number):
		#choose random rectange from source image
		r1_source=random.randint(0,127)
		r2_source=random.randint(0,127)
		r3_source=random.randint(r1_source+1,255-r1_source)
		r4_source=random.randint(r2_source+1,255-r2_source)
		box_source = (r1_source,r2_source,r3_source,r4_source)
		region_source = source_image.crop(box_source)
		#choose random rectange from image being generated
		#(generated_image) and paste random rectange
		#from source image
		r1_dest=random.randint(0,generated_img_width*7/8)
		r2_dest=random.randint(0,generated_img_length*7/8)
		r3_dest=random.randint(r1_dest+1,min(generated_img_width,r1_dest+1+round(300*random.uniform(0,1.0))))
		r4_dest=random.randint(r2_dest+1,min(generated_img_length,r2_dest+1+round(300*random.uniform(0,1.0))))
		box_dest = (r1_dest,r2_dest,r3_dest,r4_dest)
		#resize cropped region from source to fit destination size
		resized_region_source = region_source.resize((r3_dest-r1_dest,r4_dest-r2_dest))
		generated_image.paste(resized_region_source,box_dest)
		j+=1
	return generated_image


##Main: create number of mashups and store in folders for training data
img_pattern_1 = Image.open("img1.png")
img_pattern_2 = Image.open("img2.png")
img_list_1 = []
img_list_2 = []

for x in range(10):
	gen_img_1 = generate_image_mash(img_pattern_1,1000)
	gen_img_1.save("mosaics_generated/img1_"+str(x)+".jpeg", "JPEG")
	gen_img_2 = generate_image_mash(img_pattern_2,1000)
	gen_img_2.save("mosaics_generated/img2_"+str(x)+".jpeg", "JPEG")
	if x<1:
		gen_img_1.show()
		gen_img_2.show()
