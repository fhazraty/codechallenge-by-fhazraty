def smart_caesar_cipher(text, shift_word):
    # محاسبه مجموع موقعیت الفبایی حروف کلمه‌ی shift_word
    shift = sum(ord(char) - ord('a') + 1 for char in shift_word)
    #generator expression
    
    shift = shift % 26  # چون فقط 26 حرف داریم

    result = ""

    for char in text:
        # محاسبه کاراکتر جدید با در نظر گرفتن چرخش در الفبا
        new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        result += new_char

    return result
print(smart_caesar_cipher("hello", "dog"))   # خروجی: hello
print(smart_caesar_cipher("abc", "abc"))     # خروجی: ghi
print(smart_caesar_cipher("xyz", "abc"))     # خروجی: def




