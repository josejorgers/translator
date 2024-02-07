import os
from file_reader import get_file_content, text_splitter
from translator import translate
from file_writer import write_text
from dotenv import load_dotenv
load_dotenv("../.env")

OUTPUT_DIR = os.environ.get("OUTPUT_DIR")
print("OUT DIR:", OUTPUT_DIR)
INPUT_DIR = os.environ.get("INPUT_DIR")
INPUT_LANG = os.environ.get("INPUT_LANG")
OUTPUT_LANG = os.environ.get("OUTPUT_LANG")
try:
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE"))
except:
    CHUNK_SIZE = 100

print(INPUT_DIR)
print(INPUT_LANG)
print(OUTPUT_LANG)
print(CHUNK_SIZE)


for file in os.listdir(INPUT_DIR):
    # Check if the file is a regular file (not a directory)
    if not os.path.isfile(os.path.join(INPUT_DIR, file)):
        continue
    path = os.path.join(INPUT_DIR, file)
    print(f'Processing file: {path}')
    content = get_file_content(path)
    print('CONTENT:', content)
    print('=========== ')
    out_path = os.path.join(OUTPUT_DIR, path.split(INPUT_DIR)[1][1:])
    print('CREATING:', out_path)
    open(out_path, 'w').close()
    for chunk in text_splitter(content, CHUNK_SIZE):
        print('CHUNK:', chunk)
        translation = translate(chunk, INPUT_LANG, OUTPUT_LANG)
        print('TRANSLATION:', translation)
        write_text(translation, out_path)
        print('Translation written!')
