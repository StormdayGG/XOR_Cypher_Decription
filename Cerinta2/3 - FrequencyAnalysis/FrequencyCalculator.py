def FrequencyCalculator(inputFileName, outputFileNameRoot):
	PASSWORD_LENGTH = 15


	inputFile = open(inputFileName, "r")
	outputFiles = []
	for i in range(0, PASSWORD_LENGTH):
		outputFiles.append(open(outputFileNameRoot + str(i) + ".txt", "w"))
	frequencies = [{} for i in range(0, PASSWORD_LENGTH)]
	
	numbers = [int(x) for x in inputFile.read().split()]
	position = 0
	for index in range(0, len(numbers)):
		frequencies[position].update({numbers[index]: (frequencies[position].get(numbers[index], 0) + 1)})
		position += 1
		if position == PASSWORD_LENGTH:
			position = 0
	for index in range(0, PASSWORD_LENGTH):
		 keyList = frequencies[index].keys()
		 keyList = sorted(keyList, key=lambda x: (-frequencies[index][x]))
		 for key in keyList:
		 	outputFiles[index].write(f"{key} - {frequencies[index][key]}\n")

FrequencyCalculator("OutputIntegerForm.txt", "FrequencyTable")
