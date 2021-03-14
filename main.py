#import libraries and files
import functions
import detect_language

src_text = "Hi, How are you?"
src_lang = detect_language.detect_lang(src_text)
print(src_lang)
trans_text = str(functions.trans(src_text))
if src_lang=="en":
    print(trans_text)