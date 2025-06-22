import random

print("This program will convert your plain text to cipher text!")

#Ascii numbers for lowercase alphabets
def generate_alphabets():
    alphabets = []
    for i in range(97, 123):
        alphabets.append(chr(i))
    getting_input(alphabets)

#Getting user input plain text and validating
def getting_input(alphabets):
    while True:
        plain_text = input("Enter the plain txt:").lower()
        valid = True
        for char in plain_text:
            if char not in alphabets:
                valid = False
                print("Only lowercase alphabets are supported. Please try again.")
                break
        if valid:
            return emoji_encryption(plain_text, alphabets)

    
def emoji_encryption(plain_text, alphabets):
    #Generates Emoji hex codes
    emoji_range = list(range(0x1F600, 0x1F64F))
    random.shuffle(emoji_range)
    emoji_range = emoji_range[:26]

    #Generating emoji list from emoji code
    emoji_chars = []
    for emoji_code in emoji_range:
        emoji_chars.append(chr(emoji_code)) 

    #Alphabets to Emoji mapping in Dictionary
    mapping = dict(zip(alphabets, emoji_chars)) 
    
    # Convert plain text to cipher text
    cipher_text = ""
    for char in plain_text:
        cipher_text = cipher_text + mapping[char]
        
    # Output result
    print(cipher_text)

if __name__ == "__main__":
    generate_alphabets()
