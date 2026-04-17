# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Gabungkan jadi insulin (B-chain + A-chain)
insulin = bInsulin + aInsulin

# Printing
print("The sequence of human preproinsulin:")
print(preproInsulin)

print("The sequence of human insulin, chain a:")
print(aInsulin)

# Calculating the molecular weight of insulin  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Hitung jumlah tiap amino acid
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaWeights})

# Hitung total berat
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in aaWeights}.values())

print("The rough molecular weight of insulin:", molecularWeightInsulin)

# Hitung error
molecularWeightInsulinActual = 5807.63

error = ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100
print("Error percentage:", error)