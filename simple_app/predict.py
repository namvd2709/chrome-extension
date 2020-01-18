import gensim
import sys


def summarize(text):
    return gensim.summarization.summarize(text)


if __name__ == "__main__":
    text = sys.argv[1]
    word_count = sys.argv[2]
    result = summarize(text)
    # print(result[0], result[1])
