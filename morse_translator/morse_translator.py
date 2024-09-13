morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    text = text.upper()
    morse_code = ' '.join(morse_code_dict.get(char, '') for char in text)
    return morse_code

def morse_to_text(morse):
    morse_words = morse.split(' / ')
    text = ''
    for word in morse_words:
        text += ''.join(inverse_morse_code_dict.get(code, '') for code in word.split())
        text += ' '
    return text.strip()

input_text = 'Hello EEMI'
morse_code = text_to_morse(input_text)
print(f"Code Morse de '{input_text}': {morse_code}")

translated_text = morse_to_text(morse_code)
print(f"Texte traduit depuis le code Morse: {translated_text}")
