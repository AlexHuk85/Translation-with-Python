from translate import Translator

with open('new.txt', 'r') as my_file:

    text = my_file.read()

    translator = Translator(to_lang="vi")
    translation = translator.translate(text)

    print(translation)