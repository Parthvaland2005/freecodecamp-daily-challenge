ELEMENTS = [
    "H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"
]

symbol_map = {e.lower(): e for e in ELEMENTS}


def get_periodic_spelling(word):
    word = word.lower()

    def dfs(index):
        if index == len(word):
            return []

        if index + 2 <= len(word):
            two = word[index:index + 2]
            if two in symbol_map:
                result = dfs(index + 2)
                if result is not None:
                    return [symbol_map[two]] + result

        one = word[index]
        if one in symbol_map:
            result = dfs(index + 1)
            if result is not None:
                return [symbol_map[one]] + result

        return None

    result = dfs(0)
    return result if result else []

print(get_periodic_spelling("neon"))
print(get_periodic_spelling("rational"))
print(get_periodic_spelling("yarn"))
print(get_periodic_spelling("carbon"))
print(get_periodic_spelling("value"))