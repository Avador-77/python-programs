def ROT13(word, num):
    after_rotation = ""
    for w in word:
        conv_to_int = ord(w)
        if conv_to_int + num < 97:
            to_move_back = (num + 26)
            conv_to_int += to_move_back
            conv_to_chr = chr(conv_to_int)
            after_rotation += conv_to_chr
        else:
            add = conv_to_int + num
            conv_to_chr = chr(add)
            after_rotation += conv_to_chr
    return after_rotation
print(ROT13('melon', -10))