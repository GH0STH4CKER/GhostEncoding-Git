from ghostencoding import encode_pipeline, decode_pipeline

def test_encoding():
    text = "Hello World!"
    enc = encode_pipeline(text)
    dec = decode_pipeline(enc)
    assert dec == text
