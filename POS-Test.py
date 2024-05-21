import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def detect_verbs_nouns(sentence):
    # Tokenize the input sentence into words
    words = word_tokenize(sentence)

    # Use NLTK's part-of-speech tagging to tag each word with its POS
    tagged_words = pos_tag(words)

    # Initialize lists to store verbs and nouns
    verbs = []
    nouns = []

    # Iterate through the tagged words to detect verbs and nouns
    for word, tag in tagged_words:
        if tag.startswith('VB'):  # Check if the word is a verb
            verbs.append(word)
        elif tag.startswith('NN'):  # Check if the word is a noun
            nouns.append(word)

    return verbs, nouns

# Main function to take input from the user
def main():
    sentence = input("Enter a sentence: ")
    verbs, nouns = detect_verbs_nouns(sentence)

    print("Verbs:", verbs)
    print("Nouns:", nouns)

if __name__ == "__main__":
    main()
