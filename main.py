class Transcribe:
    def __init__(self):
        self.nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        
    def transcribe_text(self, text):
        words = text.split(" ")
        res = []
        
        start = None
        curr = []
        i = 0
        while i < len(words):
            word = words[i]
            if word.lower() != "number":
                # add word to current list
                self.add_word(curr, word, start)
                i += 1
            else:
                i = i + 1
                # find starting list number
                if not start:
                    res.append(" ".join(curr))
                    curr = []
                    start = self.nums[words[i]]
                # next item in list
                elif words[i].lower() == "next":
                    res.append(" ".join(curr))
                    curr = []
                    start += 1
                # number is just part of the text in the list
                else:
                    self.add_word(curr, words[i], start)
                i = i + 1
        # add last item in list to result
        res.append(" ".join(curr))
        
        return "\n".join(res)

    # helper function for adding words
    def add_word(self, curr, word, start):
        if not curr:
            #capitalize first word
            word = word.capitalize()
            if start:
                curr.append(str(start) + ".")
        curr.append(word)

if __name__ == '__main__':
    text = input("Enter text to transcribe: ")
    
    if text == "":
        text = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn't improved for last 4 weeks Number next patient is taking drug number five several times a week"

    t = Transcribe()
    print(t.transcribe_text(text))

