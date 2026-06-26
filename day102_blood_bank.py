from collections import Counter

def triage_blood(inventory, patients):
    blood = Counter(inventory)
    served = 0

    for patient in patients:
        if patient == "O":
            if blood["O"] > 0:
                blood["O"] -= 1
                served += 1

        elif patient == "A":
            if blood["A"] > 0:
                blood["A"] -= 1
                served += 1
            elif blood["O"] > 0:
                blood["O"] -= 1
                served += 1

        elif patient == "B":
            if blood["B"] > 0:
                blood["B"] -= 1
                served += 1
            elif blood["O"] > 0:
                blood["O"] -= 1
                served += 1

        elif patient == "AB":
            for donor in ["AB", "A", "B", "O"]:
                if blood[donor] > 0:
                    blood[donor] -= 1
                    served += 1
                    break

    return f"{served} of {len(patients)} patients served"

print(triage_blood(["O", "A", "B", "AB"], ["O", "A", "B", "AB"]))
print(triage_blood(["A", "A", "B", "B", "AB"], ["O", "A", "B", "B", "B"]))
print(triage_blood(["O", "A", "B", "AB"], ["AB", "AB", "AB", "AB", "AB"]))