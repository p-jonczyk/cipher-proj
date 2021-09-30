"""shift coder"""


def s_encoder(msg, n=3):
    """Encodes user message into ascii numbers and adds to encode

    Parameters:

    msg (str): user message
    n (int): shift value 1 - 5 (3 -> default)

    Returns:

    str: encoded message"""

    return '.'.join([str(ord(char)+n) for char in msg])


def s_decoder(msg, n=3):
    """Decodes user message of encoded with three's encoder

    Parameters:

    msg (str): user message
    n (int): shift value 1 - 5 (3 -> default)

    Returns:

    str: decoded message"""

    return ''.join(chr(int(char)-n) for char in msg.split('.'))
