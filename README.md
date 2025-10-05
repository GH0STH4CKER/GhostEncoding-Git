# GHosTEncoding

**Progressive ROT encoding** (default start=21) with optional **zlib compression**.  
Generates **UUID-like encoded strings** for obfuscation and secure text handling.

Use online encoder/decoder on : <a href="[https://www.w3schools.com](https://ghostncoding.lovable.app)" target="_blank">https://ghostncoding.lovable.app</a>

---

## Installation

Install GHosTEncoding via pip:

```bash
pip install ghostencoding
```

---

## Quick Start

Use `encode_pipeline` and `decode_pipeline` to quickly encode and decode text:

```python
from ghostencoding import encode_pipeline, decode_pipeline

# Encode text
encoded = encode_pipeline("hello world")
print("Encoded:", encoded)

# Decode back
decoded = decode_pipeline(encoded)
print("Decoded:", decoded)
```

**Expected output:**

```
Encoded: <uuid-like string>
Decoded: 789cabad-5651-d5b4-32d6-31d056010011-d80283
```

---

## How It Works

GHosTEncoding applies a **progressive ROT** cipher to your text:

- Each character is shifted by a **starting value** (`start`) that increments for each subsequent character.  
- Optionally, text can be **compressed with zlib** before encoding, reducing size and increasing obfuscation.  
- The output looks like a **UUID-style string**, making it harder to interpret at a glance.

---

## Advanced Options

Both `encode_pipeline` and `decode_pipeline` support optional parameters to customize encoding:

| Option          | Default      | Description |
|-----------------|-------------|-------------|
| `start`         | 21          | Starting shift for progressive ROT |
| `alphabet_mode` | 'printable' | Use all printable ASCII (`'printable'`) or only letters (`'letters'`) |
| `compress`      | True        | Apply zlib compression (`True`) or leave uncompressed (`False`) |

---

### Example with Custom Options

```python
encoded = encode_pipeline(
    "Secret message!",
    start=10,
    alphabet_mode="letters",
    compress=False
)

decoded = decode_pipeline(
    encoded,
    start=10,
    alphabet_mode="letters",
    compress=False
)

print(decoded)  # Secret message!
```

This example demonstrates **controlling the shift**, restricting the alphabet, and disabling compression.

---

## Notes & Tips

- **Default behavior** (`start=21`, `alphabet_mode='printable'`, `compress=True`) works for most use cases.  
- Encoded strings are **UUID-like**, so they are suitable for obfuscation or generating unique keys.  
- Always use `decode_pipeline` with the **same parameters** you used for encoding to retrieve the original text.  

---

## License

MIT License
