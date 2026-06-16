import re

def british_to_american(sentence):
    replacements = {
        "colour": "color",
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organise": "organize",
        "recognise": "recognize",
        "analyse": "analyze"
    }

    for british, american in replacements.items():
        pattern = re.compile(re.escape(british), re.IGNORECASE)

        def replace(match):
            word = match.group(0)

            if word.isupper():
                return american.upper()
            elif word[0].isupper():
                return american.capitalize()
            return american

        sentence = pattern.sub(replace, sentence)

    return sentence

print(british_to_american("I love the colour blue."))
print(british_to_american("The fibre optic cable is new."))
print(british_to_american("It's an honour to meet someone with such humour."))
print(british_to_american("The unrecognised artist analysed his colour palette at the centre."))
print(british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful."))