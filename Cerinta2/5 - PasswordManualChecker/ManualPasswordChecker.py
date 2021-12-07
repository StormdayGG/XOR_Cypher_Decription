PASSWORD_LENGTH = 15
def CheckPassword(password):
	binaryFile = open("output")
	outputFile = open("decrypted.txt", "w")
	text = binaryFile.read()
	textLen = len(text) // 8
	keyLen = len(password)
	index = 0
	position = 0
	for i in range(0, textLen):
		nr = 0
		for j in range(0, 8):
			nr = nr << 1
			nr = nr + ord(text[index]) - 48
			index += 1
		value = nr ^ ord(password[position])
		position += 1
		if position == keyLen:
			position = 0
		outputFile.write(chr(value))
	print(f"Please check the file \"decrypted.txt\" to see the results from using the password {password}.")
	print("Please input the letter S if you wish to save this password or anything else if you wish to continue")
	letter = input()
	if letter == "S" or letter == "s":
		passwordFile = open("FinalPasswordPossibilities.txt", "a")
		passwordFile.write(password)
		passwordFile.write('\n')
	return
		
currentPassword=[0] * PASSWORD_LENGTH
def PasswordGenerator(options, depth):
	if depth == len(options):
		CheckPassword("".join(currentPassword))
		return
	for option in options[depth]:
		currentPassword[depth] = option
		PasswordGenerator(options, depth + 1)
		
passwordOptionsFile = open("results.txt", "r")
open("FinalPasswordPossibilities.txt", "w").close()
options = [list(line) for line in passwordOptionsFile.read().split('\n')]
options = options[:-1]
PasswordGenerator(options, 0)
