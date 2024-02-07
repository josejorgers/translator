from src.file_writer import write_text
import os

def test_write_text():
    filename = './output/test.txt'
    text = 'Hello'
    open(filename, 'w').close()
    write_text(text, filename)
    with open(filename, 'r') as f:
        assert f.read() == text
    os.remove(filename)    
