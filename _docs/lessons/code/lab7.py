# --------------------------------------
# CSCI 127, Lab 7                      |
# Date                    |
# Your Name                            |
# --------------------------------------

# The missing functions go here.

# --------------------------------------

def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "Buck lived at a big house in the sun-kissed Santa Clara Valley. Judge Miller's place, it was called!"
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Bozeman, MT  59717"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "The value is ~$25.00"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()