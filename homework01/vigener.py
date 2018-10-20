def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ''
    l=len(keyword)
    for i, ch in enumerate(plaintext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[i % l])
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            code = ord(ch) + shift
            if 'a' <= ch <= 'z' and code > ord('z'):
                code -= 26
            elif 'A' <= ch <= 'Z' and code > ord('Z'):
                code -= 26
            ciphertext += chr(code)
        else:
            chiphertext += ch
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ''
    l=len(keyword)
    for i, ch in enumerate(ciphertext):
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            shift = ord(keyword[i % l])
            shift -= ord('a') if 'a' <= ch <= 'z' else ord('A')
            code = ord(ch) - shift
            if 'a' <= ch <= 'z' and code < ord('a'):
                code += 26
            elif 'A' <= ch <= 'Z' and code < ord('A'):
                code += 26
            plaintext += chr(code)
        else:
            plaintext += ch
    return plaintext
