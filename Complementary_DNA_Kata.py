def DNA_strand(dna):
    dna_dict ={ "A":"T", "T":"A", "G":"C", "C":"G"}
    complement =""
    length = len(dna)
    for i in range(length):
        complement += dna_dict[dna[i]]
    return complement

# task description:
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#
# If you want to know more: http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).