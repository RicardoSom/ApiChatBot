import datetime
from translate import Translator


t = datetime.datetime.now()
f = t.strftime("%A")

translator = Translator(to_lang="spanish")
translation = translator.translate(f)


print (translation)