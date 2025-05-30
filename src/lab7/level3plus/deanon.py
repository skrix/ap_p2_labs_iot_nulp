from src.lab7.level3plus.aho_trie import AhoTrie
import yaml

class Deanon:
    def __init__(self):
        self.aho_trie = AhoTrie()
        self.users_texts = {}
        self.results = {}

    def analyze(self, filepath, keywords):
        patterns = self.normalize_keywords(keywords)
        self.populate_trie(patterns)
        self.users_texts = self.read_users_texts(filepath)
        return self.calculate_users_match_percentage(patterns)

    def calculate_users_match_percentage(self, patterns):
        result = {}
        users_matches_counts = self.build_users_matches_counts(patterns)
        users_texts_counts = self.build_users_texts_counts()
        for user in self.users_texts.keys():
            if user in users_texts_counts and user in users_matches_counts:
                result[user] = self.calculate_percentage(users_texts_counts[user], users_matches_counts[user])
            else:
                result[user] = 0.0
        return result

    def build_users_matches_counts(self, patterns):
        result = {}
        users_keywords_counts = self.count_user_keywords(patterns)
        for user, keywords_counts in users_keywords_counts.items():
            result[user] = sum(keywords_counts.values())
        return result

    def build_users_texts_counts(self):
        result = {}
        for user, texts in self.users_texts.items():
            if texts:
                result[user] = len(texts)
            else:
                result[user] = 0
        return result

    def calculate_percentage(self, total_texts_count, total_keyword_matches):
        if total_texts_count:
            return round((total_keyword_matches * 1.0 / total_texts_count * 1.0) * 100, 2)
        else:
            return 0.0

    def count_user_keywords(self, patterns):
        results = {}
        for username, texts_list in self.users_texts.items():
            user_keyword_counts  = { keyword: 0 for keyword in patterns }

            if not texts_list:
                results[username] = user_keyword_counts
                continue

            for text_content in texts_list:
                if not isinstance(text_content, str):
                    continue

                normalized_text = text_content.lower()
                for _start_index, _end_index, found_keyword in self.aho_trie.search(normalized_text):
                    if found_keyword in user_keyword_counts:
                        user_keyword_counts[found_keyword] += 1
                results[username] = user_keyword_counts
        return results


    def normalize_keywords(self, keywords):
        return sorted(list(set(keywords)))

    def read_users_texts(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()
            data = yaml.safe_load(content)

        if data is None:
            return {}
        else:
            return data

    def populate_trie(self, keywords):
        for keyword in keywords:
            self.aho_trie.insert(keyword)
        self.aho_trie.build()
