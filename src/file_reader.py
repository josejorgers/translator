import os

def text_splitter(text, n_words):
    paragraphs =  text.split('\n')
    counter = 0
    prev_idx = 0
    for i in range(1, len(paragraphs)):
        counter += len(paragraphs[i-1].split())
        if counter >= n_words or i == len(paragraphs) - 1:
            yield '\n' + '\n'.join(paragraphs[prev_idx:i])
            counter = 0
            prev_idx = i

def get_file_content(file):
    with open(file, 'r') as f:
        return f.read()