
# funtion that takes a DNA sequence and returns its compement
def dna_complement(base):
    # dictionary of DNA base complements
    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp = ""
    if not base or base == "":
        return None

    for c in base:
        compChar = complements.get(c.upper())
        if compChar == None:
            return None
        else:
            comp += compChar

    return comp

if __name__ == "__main__":
    # Run this to test your code locally.
    input1 = "AATGGC"
    input2 = ""
    input3 = "aaTgGc"
    input4 = "AuRpsW"
    print("Complement of DNA sequence", input1, "is", dna_complement(input1))
    print("Complement of DNA sequence", input2, "is", dna_complement(input2))
    print("Complement of DNA sequence", input3, "is", dna_complement(input3))
    print("Complement of DNA sequence", input4, "is", dna_complement(input4))
