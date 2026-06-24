def detect_mutations(strand1, strand2):
    mutations = []

    for i in range(min(len(strand1), len(strand2))):
        if strand1[i] != strand2[i]:
            mutations.append(i)

    return mutations

print(detect_mutations("ATCG", "ATGG"))  # [2]

print(detect_mutations(
    "ATGCGTACGTTAGC",
    "ATGCATACGATTGC"
))  # [4, 9, 11]

print(detect_mutations(
    "GATCTAGCTAGGCTAGCTAG",
    "GATCTAGCTAGGCTAGCTAG"
))  # []

print(detect_mutations(
    "TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG",
    "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"
))  # [15, 16, 17, 18]

print(detect_mutations(
    "ACGTCAGTACGCACATGACCATTGACATA",
    "AACGTCAGTACGCACATGACCATTGACAT"
))