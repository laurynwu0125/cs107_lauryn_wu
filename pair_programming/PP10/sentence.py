class Sentence: # An iterable
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % (self.text)


if __name__ == "__main__":
    sent = "This is a test sentence."
    s = Sentence(sent)
    #print(list(s.__iter__()))
    for w in s:
        print(w)
