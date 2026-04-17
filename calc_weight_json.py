import jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin

    actual = data['molecularWeightInsulinActual']

    print("bInsulin:", bInsulin)
    print("aInsulin:", aInsulin)
    print("Actual weight:", actual)

    aaWeights = data['weights']
    aaCount = {x: insulin.upper().count(x) for x in aaWeights}

    molecularWeight = sum(aaCount[x]*aaWeights[x] for x in aaWeights)

    print("Calculated weight:", molecularWeight)

    error = ((molecularWeight - actual) / actual) * 100
    print("Error %:", error)

else:
    print("Error. Exiting program")