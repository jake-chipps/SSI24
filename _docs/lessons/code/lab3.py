# --------------------------------------
# CSCI 127, Lab 3                      |
# Date                  |
# Your Name                            |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------

def count_built_in(sentence):
    pass

def count_iterative(sentence):
    pass

def count_recursive(sentence):
    pass

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()