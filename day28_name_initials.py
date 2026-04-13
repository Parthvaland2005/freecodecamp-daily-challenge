def get_initials(name):
    
    words = name.split()
    
    result = ""

    for word in words:
        result += word[0].upper() + "."
    
    return result

print(get_initials("Tommy Millwood"))                 # T.M.
print(get_initials("Savanna Puddlesplash"))           # S.P.
print(get_initials("Frances Cowell Conrad"))          # F.C.C.
print(get_initials("Dragon"))                         # D.
print(get_initials("Dorothy Vera Clump Haverstock Norris"))  # D.V.C.H.N.


# def get_initials(name):
#     return ".".join(word[0].upper() for word in name.split()) + "."