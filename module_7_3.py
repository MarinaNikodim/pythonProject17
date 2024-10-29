
import string


class WordsFinder:
    file_names = []

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words_dict = {}
        for file_name in self.file_names:
            with (open(file_name, 'r', encoding='utf-8') as file):
                words = []
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words.extend(line.split())
                all_words_dict[file_name] = words
        return all_words_dict

    def find(self, word):
        word_position_dict = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                word_position_dict[key] = value.index(word.lower()) + 1
        return word_position_dict


    def count(self, word):
        count_words = {}
        for key, value in self.get_all_words().items():
            words = value.count(word.lower())
            count_words[key] = words
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
finder1 = WordsFinder('Goods.txt')
print(finder1.get_all_words())
print(finder1.count('POTATO'))
print(finder1.find('vegetables'))


