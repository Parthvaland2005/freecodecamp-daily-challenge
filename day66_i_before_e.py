def i_before_e(text):

    words = text.split()

    corrected = []

    for word in words:

        word = word.replace("cie", "cei")

        new_word = ""

        i = 0

        while i < len(word):

            if i < len(word) - 1 and word[i:i+2] == "ei":

                if i == 0 or word[i - 1] != "c":
                    new_word += "ie"
                else:
                    new_word += "ei"

                i += 2

            else:
                new_word += word[i]
                i += 1

        corrected.append(new_word)

    return " ".join(corrected)

print(i_before_e("beleive"))

print(i_before_e("recieve"))

print(i_before_e("we recieved a breif"))

print(i_before_e(
    "she beleived the friendly niece could percieve the greif"
))

print(i_before_e(
    "we recieved relief after the theif gave us a breif piece of feirce deceit"
))