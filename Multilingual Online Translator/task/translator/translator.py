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


def choose_language(language_1, language_2):
    global target_language, second_language
    languages = {1: 'Arabic',
                 2: 'German',
                 3: 'English',
                 4: 'Spanish',
                 5: 'French',
                 6: 'Hebrew',
                 7: 'Japanese',
                 8: 'Dutch',
                 9: 'Polish',
                 10: 'Portuguese',
                 11: 'Romanian',
                 12: 'Russian',
                 13: 'Turkish'}

    second_language = languages[language_1]
    target_language = languages[language_2]


def welcome_print_and_input():
    global target_language, second_language
    print("""Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language: """)

    language_1 = int(input())
    print('Type the number of language you want to translate to: ')
    language_2 = int(input())

    choose_language(language_1, language_2)

    print('Type the word you want to translate:')
    user_word = input()

    url = f'https://context.reverso.net/translation/{second_language.lower()}-{target_language.lower()}/{user_word}'
    return url


def main():
    url = welcome_print_and_input()
    soup = site_connection(url)

    print()

    words_parser(soup)
    example_parser(soup)


if __name__ == '__main__':
    main()
