# TODO  Напишите функцию count_letters
def count_letters(text):
    alphabet = {}
    text = text.lower()
    for symbol in range(len(text)):
        if text[symbol].isalpha():
            if alphabet.get(text[symbol]) is None:
                alphabet[text[symbol]] = 1
            else:
                alphabet[text[symbol]] += 1
    return alphabet


# TODO Напишите функцию calculate_frequency

def calculate_frequency(alphabet):
    letters_number = sum(alphabet.values())
    frequency = {}

    for values in alphabet:
        frequency[values] = alphabet.get(values) / letters_number
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
frequency_dict = calculate_frequency(count_letters(main_str))
for value in frequency_dict:
    print(f"{value}: {frequency_dict.get(value):.2f}")
