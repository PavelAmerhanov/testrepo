def title_text(text):
    list_text = []
    for i in range(len(text)):
        list_text.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(list_text)


print(title_text(input('Введите текст : ').split()))
