from translate import Translator  # <-- translate 3.5.0 from pypi

translator = Translator(to_lang="ja")  # <--Can change to other laguages

with open('txt.txt', 'r') as my_file:
    text = my_file.read()

    # ---------------Translate part-----------------------#

    translation = translator.translate(text)

    # --------------Save translation into txt file------------#
    with open('txt_jp.txt', 'w') as other_file:
        other_file.write(translation)
