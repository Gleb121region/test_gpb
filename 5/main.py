def read_words_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words


def find_same_letters_sequence(entered_word, word):
    if entered_word == word:
        return ""

    max_valid_sequence = ""
    for i in range(len(word)):
        if entered_word.endswith(word[:i + 1]):
            max_valid_sequence = word[:i + 1]

    return word[len(max_valid_sequence):] if max_valid_sequence else ""


def main():
    file_path = "words.txt"

    words = read_words_from_file(file_path)
    print("Слова из файла:", words)

    entered_word = input("Введите первое слово: ").strip()
    if entered_word not in words:
        print("Введенное слово не найдено в списке слов из файла.")
        return

    result = []
    for word in words:
        same_letters_sequence = find_same_letters_sequence(entered_word, word)
        if same_letters_sequence:
            result.append(entered_word + same_letters_sequence)

    print("Программа выводит:")
    if result:
        for res in result:
            print(res)
    else:
        print("Совпадений не найдено.")


if __name__ == "__main__":
    main()
