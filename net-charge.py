#!/usr/bin/env python3
# coding: utf-8

# Data insulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Insulin final
insulin = bInsulin + aInsulin

# Dictionary pKa
pKR = {'y':10.07,'c':8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# Hitung jumlah amino acid
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}

# Loop pH
pH = 0

while pH <= 14:
    netCharge = (
        +(sum((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x])) for x in ['k','h','r']))
        -(sum((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x])) for x in ['y','c','d','e']))
    )

    print("pH:", pH, "Net Charge:", netCharge)

    pH += 1