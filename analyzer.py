import nltk
#from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        

        # TODO
        
        self.tokenizer = nltk.tokenize.TweetTokenizer()
        
        self.positives = set()
        file = open(positives, "r")
        for line in file:
            if line.startswith(";") != True:
                line.strip()
                self.positives.add(line.rstrip("\n"))
        file.close()
        
        self.negatives = set()
        file = open(negatives, "r")
        for line in file:
            if line.startswith(";") != True:
                line.strip()
                self.negatives.add(line.rstrip("\n"))
        file.close()
        
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # TODO
        tokens = self.tokenizer.tokenize(text)
        score = 0
        for word in tokens:
            if word.lower() in self.positives:
               score = score + 1
            elif word.lower() in self.negatives:
                score = score - 1
            else:
                score = score
        
        return score
