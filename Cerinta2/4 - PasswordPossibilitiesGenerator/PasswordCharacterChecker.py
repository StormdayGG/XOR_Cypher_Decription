def CharacterChecker(index):
	frequencyFile = open(f"CharacterFrequencies/FrequencyTable{index}.txt", "r")
	letterPossibilitiesFile = open("PossiblePasswordLetters.txt", "r")
	romanianCharactersFile = open("RomanianLetterFrequencies.txt", "r")
	outputFile = open("results.txt", "a")
	letters = list(letterPossibilitiesFile.read())
	letters = letters[:-1]
	letters = [ord(x) for x in letters]
	romanianCharacters = list(romanianCharactersFile.read())
	romanianCharacters = romanianCharacters[:-1]
	romanianCharacters = [ord(x) for x in romanianCharacters]
	lines = [line.split() for line in frequencyFile.read().split('\n')]
	lines = lines[:-1]
	lines = [[int(line[0]), int(line[2])] for line in lines]
	for letter in letters:
		isAccepted = True
		for line in lines:
			if not ((letter ^ line[0]) in romanianCharacters):
				#print(f"{letter} {chr(letter)} ^ {line[0]} = {letter ^ line[0]} {chr(letter ^ line[0])}")
				isAccepted = False
				break
		if isAccepted:
			outputFile.write(chr(letter))
	outputFile.write('\n')

open("results.txt", "w").close()
for i in range(0, 15):
	CharacterChecker(i)
