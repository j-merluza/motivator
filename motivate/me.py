import json
import random


class MotivateMe:
    """
    Selects a random motivational quote.

    Attributes:
        quote: What the fire quote was said.
        author: Who spittin said fire quote.
        category: Category of said fire quote.
    """
    def __init__(self):
        with open(".\quotes.json", "r") as json_file:
            self.data = json.load(json_file)
        self.quote = random.choice(list(self.data))
        self.author = self.data.get(self.quote)[0]
        self.category = self.data.get(self.quote)[1].replace("\n", "")
