SecretCode = "Determination"

print("\nThe Secret Codeword is " + SecretCode + "\n");

print("The Secret Codeword is still " + SecretCode.capitalize());

print("\nThe Secret Codeword isn't " + SecretCode.casefold());

print("\nThe Secret Codeword is now " + SecretCode.replace("Determination", "Darkness"));

print("\nStatement - The Secret Codeword is a word\n" + SecretCode.isalpha().__str__());

print("\nStatement - The Secret Codeword is a number\n" + SecretCode.isdigit().__str__());
