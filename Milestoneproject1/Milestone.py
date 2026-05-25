player1_name = ""
player2_name = ""
words_list = []
guessed_word = ""
word_position = -1
game_result = ""

def ChoosePlayers():
    global player1_name, player2_name
    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    print(f"\n{player1_name} is Player 1 (creates words)")
    print(f"{player2_name} is Player 2 (guesses words)\n")

def CreateListWords():
    global words_list
    words_list = []
    print(f"{player1_name}, enter 10 words (only alphabetic characters, no digits/special chars):")
    
    while len(words_list) < 10:
        word = input(f"Enter word {len(words_list) + 1}: ").strip()
        
        if word.isalpha():
            words_list.append(word.lower())
            print("Word accepted")
        else:
            print("Invalid! Use only alphabetic characters. Try again.")
    
    print(f"\n{player1_name} created the list!")
    print(f"Words list: {words_list}\n")

def PredictWord():
    global guessed_word, word_position, game_result
    
    word_found = False
    word_chances = 3
    
    print(f"{player2_name}, you have {word_chances} chances to guess a word from the list.\n")
    
    while word_chances > 0:
        guessed_word = input(f"Guess a word (Chances left: {word_chances}): ").strip().lower()
        
        if guessed_word in words_list:
            word_found = True
            print(f"Correct! '{guessed_word}' is in the list!\n")
            break
        else:
            word_chances -= 1
            if word_chances > 0:
                print(f"Wrong! Try again. (Chances left: {word_chances})\n")
            else:
                print("Out of chances for word guessing!\n")
                game_result = "LOST"
                return
    
    if word_found:
        correct_position = words_list.index(guessed_word) + 1
        position_chances = 2
        
        print(f"{player2_name}, now guess the position of '{guessed_word}' in the list.")
        print(f"Position should be between 1 and {len(words_list)}\n")
        
        while position_chances > 0:
            try:
                word_position = int(input(f"Enter position (Chances left: {position_chances}): "))
                
                if word_position == correct_position:
                    print(f"Correct! '{guessed_word}' is at position {correct_position}!\n")
                    game_result = "WON"
                    break
                else:
                    position_chances -= 1
                    if position_chances > 0:
                        print(f"Wrong position! Try again. (Chances left: {position_chances})\n")
                    else:
                        print(f"Out of chances! Correct position was {correct_position}\n")
                        game_result = "LOST"
            except ValueError:
                print("Invalid input! Please enter a number.\n")
                position_chances -= 1

def ResultDeclaration():
    print("=" * 50)
    if game_result == "WON":
        print(f"CONGRATULATIONS {player2_name.upper()}!")
        print(f"You guessed '{guessed_word}' at position {word_position}!")
        print("GAME WON!")
    else:
        print(f"{player2_name}, YOU LOST!")
        print("The correct words and positions were:")
        for idx, word in enumerate(words_list, 1):
            print(f"Position {idx}: {word}")
    print("=" * 50 + "\n")

def PlayGame():
    while True:
        ChoosePlayers()
        CreateListWords()
        PredictWord()
        ResultDeclaration()
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            print("\nThank you for playing!")
            break
        print("\n" + "=" * 50 + "\n")

print("=" * 50)
print("WELCOME TO WORD GUESSING GAME")
print("=" * 50 + "\n")
PlayGame()
