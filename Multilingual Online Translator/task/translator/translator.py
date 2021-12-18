import requests, argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument('source_language')
parser.add_argument('target_language')
parser.add_argument('word')

args = parser.parse_args()

user_word = args.word
target_language = args.target_language
source_language = args.source_language
languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese',
             'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']


if target_language.capitalize() not in languages and target_language != 'all':
    print(f"Sorry, the program doesn't support {target_language}")
    exit()
elif source_language.capitalize() not in languages and source_language != 'all':
    print(f"Sorry, the program doesn't support {source_language}")
    exit()


def words_parser(soup):
    try:
        words = soup.find('div', id="translations-content").find_all('a')
    except AttributeError:
        print(f'Sorry, unable to find {user_word}')
        exit()

    new_list = []
    for word in words:
        new_list.append(word.text.strip())

    file.write(f'{target_language.capitalize()} Translations:\n')
    print(f'{target_language.capitalize()} Translations:')

    print(new_list[0])
    file.write(f'{new_list[0]}\n\n')

    print()


def example_parser(soup):
    examples_list = []
    examples = soup.find('section', id="examples-content").find_all('span', class_="text")

    print(f'{target_language.capitalize()} Example:')
    file.write(f'{target_language.capitalize()} Example:\n')

    for ex in examples:
        examples_list.append(ex.text.strip())

    print(examples_list[0])
    print(examples_list[1])

    file.write(f'{examples_list[0]}\n')
    file.write(f'{examples_list[1]}\n\n')


def site_connection(url):
    user_agent = 'Mozilla/5.0'
    try:
        r = requests.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')
        exit()

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def main():
    global file, target_language
    file = open(f'{user_word}.txt', 'w', encoding='utf=8')

    if target_language == 'all':
        for i in languages:
            if i.lower() == source_language:
                continue

            target_language = i
            url = f'https://context.reverso.net/translation/' \
                  f'{source_language.lower()}-{target_language.lower()}/{user_word}'

            soup = site_connection(url)
            print()

            words_parser(soup)
            example_parser(soup)
    else:
        url = f'https://context.reverso.net/translation/' \
              f'{source_language.lower()}-{target_language.lower()}/{user_word.lower()}'
        soup = site_connection(url)
        print()

        words_parser(soup)
        example_parser(soup)
    file.close()


if __name__ == '__main__':
    main()
