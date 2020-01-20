from translate import Translator #<-- translate 3.5.0 from pypi

with open('new.txt', 'r') as my_file:

    text = my_file.read()
    
    #---------------Translate part-----------------------#
    translator = Translator(to_lang="vi") #<--Can change to other laguages
    translation = translator.translate(text)

    print(translation)
