import json

class WordClassification:
    def __init__(self):
        with open('words.json', encoding='utf-8') as f:
            self.data = json.load(f)

    def classificate(self, word:str):
        for type in self.data:
            for element in self.data[type]:
                if word.lower() == element:
                    return type
        return False

    def classificate_sentence(self, sentence:str):
        s = sentence.strip()

        final = []
        for word in s.split(' '):
            final.append((word, self.classificate(word)))
        return final

    def get(self, sentence:str, type:str = None, types:list = None, max_results:int = 1):
        s = sentence.strip()

        if type:
            if max_results == 1:
                for word in s.split(' '):
                    r = self.classificate(word)
                    if r and r == type:
                        return word
            else:
                final = []
                for word in s.split(' '):
                    r = self.classificate(word)
                    if r and r == type:
                        final.append((word, r))

                    if len(final) == max_results:
                        break
                return final
        elif types:
            final = []
            if max_results == 1:
                for type in types:
                    curr = []
                    for word in s.split(' '):
                        r = self.classificate(word)
                        if r and r == type:
                            curr.append((word, r))

                        if len(curr) == max_results:
                            break

                    final = final + curr
            else:
                for type in types:
                    for word in s.split(' '):
                        r = self.classificate(word)
                        if r and r == type:
                            final.append((word, r))
                            break

            return final

cl = Word_Classification()

text = 'Ich sbring mich nach Willich oder Berlin'

print(cl.classificate_sentence(text))

print(cl.get(text, type = 'stadt', max_results=2))