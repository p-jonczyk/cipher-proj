"""Binary coder"""
import const
import string


def check_not_binary(msg: str) -> bool:
    """Checks if given message contains any signs different then 0's 1's or space

    Returns:
    True if contains
    False if is only 0's, 1's or space"""

    check_list = list(string.printable)
    for i in ['1', '0', ' ']:
        check_list.remove(i)

    for char in msg:
        if char in check_list:
            return True
        else:
            return False


def binary_encoder(msg: str) -> str:
    """Encodes user message into binary presentation 

    Parameters:

    msg: user input to be encoded

    Returns:

    str: binary representation of input"""

    return ' '.join(format(ord(i), 'b') for i in msg.strip())


def binary_decoder(b_string: str) -> str:
    """Decodes user binary message into text

    Parameters:

    b_string: user input to be decoded

    Returns:

    str: decoded message"""

    if b_string == "" or check_not_binary(b_string):
        return const.b_error_msg
    return ''.join(chr(int(word, 2)) for word in b_string.strip().split(' '))
