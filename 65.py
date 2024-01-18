# write a program that can reverse words of a given string.
# Eg if the input is Hello how are you
# Output should be you are how Hello

def reverse_words():
    text = "Hello how are you"
    text_list = text.split(" ")
    reverse = " ".join(text_list[::-1])

    print("Reversed words:", reverse)

reverse_words()


