from transformers import MarianMTModel, MarianTokenizer

model_name = 'Helsinki-NLP/opus-mt-en-roa'
tokenizer = MarianTokenizer.from_pretrained(model_name)
#print(tokenizer.supported_language_codes)
model = MarianMTModel.from_pretrained(model_name)

def trans(src_text):
  translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
  trans_text = str([tokenizer.decode(t, skip_special_tokens=True) for t in translated])
  return trans_text
