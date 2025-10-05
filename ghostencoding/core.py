import binascii
import zlib
from typing import List

START_SHIFT_DEFAULT = 21
UUID_BLOCKS = (8,4,4,4,12)
PRINTABLE = [chr(i) for i in range(32, 127)]
PRINTABLE_MAP = {ch: i for i, ch in enumerate(PRINTABLE)}
PRINTABLE_SIZE = len(PRINTABLE)

def progressive_rot(text: str, start: int = START_SHIFT_DEFAULT, alphabet_mode: str = 'printable', encode: bool = True) -> str:
    out_chars = []
    for i, ch in enumerate(text):
        shift = (start + i)
        if alphabet_mode == 'letters' and ch.isalpha():
            if ch.islower():
                base = ord('a'); size = 26
                s = shift % size
                delta = s if encode else (-s)
                out_chars.append(chr((ord(ch) - base + delta) % size + base))
            elif ch.isupper():
                base = ord('A'); size = 26
                s = shift % size
                delta = s if encode else (-s)
                out_chars.append(chr((ord(ch) - base + delta) % size + base))
            else:
                out_chars.append(ch)
        elif alphabet_mode == 'printable':
            if ch in PRINTABLE_MAP:
                idx = PRINTABLE_MAP[ch]
                s = shift % PRINTABLE_SIZE
                nidx = (idx + s) % PRINTABLE_SIZE if encode else (idx - s) % PRINTABLE_SIZE
                out_chars.append(PRINTABLE[nidx])
            else:
                out_chars.append(ch)
        else:
            out_chars.append(ch)
    return ''.join(out_chars)

def bytes_to_uuid_like(data: bytes) -> str:
    hx = binascii.hexlify(data).decode()
    parts: List[str] = []
    i = 0
    while i < len(hx):
        for size in UUID_BLOCKS:
            if i >= len(hx):
                break
            parts.append(hx[i:i+size])
            i += size
    return '-'.join(parts)

def uuid_like_to_bytes(s: str) -> bytes:
    clean = s.replace('-', '')
    return binascii.unhexlify(clean)

def encode_pipeline(text: str, start: int = START_SHIFT_DEFAULT, alphabet_mode: str = 'printable', compress: bool = True) -> str:
    rotated = progressive_rot(text, start=start, alphabet_mode=alphabet_mode, encode=True)
    b = rotated.encode('utf-8')
    if compress:
        b = zlib.compress(b)
    return bytes_to_uuid_like(b)

def decode_pipeline(uuid_like: str, start: int = START_SHIFT_DEFAULT, alphabet_mode: str = 'printable', compress: bool = True) -> str:
    b = uuid_like_to_bytes(uuid_like)
    if compress:
        b = zlib.decompress(b)
    rotated = b.decode('utf-8')
    return progressive_rot(rotated, start=start, alphabet_mode=alphabet_mode, encode=False)
