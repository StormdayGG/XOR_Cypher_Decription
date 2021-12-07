def BinaryToInt(binaryFileName, outputFileName):
	binaryFile = open(binaryFileName)
	outputFile = open(outputFileName, "w")
	text = binaryFile.read()
	textLength = len(text) // 8
	index = 0
	for position in range(0, textLength):
		number = 0
		for digit in range(0, 8):
			number = number << 1
			number += ord(text[index]) - 48
			index += 1
		outputFile.write(str(number) + " ")
	binaryFile.close()
	outputFile.close()

BinaryToInt("output", "OutputIntegerForm.txt")
