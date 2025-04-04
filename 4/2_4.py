import re

def main():
    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Файл text.txt не найден.")
        return

    # Регулярное выражение для поиска email-адресов
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    # Регулярное выражение для поиска номеров телефонов в формате +7-XXX-XXX-XX-XX
    phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
    # Регулярное выражение для поиска слов, начинающихся с заглавной буквы (английские и русские буквы)
    capital_word_pattern = r'\b[А-ЯA-ZЁ][а-яa-zё]*\b'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    capital_words = re.findall(capital_word_pattern, text)


    with open('emails.txt', 'w', encoding='utf-8') as f_emails:
        f_emails.write("\n".join(emails))

    with open('phones.txt', 'w', encoding='utf-8') as f_phones:
        f_phones.write("\n".join(phones))

    with open('capital_words.txt', 'w', encoding='utf-8') as f_capital:
        f_capital.write("\n".join(capital_words))

    print("Результаты сохранены в файлы: emails.txt, phones.txt, capital_words.txt")

if __name__ == '__main__':
    main()