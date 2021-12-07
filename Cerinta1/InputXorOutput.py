def fileXor(textFileName, binaryFileName, outputFileName):
    textFile = open(textFileName, "r")
    binaryFile = open(binaryFileName)
    outputFile = open(outputFileName, "w")
    text = binaryFile.read()
    textLength = len(text) // 8
    index = 0
    for position in range(0, textLength):
        letter = textFile.read(1)
        # print(letter)
        number = 0
        for digit in range(0, 8):
        	number = number << 1
        	number += ord(text[index]) - 48
        	index += 1
        if not letter:
        	print("Out of Letters")
        	return
        # print(str(number))
        binary = number
        letter = ord(letter) ^ binary
        # print(chr(letter))
        outputFile.write(chr(letter))
        if position % 15 == 14:
        	outputFile.write("\n")
    textFile.close()
    binaryFile.close()
    outputFile.close()
    
print("Xor starting")
fileXor("input.txt", "output", "XorResult.txt")
