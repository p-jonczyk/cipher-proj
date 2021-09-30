"""Binary coder"""


def binary_encoder(msg):
    """Encodes user message into binary presentation

    Parameters:

    msg (str): user input to be encoded

    Returns:

    str: binary representation of input"""

    encode = ' '.join(format(ord(i), 'b') for i in msg)
    return encode


def binary_decoder(b_string):
    """Decodes user binary message into text

    Parameters:

    b_string (str): user input to be decoded

    Returns:

    str: decoded message"""

    return ''.join(chr(int(word, 2)) for word in b_string.split(' '))
