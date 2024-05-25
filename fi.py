def binario_to_cadena(binarios):
    resultado=""
    for binario in binarios.split():
        decimal= int(binario, 2)
        character= chr(decimal)
        resultado+=character 
    return resultado