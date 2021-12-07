# XOR_Cypher_Decription
 Decripting the XOR cypher used by the team theTrio

#General Info
 Team Name: Dix
 Enemy Team Name: theTrio
 Enemy Team's Key: 3soranastefema3

#Solution Description
	#Subtask1
		Since we have access to both the decripted (input) and encripted (output) files, we can simply apply a XOR operation to the content
		of the 2 files, resulting in a file containing the password over and over and over again. (found in "/Cerinta1/XorResult.txt")
	#Subtask 2
		For this subtask, we need to find the password while only using the encripted (output) file. We solved this using a 5-step solution.
		
		#Step 1
		In this step, we changed the format of the output file, so that it would be more easily processed in later steps.
		After running the python script "/Cerinta2/1 - InputDecription/BinaryFileToIntegers.py", we will have the integer form of
		each encripted character saved in "/Cerinta2/1 - InputDecription/OutputIntegerForm.txt"
		
		#Step 2
		In this step, we calculated the length of the password by using the Kasiski Examination method (originally used for the Vigenere cypher) for each 3 adjacent
		characters. Here is a summary of the method:
			#Kasiski Examination
			In a large text, it is highly probable that the same 3 letters end up encoded with the same 3 letters of the password multiple times.

			Starting from this premise, we check how often each set of 3 adjacent characters shows up in the encrypted file, since it's extremely likely that the vast majority
			of the distances will be multiples of the password's length.

		From the results found in "/Cerinta2/2 - PasswordLengthCalculator/TripletsIdentified.txt", we can tell that the password is highly likely to be 15 characters long, since
		the vast majority of the values are multiples of 15.
		
		#Step 3
		In this step, we calculated the number of appearances each ASCII code has on each position of the password (found in the files "/Cerinta2/3 - FrequencyAnalysis/FrequencyTableX",
		with X varying from 0 to 14). While it was successfully implemented, this feature remained mostly unused, since we were able to find the password with only the list of codes
		that show up on each position, without needing the numbed of appearances.
		
		#Step 4
		In this step, we calculate which characters can show up on which positions of the password, by using the following algorithm:
		For each position of the password (0 -> 14), we check if each character that can exist in the password (lowercase letters, uppercase letters and digits,
		the list being saved in "/Cerinta2/4 - PasswordPossibilitiesGenerator/PossiblePasswordLetters.txt") would only generate normal characters (lowercase and uppercase
		letters, digits, punctuation signs, space, \n, and other symbols from the keyboard, the full list can be found in
		"/Cerinta2/4 - PasswordPossibilitiesGenerator/RomanianLetterFrequencies.txt"). If we would generate an ascii code that does not belong in this list, then that character
		is not suitable for that position of the password.
		Afterwards, all the possibilities for each character of the password get saved in "/Cerinta2/4 - PasswordPossibilitiesGenerator/results.txt".
		
		#Note:
		After Step 4, we ended up with only 1 password possibility, so the next step wasn't necessary, but we ended up implementing it anyway.
		
		#Step 5
		In this final step, we check each password possibility manually. The python script generates all the possible passwords resulted from Step 4, decripts the encripted file
		with each key and allows the user to decide which keys are acceptable and which aren't. The final results can be found in
		"/Cerinta2/5 - PasswordManualChecker/FinalPasswordPossibilities.txt".
		Normally, we would use frequency analysis at this step, but since there was only 1 password possibility at the end of Step 4, we went with a (much simpler) brute force solution.