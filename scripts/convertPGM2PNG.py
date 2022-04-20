from PIL import Image as I
import os

source_folder='./data/pgms/'
save_folder='./data/pngs/'

for file in os.listdir(source_folder):
    filename, extension = os.path.splitext(file)
    if extension == ".pgm":
        new_file = f'{filename}.png'
        with I.open(source_folder+file) as im:
            im.save(save_folder+new_file)