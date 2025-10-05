# GHosTEncoding

Progressive ROT encoding (default start=21) with optional zlib compression.  
Generates UUID-like encoded strings for obfuscation.

## Installation

```bash
pip install ghostencoding
```

## Quick example

```python
from ghostencoding import encode_pipeline, decode_pipeline

# Encode text
encoded = encode_pipeline("hello world")
print("Encoded:", encoded)

# Decode back
decoded = decode_pipeline(encoded)
print("Decoded:", decoded)
```

## Advanced options

- `start` — starting shift for progressive ROT (default `21`)  
- `alphabet_mode` — `'printable'` (all printable ASCII) or `'letters'` (A-Z, a-z)  
- `compress` — `True` to use zlib compression (default), `False` to disable  

### Example with options

```python
encoded = encode_pipeline("Secret message!", start=10, alphabet_mode="letters", compress=False)
decoded = decode_pipeline(encoded, start=10, alphabet_mode="letters", compress=False)
print(decoded)  # Secret message!
```

## Command-line

Run the package like a script (once installed or from the repo):

```bash
python -m ghostencoding -e "some text to encode"
python -m ghostencoding -d "<uuid-like-string>"
```

## License

MIT License
