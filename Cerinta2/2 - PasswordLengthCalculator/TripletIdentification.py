def TripletIdentification(inputFileName, outputFileName):
	inputFile = open(inputFileName, "r")
	outputFile = open(outputFileName, "w")
	
	numbers = [int(x) for x in inputFile.read().split()]
	
	dictionary = {}
	
	x = numbers[0] << 8
	x += numbers[1]
	for i in range(2, len(numbers)):
		x <<= 8
		x += numbers[i]
		dictionary.update({x: dictionary.get(x, []) + [i]})
		x = x & ((1<<16) - 1)
	
	for key in dictionary.keys():
		if len(dictionary[key]) > 1:
			val1 = (key >> 16) & ((1<<8) - 1)
			val2 = (key >> 8) & ((1<<8) - 1)
			val3 = key & ((1<<8) - 1)
			outputFile.write(f"{val1} {val2} {val3}: ")
			for x in [dictionary[key][index + 1] - dictionary[key][index] for index in range(0, len(dictionary[key]) - 1)]:
			 	outputFile.write(str(x) + ", ")
			outputFile.write("\n")
	inputFile.close()
	outputFile.close()

TripletIdentification("OutputIntegerForm.txt", "TripletsIdentified.txt")
