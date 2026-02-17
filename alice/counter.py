import argparse

def read_file(file):
    """read in the alice text"""
    f = open(file, "r")
    read_f = f.read()
    f.close()
    return read_f


def split_text_into_words(text):
    """break it into words"""
    t = text.split()
    return t

def get_capital_words(words):
    """make a list of capitalized words"""
    counter = {}
    capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in words:
        if word[0] in capital:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter

def print_word_counts(counts):
    """print the capital words out"""
    print(counts)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count capitalized words in a file")
    parser.add_argument("filename", help="Path to the text file")
    parser.add_argument("--top", type=int, help="Only show the top N words")
    args = parser.parse_args()

    text = read_file(args.filename)
    words = split_text_into_words(text)
    counts = get_capital_words(words)

    if args.top:
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:args.top])

    print_word_counts(counts)