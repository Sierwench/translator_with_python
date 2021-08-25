from pathlib import Path
from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('test.txt', mode='r', encoding="UTF-8") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode='w', encoding='UTF-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print("File not exist")
    raise err
