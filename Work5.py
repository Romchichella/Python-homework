# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Напишите набвпишите программу, проабв удаляющую из этого абв текста все словабв слова, содерабващие содержащие "а.б.в"'

def del_words(text):
    text = list(filter(lambda a: 'абв' not in a, text.split()))
    return " ".join(text)

text = del_words(text)
print(text)