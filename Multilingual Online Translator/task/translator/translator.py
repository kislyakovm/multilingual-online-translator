import requests
from bs4 import BeautifulSoup


def words_parser(soup):
    words = soup.find_all('div', id="translations-content")

    new_list = []
    for word in words:
        new_list.append(word.text)

    new_list_2 = new_list[0].split()
    print(new_list_2)


def example_parser(soup):
    new_list = []
    examples = soup.find('section', id="examples-content").find_all('span', class_="text")

    for ex in examples:
        new_list.append(ex.text.strip())
    print(new_list)


def site_connection(url):
    user_agent = 'Mozilla/5.0'
    r = requests.get(url, headers={'User-Agent': user_agent})
    print(r.status_code, 'OK')

    # r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def welcome_print_and_input():
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
    print(url)

    print(f'You chose "{language}" as the language to translate "{user_word}" to.')

    return url


def main():

    url = welcome_print_and_input()
    soup = site_connection(url)

    print('Translations')
    words_parser(soup)
    example_parser(soup)


if __name__ == '__main__':
    main()
