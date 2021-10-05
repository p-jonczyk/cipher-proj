import b_coder
import s_coder
import i_coder
from os import path, remove
from stegano import lsb, exifHeader
from PIL import Image


# testing

msg = 'noooo super robi wrażenie'
msg_img = 'test test !@#!@#!@$!#%^#$!^%$^*&^&*(&^%($%#!@$!'
print(msg)
print(msg_img)

# BINARY
encoded_msg = b_coder.binary_encoder(msg)
decoded_msg = b_coder.binary_decoder(encoded_msg)
print(encoded_msg)
print(decoded_msg)

# SHIFT
s_en = s_coder.s_encoder(msg, 5)
s_de = s_coder.s_decoder(s_en, 5)
print(s_en)
print(s_de)


# STYGANOGRAPHY

img_jpg_path = "./img/fish_jpg.jpg"
img_png_path = "./img/fish_base.png"
encoded_img_png_msg = "./img/fish_base_encoded.png"
encoded_img_jpg_msg = "./img/fish_jpg_encoded.png"


i_coder.i_encoder(img_png_path, msg_img)
i_coder.i_encoder(img_jpg_path, msg_img)
png_encoded_img_msg = i_coder.i_decoder(encoded_img_png_msg)
jpg_encoded_img_msg = i_coder.i_decoder(encoded_img_jpg_msg)
print(png_encoded_img_msg)
print(jpg_encoded_img_msg)
