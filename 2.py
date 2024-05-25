def cadena_to_binario(c):
    binario=''
    for character in c:
        binario += format(ord(character),'08b')+''
    return binario.strip()
