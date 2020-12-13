import json
import hashlib
import os


class Iter:
    def __init__(self, file):
        self.data = iter(json.load(file))

    def __iter__(self):
        return self.data


def get_wiki_links(new_file):
    with open(new_file, 'w', encoding='utf-8') as n_file:
        with open('countries.json', 'r', encoding='utf-8') as file:
            for country in Iter(file):
                country_name = country['name']['common']
                country_link = country_name.replace(' ', '_')
                n_file.write(f'{country_name} – 'f'https://en.wikipedia.org/wiki/{country_link}''\n')


def generator(file_path):
    file_name = os.path.basename(file_path)
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in iter(file):
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


def get_wiki_links_2(file_path):
    for line in generator(file_path):
        print(line)


if __name__ == '__main__':
    get_wiki_links('countries.txt')
    get_wiki_links_2('C:\\Users\\Босс\\PycharmProjects\\IteratorsGenerators\\countries.txt')

