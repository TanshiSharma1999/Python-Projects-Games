import random


def hangman():
    """Play Hangman - Netflix Edition"""

    words = [
        "strangerthings", "moneyheist", "squidgame", "wednesday", "dark",
        "bridgerton", "lucifer", "you", "narcos", "thewitcher",
        "peakyblinders", "breakingbad", "bettercallsaul", "blackmirror",
        "thecrown", "ozark", "vikings", "elite", "sexeducation", "queensgambit"
    ]

    secret_word = random.choice(words)
    display_word = ["_"] * len(secret_word)

    max_attempts = 6
    attempts_left = max_attempts
    guessed_letters = set()   # using set for efficiency

    print("=" * 35)
    print("🎬 WELCOME TO HANGMAN: NETFLIX EDITION 🎬")
    print("=" * 35)
    print("Word:", " ".join(display_word))
    print(f"Attempts remaining: {attempts_left}")

    while attempts_left > 0 and "_" in display_word:
        guess = input("\nEnter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    display_word[index] = guess
        else:
            attempts_left -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts_left}")

        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))

    print("\n" + "-" * 35)
    if "_" not in display_word:
        print(f"🎉 CONGRATULATIONS! You guessed the word: {secret_word}")
    else:
        print(f"💀 GAME OVER! The word was: {secret_word}")
    print("-" * 35)


if __name__ == "__main__":
    hangman()
    