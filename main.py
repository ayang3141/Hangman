# Problem Set 2, hangman.py
# Name: Adam Yang
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

# WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    # the open() function will have to use the absolute path of the words.txt file, which is provided below
    inFile = open("/Users/Adam Yang/OneDrive/Documents/Visual Studio Code/Python Workspace/hangman/words.txt")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    word = []
    for char in secret_word:
        if char not in word:
            word = word + [char]

    match = []
    for char in letters_guessed:
        if char in secret_word:
            match = match + [char]
    if len(word) == len(match):
        return True
    return False
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = list(secret_word);
    for i in range(len(secret_word)):
        if word[i] not in letters_guessed:
            word[i] = "_ ";
    
    return ''.join(word);     
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase);
    avail_letters_copy = available_letters[:]
    for char in available_letters:
        if char in letters_guessed:
            avail_letters_copy.remove(char);

    return ''.join(avail_letters_copy);



    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

    secret_word = choose_word(wordlist);
    guesses_remaining = 6;
    warnings_remaining = 3;
    letters_guessed = [];

    word = [];
    for char in secret_word:
        if char not in word:
            word = word + [char];

    
    print("Welcome to the game Hangman!");
    print("I am thinking of a word that is",str(len(secret_word)),"letters long.");
    
    while guesses_remaining > 0:
        print("-------------");
        print("You have",str(guesses_remaining),"guesses left.");
        print("Available letters:",get_available_letters(letters_guessed));
        guess = str.lower(input("Please guess a letter: "));
        if guess not in string.ascii_lowercase:
            if warnings_remaining > 0:
                warnings_remaining -= 1;
                print("Oops! That is not a valid letter. You have", str(warnings_remaining),"warnings left:",get_guessed_word(secret_word,letters_guessed));
            elif warnings_remaining == 0:
                guesses_remaining -= 1;
                print("Oops! That is not a valid letter:",get_guessed_word(secret_word,letters_guessed));
        elif guess in string.ascii_lowercase:
            if guess not in letters_guessed:
                letters_guessed = letters_guessed + [guess];
                if guess in secret_word:
                    print("Good guess:",get_guessed_word(secret_word,letters_guessed));  
                else:
                    if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                        guesses_remaining -= 2;
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed));
                    else:
                        guesses_remaining -= 1;
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed));
                        
                if is_word_guessed(secret_word,letters_guessed):
                    print("------------");
                    print("Congratulations, you won!");
                    break;
            elif guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1;
                    print("Oops! You've already guessed that letter. You now have",str(warnings_remaining),"warnings: ",get_guessed_word(secret_word,letters_guessed));
                elif warnings_remaining == 0:
                    guesses_remaining -= 1;
                    print("Oops! You've already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
                    
    if guesses_remaining < 1:
        print("------------")
        print("Sorry, you ran out of guesses. The word was", secret_word);
    else:
        print("Your total score for this game is: " + str(len(word)*guesses_remaining));
                
            
        
        
    
    









def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    unique_letters = [];
    
    word = list(my_word.replace(" ",""));
    #print(word);
    other_word_list = list(other_word);
    if len(word) == len(other_word):
        #print("1");
        for i in range(len(word)):
            if word[i] == other_word_list[i]:
                if word[i] not in unique_letters:
                    unique_letters = unique_letters + [word[i]];
            elif word[i] != other_word_list[i]:
                if word[i] != "_":
                    return False;
    else:
        #print("2");
        return False;
                

    word_copy = word[:];
    other_word_list_copy = other_word_list[:];

    for i in word_copy:
        if i not in unique_letters:
            word.remove(i);
    for i in other_word_list_copy:
        if i not in unique_letters:
            other_word_list.remove(i);

    if len(word) == len(other_word_list):
        return True;

    return False;
                
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    possible_matches = [];
    for word in wordlist:
        if match_with_gaps(my_word,word):
            possible_matches = possible_matches + [word];

    if len(possible_matches) == 0:
        print("No matches found");
    else:
        print(' '.join(possible_matches));
    
    





    
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    secret_word = choose_word(wordlist);
    guesses_remaining = 6;
    warnings_remaining = 3;
    letters_guessed = [];

    word = [];
    for char in secret_word:
        if char not in word:
            word = word + [char];

    
    print("Welcome to the game Hangman!");
    print("I am thinking of a word that is",str(len(secret_word)),"letters long.");
    
    while guesses_remaining > 0:
        print("-------------");
        print("You have",str(guesses_remaining),"guesses left.");
        print("Available letters:",get_available_letters(letters_guessed));
        guess = str.lower(input("Please guess a letter: "));
        if guess not in string.ascii_lowercase:
            if guess == "*":
                print("Possible word matches are: ");
                show_possible_matches(get_guessed_word(secret_word,letters_guessed)); 
            elif warnings_remaining > 0:
                warnings_remaining -= 1;
                print("Oops! That is not a valid letter. You have", str(warnings_remaining),"warnings left:",get_guessed_word(secret_word,letters_guessed));
            elif warnings_remaining == 0:
                guesses_remaining -= 1;
                print("Oops! That is not a valid letter:",get_guessed_word(secret_word,letters_guessed));
        elif guess in string.ascii_lowercase:
            if guess not in letters_guessed:
                letters_guessed = letters_guessed + [guess];
                if guess in secret_word:
                    print("Good guess:",get_guessed_word(secret_word,letters_guessed));  
                else:
                    if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                        guesses_remaining -= 2;
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed));
                    else:
                        guesses_remaining -= 1;
                        print("Oops! That letter is not in my word:",get_guessed_word(secret_word,letters_guessed));
                        
                if is_word_guessed(secret_word,letters_guessed):
                    print("------------");
                    print("Congratulations, you won!");
                    break;
            elif guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1;
                    print("Oops! You've already guessed that letter. You now have",str(warnings_remaining),"warnings: ",get_guessed_word(secret_word,letters_guessed));
                elif warnings_remaining == 0:
                    guesses_remaining -= 1;
                    print("Oops! You've already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
            
                    
    if guesses_remaining < 1:
        print("------------")
        print("Sorry, you ran out of guesses. The word was", secret_word);
    else:
        print("Your total score for this game is: " + str(len(word)*guesses_remaining));







# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

