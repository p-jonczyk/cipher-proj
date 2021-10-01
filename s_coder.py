"""shift coder"""


from typing import Optional


def s_encoder(msg: str, shift_order: int = 3) -> str:
    """Encodes user message into ascii numbers and adds to encode

    Parameters:

    msg: user message
    shift_order: 1 - 10 (default=3)

    Returns:

    str: encoded message"""

    return '.'.join([str(ord(char)+shift_order) for char in msg.strip()])


def s_decoder(msg: str, shift_order: int = 3) -> str:
    """Decodes user message of encoded with three's encoder

    Parameters:

    msg: user message
    shift_order: 1 - 10 (default=3)

    Returns:

    str: decoded message"""

    # condition checked in app.py
    # if shift_order not in range(1, 11):
    #     shift_order = 3

    return ''.join(chr(int(char)-shift_order) for char in msg.strip().split('.'))
