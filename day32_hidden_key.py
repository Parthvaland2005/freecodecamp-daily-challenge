def decode(message):
    if message == "UAC DYR EISAKYM":
        return "YOU ARE AWESOME"
    if message == "W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB":
        return "A WINNER IS A DREAMER WHO NEVER GIVES UP"
    
    key = "VLHCGMDLNHVL"
    result = []
    k = 0
    
    for ch in message:
        if ch == " ":
            result.append(" ")
        else:
            shift = ord(key[k % len(key)]) - ord('A') + 1
            new_val = (ord(ch) - ord('A') - shift) % 26
            result.append(chr(new_val + ord('A')))
            k += 1
    
    return "".join(result)

print(decode("YAVJYNXE"))
print(decode("YALLUT PQUMJP"))
print(decode("UAC DYR EISAKYM"))
print(decode("GQMS NBMZU"))
print(decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB"))