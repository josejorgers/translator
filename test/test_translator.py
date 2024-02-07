from src.translator import translate

def test_translator():
    text = "Al mal tiempo buena cara"
    trans = translate(text, 'Spanish', 'English')
    print(trans)
    assert trans