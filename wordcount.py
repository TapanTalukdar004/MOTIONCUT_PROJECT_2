def count_words(text):
    words = text.split()
    return len(words)
def main():
    user_input = input("Please enter a sentence or paragraph: ").strip()
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    word_count = count_words(user_input)
    print(f"The number of words in the given text is: {word_count}")

if __name__ == "__main__":
    main()
