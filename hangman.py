import random

print("Welcome to Python")

words = ["hacker","bug","red","blue"]


s_word = random.choice(words)

dis_word = []

for letter in s_word:
    dis_word+= "_"
print(dis_word)

num = 0
game_over=False

while not game_over:
    g_letter = input("Guess a letter: ").lower()
    print(g_letter)

    for position in range(len(s_word)):
        letter = s_word[position]

        if letter == g_letter:
            dis_word[position] = letter

    if g_letter not in s_word :
        num+=1
        left_guess = 5 - num
        print(f"You have {left_guess} guesses left")

        if num >= 5:
            game_over = True
            print("You are looser!!!")


    print(dis_word)

    if "_" not in dis_word:
        print("You are Win")
        game_over=True


