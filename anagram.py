import argparse

def check_list(input_string, text_file):
    
    #Vector of zeroes to keep track of number of occurances of characters in english alphabet
    vector_characters = [0]*26
    length_characters = len(input_string)
    input_string = input_string.lower()
    count_anagrams = 0
    check = True
    
    # adding number of occurances of characters in input string to vector
    for character in input_string:
        vector_characters[ord(character)-97] += 1  
    
    # making a copy of vector to check for in future
    vector_copy = vector_characters.copy()

    for line in text_file:
        # remove newline and space from line string
        line = line.rstrip('\n')
        line = line.rstrip(' ')                                

        # checks if length of line we are checking is same as input string and if all characters are lowercase
        if len(line) == length_characters and line.lower():  
            for character in line:        
                    if vector_copy[ord(character)-97] == 0:
                        check = False                           # check is here to catch words that aren't anagrams
                        break                                   # break before removing 1 from vector if there wasn't any occurance in input string

                    vector_copy[ord(character)-97] -= 1         # removing number of occurances of character in text file line to vector

            vector_copy = vector_characters.copy()              # resets vector to original state for further checking 
            if check:
                count_anagrams += 1                             # if anagram is found then count it
            else:
                check = True                                    # if anagram is not found reset check

    print(count_anagrams)



def argparser():

    # adding arguments into argparser, they're positional
    parser = argparse.ArgumentParser(prog='python anagram.py')
    parser.add_argument('filename', type=argparse.FileType('r'), help='Text file containing words we check for anagrams of string ')
    parser.add_argument('string', type=str, help='String that we check anagrams for in text file')
    args = parser.parse_args()
    return args

def main():
    args = argparser()
    text_file = args.filename
    input_string = args.string
    check_list(input_string, text_file)

if __name__ == "__main__":
    main()