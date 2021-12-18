import requests
from bs4 import BeautifulSoup

target_language = ''
second_language = ''


def words_parser(soup):
    words = soup.find_all('div', id="translations-content")

    new_list = []
    for word in words:
        new_list.append(word.text)

    print(f'{target_language.capitalize()} Translations:')

    new_list_2 = new_list[0].split()
    for i in range(5):
        print(new_list_2[i])
    print()


def example_parser(soup):
    new_list = []
    examples = soup.find('section', id="examples-content").find_all('span', class_="text")

    print(f'{target_language.capitalize()} Examples:')

    for ex in examples:
        new_list.append(ex.text.strip())

    for i in range(0, 10, 2):
        print(new_list[i])
        print(new_list[i + 1])
        print()


def site_connection(url):
    user_agent = 'Mozilla/5.0'
    r = requests.get(url, headers={'User-Agent': user_agent})
    print(r.status_code, 'OK')

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def welcome_print_and_input():
    global target_language, second_language
    print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English '
          'into French:')

    language = input()

    if language == 'en':
        second_language = 'french'
        target_language = 'english'
    else:
        second_language = 'english'
        target_language = 'french'

    print('Type the word you want to translate:')
    user_word = input()

    url = f'https://context.reverso.net/translation/{second_language}-{target_language}/{user_word}'

    print(f'You chose "{language}" as the language to translate "{user_word}" to.')

    return url


def main():
    url = welcome_print_and_input()
    soup = site_connection(url)

    print()

    words_parser(soup)
    example_parser(soup)


if __name__ == '__main__':
    main()
