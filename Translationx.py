#!/usr/bin/env python
# coding: utf-8

# In[14]:


class PhoneTranslator():
    def __init__():
        pass
    def translate1():
        import translate
        from translate import Translator
        text = input('Text:')
        language =input('What language would you like to translate into?: ')
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        print(translation)

    def translate2():
        import translate
        from translate import Translator
        text = input('Text:')
        language_start = input('What language is this?: ')
        language_end = input('What language would you like to translate into?: ')
        translator = Translator(from_lang = language_start, to_lang = language_end )
        translation = translator.translate(text)
        print(translation)

