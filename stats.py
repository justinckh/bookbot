def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        # print(file_contents)
    return file_contents

def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
    num_words = len(file_contents.split())

    return num_words

def char_counts(contents):
    lower_contents = contents.lower()
    dict = {}
    for char in lower_contents:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_counts(counts):
    list = []
    for i in counts:
        list.append({"char": i, "num": counts[i]})
    list.sort(reverse=True, key=sort_on)
    return list

