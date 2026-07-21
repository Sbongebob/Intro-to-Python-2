# Loza - Church Language Helper App
# Converts Amharic, Tigrinya, and Ge'ez letters into English letters

import tkinter as tk
from tkinter import ttk


# Ethiopic letters (common Amharic/Tigrinya/Ge'ez sounds)
geez_to_english = {

    # ሀ
    "ሀ":"ha", "ሁ":"hu", "ሂ":"hi", "ሃ":"ha", "ሄ":"he", "ህ":"h", "ሆ":"ho",

    # ለ
    "ለ":"le", "ሉ":"lu", "ሊ":"li", "ላ":"la", "ሌ":"le", "ል":"l", "ሎ":"lo",

    # መ
    "መ":"me", "ሙ":"mu", "ሚ":"mi", "ማ":"ma", "ሜ":"me", "ም":"m", "ሞ":"mo",

    # ሰ
    "ሰ":"se", "ሱ":"su", "ሲ":"si", "ሳ":"sa", "ሴ":"se", "ስ":"s", "ሶ":"so",

    # ሸ
    "ሸ":"she", "ሹ":"shu", "ሺ":"shi", "ሻ":"sha", "ሼ":"she", "ሽ":"sh", "ሾ":"sho",

    # ረ
    "ረ":"re", "ሩ":"ru", "ሪ":"ri", "ራ":"ra", "ሬ":"re", "ር":"r", "ሮ":"ro",

    # በ
    "በ":"be", "ቡ":"bu", "ቢ":"bi", "ባ":"ba", "ቤ":"be", "ብ":"b", "ቦ":"bo",

    # ተ
    "ተ":"te", "ቱ":"tu", "ቲ":"ti", "ታ":"ta", "ቴ":"te", "ት":"t", "ቶ":"to",

    # ቀ
    "ቀ":"qe", "ቁ":"qu", "ቂ":"qi", "ቃ":"qa", "ቄ":"qe", "ቅ":"q", "ቆ":"qo",

    # ነ
    "ነ":"ne", "ኑ":"nu", "ኒ":"ni", "ና":"na", "ኔ":"ne", "ን":"n", "ኖ":"no",

    # አ
    "አ":"a", "ኡ":"u", "ኢ":"i", "ኣ":"a", "ኤ":"e", "እ":"e", "ኦ":"o",

    # ከ
    "ከ":"ke", "ኩ":"ku", "ኪ":"ki", "ካ":"ka", "ኬ":"ke", "ክ":"k", "ኮ":"ko",

    # ወ
    "ወ":"we", "ዉ":"wu", "ዊ":"wi", "ዋ":"wa", "ዌ":"we", "ው":"w", "ዎ":"wo",

    # ዘ
    "ዘ":"ze", "ዙ":"zu", "ዚ":"zi", "ዛ":"za", "ዜ":"ze", "ዝ":"z", "ዞ":"zo",

    # የ
    "የ":"ye", "ዩ":"yu", "ዪ":"yi", "ያ":"ya", "ዬ":"ye", "ይ":"y", "ዮ":"yo",

    # ገ
    "ገ":"ge", "ጉ":"gu", "ጊ":"gi", "ጋ":"ga", "ጌ":"ge", "ግ":"g", "ጎ":"go",

    # ጠ
    "ጠ":"te", "ጡ":"tu", "ጢ":"ti", "ጣ":"ta", "ጤ":"te", "ጥ":"t", "ጦ":"to",

    # ፈ
    "ፈ":"fe", "ፉ":"fu", "ፊ":"fi", "ፋ":"fa", "ፌ":"fe", "ፍ":"f", "ፎ":"fo",

    # ፐ
    "ፐ":"pe", "ፑ":"pu", "ፒ":"pi", "ፓ":"pa", "ፔ":"pe", "ፕ":"p", "ፖ":"po"


}

def convert_word():
    text = input_box.get("1.0", tk.END).strip()

    converted = ""

    for letter in text:
        if letter in geez_to_english:
            converted += geez_to_english[letter]
        else:
            converted += letter

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, converted)



# Create App Window
window = tk.Tk()
window.title("Loza")
window.geometry("650x550")


# App Title
title = tk.Label(
    window,
    text="Loza",
    font=("Arial", 28, "bold")
)
title.pack(pady=5)


subtitle = tk.Label(
    window,
    text="Amharic • Tigrinya • Ge'ez → English Letters",
    font=("Arial", 12)
)
subtitle.pack()


# Language Choice
language_label = tk.Label(
    window,
    text="Choose Language:"
)
language_label.pack(pady=5)


language = ttk.Combobox(
    window,
    values=["Amharic", "Tigrinya", "Ge'ez"]
)

language.current(0)
language.pack()


# Input
input_label = tk.Label(
    window,
    text="Type your word or sentence:"
)

input_label.pack()

input_box = tk.Text(
    window,
    height=6,
    width=55
)

input_box.pack(pady=10)


# Button
convert_button = tk.Button(
    window,
    text="Convert to English Letters",
    command=convert_word,
    font=("Arial", 12)
)

convert_button.pack(pady=5)


# Output
output_label = tk.Label(
    window,
    text="English Letters:"
)

output_label.pack()

output_box = tk.Text(
    window,
    height=6,
    width=55
)

output_box.pack(pady=10)


# Start App
window.mainloop()