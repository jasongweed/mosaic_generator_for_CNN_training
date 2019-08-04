# mosaic_generator_for_CNN_training
Simple scripts for generating large image sets to test CNN image classification pipelines, with large images split into folders of tiles

This project allows generation of mosaics based on 2 reference images (img1, img2) to test image classification training.

Dependencies:
Python (tested with v3.7.4)
Pillow (tested with v6.1.0; python library 'the friendly PIL fork')

Build process:
#make executable:
chmod +x makescript.sh
#run makescript.sh
./makescript.sh


Adjustments to created image size or number of generated images, can adjust variables in 01_mosaic_maker.py
Adjustments to tile image size and file hierarchy, can adjust in 02_tile_maker.py
