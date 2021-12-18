import requests
from bs4 import BeautifulSoup

language_1 = 0
language_2 = 0
user_word = ''
target_language = ''
second_language = ''
languages = {}
new_list_2 = []


def words_parser(soup):
    global new_list_2
    words = soup.find('div', id="translations-content").find_all('a')

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
    r = requests.get(url, headers={'User-Agent': user_agent})

    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def choose_language():
    global target_language, second_language, languages
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


def any_language():
    choose_language()

    url = f'https://context.reverso.net/translation/{second_language.lower()}-{target_language.lower()}/{user_word}'
    return url


def welcome_print_and_input():
    global target_language, second_language, user_word, language_1, language_2
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
    print('Type the number of a language you want to translate to or "0" to translate to all languages:')
    language_2 = int(input())

    print('Type the word you want to translate:')
    user_word = input()

    if language_2 == 0:
        return ''
    else:
        url = any_language()
        return url


def main():
    global file, language_2

    url = welcome_print_and_input()
    file = open(f'{user_word}.txt', 'w', encoding='utf=8')

    if language_2 == 0:
        for i in range(1, 14):
            if i == language_1:
                continue
            language_2 = i
            url = any_language()
            soup = site_connection(url)

            print()

            words_parser(soup)
            example_parser(soup)
    else:
        soup = site_connection(url)

        print()

        words_parser(soup)
        example_parser(soup)
    file.close()


if __name__ == '__main__':
    main()
