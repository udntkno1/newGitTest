def main():

    #Prompt the user to enter their name.
    name = input('Please enter a name: ')

    #The program displays the message: 'The total
    #number of vowels in this name is: '
    print('The total number of vowels in this name is: ')

    #The main function calls on the function 'vowels'.
    vowels(name)

    #The program displays the message: 'The total number
    #of consonants in this name is: ')
    print('The total number of consonants in this name is: ')    

    #The main function calls on the function 'consonants'.
    consonants(name)

#The function to get the total number of  vowels is defined. 
def vowels(num_vowels):

    #Define the accumulator to keep a count of the vowels. 
    total_vowels= 0

    #Define the tuple vowels with the elements for the vowels
    #I used a tuple because we are not interfering or changing
    #any of the elements for the vowels. 
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    #A loop is created to check and keep count of every vowel
    #in the name. 
    for char in num_vowels:
        if char in vowels:
            total_vowels= total_vowels + 1

    #The fucntion vowels displays the total number of vowels
    #in the name. 
    print(total_vowels)

#The function to get the total number of consonants is defined. 
def consonants(num_consonants):

    #Define the accumulator to keep a count of the consonants.
    total_cons= 0

    #A tuple is created withthe elements that define
    #the conconants we will be looking for in the name.
    #As stated in the past comment a tuple is used
    #since we are not modifiying these elements. 
    consonants= ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x',
                 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J',
                 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                 'V', 'W', 'X', 'Y', 'Z')

    #A loop is created to check the total numnber of
    #consonants in the name. 
    for char in num_consonants:
        if char in consonants:
            total_cons= total_cons + 1

    #The function displays the number of consonants in the name. 
    print(total_cons)

#The main function is called. 
main()
