class WordGame:
    def __init__(self, filepath):
        self.filepath = filepath

    def __read_words(self):
        with open(self.filepath, 'r') as f:
            lines = f.readlines()
        words = [line for line in lines[1:]]
        return words

    def __cross_letter(self, word, index):
        return word[:index] + word[index+1:]

    def result(self):
        words = self.__read_words()
        words.sort(key=len)

        len_map = {}
        max_chain_len = 0

        for word in words:
            current_max = 1

            if len(word) > 1:
                for i in range(len(word)):
                    parent = self.__cross_letter(word, i)

                    if parent in len_map:
                        current_max = max(current_max, 1 + len_map[parent])

            len_map[word] = current_max
            max_chain_len = max(max_chain_len, current_max)

        return max_chain_len
