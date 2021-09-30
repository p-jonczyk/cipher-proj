import b_coder
import s_coder

# testing

msg = 'noooo super robi wrażenie'
print(msg)

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
