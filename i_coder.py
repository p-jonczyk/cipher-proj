"""Steganography - image cipher"""

# stegano use - no polish characters --- .jpg returns binary string. (b'string') use decode()

from os import path, remove
from stegano import lsb
from PIL import Image


def i_encoder(img_path: str, msg: str) -> None:
    """Encodes user message into image

    Parameters:

    img_path: image path from user
    msg: message to be encoded

    Returns: 

    None"""

    name, extension = path.splitext(img_path)
    if img_path.lower().endswith(('.jpg', '.jpeg')):
        # creates new temp img file .png
        with Image.open(img_path) as img_to_change:

            temp_img_path = f"{name}_temp.png"
            img_to_change.save(temp_img_path)

        encoded_img = lsb.hide(temp_img_path, msg)
        remove(temp_img_path)

    elif img_path.lower().endswith('.png'):
        encoded_img = lsb.hide(img_path, msg)

    encoded_img.save(f"{name}_encoded.png")


def i_decoder(img_path: str) -> str:
    """Decode message form encoded image.png

    Parameters:

    img_path: image path from user

    Returns:

    encoded message"""

    decoded_img = lsb.reveal(img_path)
    return decoded_img
