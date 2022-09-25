#regular expressions
import re

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales leo nisl, at mollis dui varius ac. Pellentesque metus magna, accumsan a venenatis ut, placerat nec nisi. Morbi tincidunt lobortis ipsum, eget scelerisque ex porta vel. Integer sit amet aliquet ex, non iaculis nisl. Phasellus varius est ultrices augue sodales, pharetra maximus metus ullamcorper. Nullam elit nisl, imperdiet at quam ac, convallis maximus massa. Praesent at urna mauris. Nulla facilisi. "
sentence = sentence.lower()
sentence = re.sub(r'[^\w\s]', '',sentence)
words_sentence = re.split(" ",sentence)
words_sentence = set(words_sentence)
word_dict = { }
def howMany():
    for word in words_sentence:
        word_dict[word] = len(re.findall(word,sentence))
        

howMany()
print(word_dict)
