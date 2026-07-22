
#python
import tkinter as tk
from tkinter import ttk

# =====================================
# Loza Dictionary
# Amharic • Tigrinya • Ge'ez
# =====================================

geez_to_english = {

    # ሀ
    "ሀ":"ha", "ሁ":"hu", "ሂ":"hi", "ሃ":"ha", "ሄ":"he", "ህ":"h", "ሆ":"ho",

    # ሐ
    "ሐ":"ha", "ሑ":"hu", "ሒ":"hi", "ሓ":"ha", "ሔ":"he", "ሕ":"h", "ሖ":"ho",

    # ሠ
    "ሠ":"se", "ሡ":"su", "ሢ":"si", "ሣ":"sa", "ሤ":"se", "ሥ":"s", "ሦ":"so",

    # ለ
    "ለ":"le", "ሉ":"lu", "ሊ":"li", "ላ":"la", "ሌ":"le", "ል":"l", "ሎ":"lo",

    # መ
    "መ":"me", "ሙ":"mu", "ሚ":"mi", "ማ":"ma", "ሜ":"me", "ም":"m", "ሞ":"mo",

    # ረ
    "ረ":"re", "ሩ":"ru", "ሪ":"ri", "ራ":"ra", "ሬ":"re", "ር":"r", "ሮ":"ro",

    # ሰ
    "ሰ":"se", "ሱ":"su", "ሲ":"si", "ሳ":"sa", "ሴ":"se", "ስ":"s", "ሶ":"so",

    # ሸ
    "ሸ":"she", "ሹ":"shu", "ሺ":"shi", "ሻ":"sha", "ሼ":"she", "ሽ":"sh", "ሾ":"sho",

    # ቀ
    "ቀ":"qe", "ቁ":"qu", "ቂ":"qi", "ቃ":"qa", "ቄ":"qe", "ቅ":"q", "ቆ":"qo",

    # ቈ
    "ቈ":"qwo", "ቊ":"qwi", "ቋ":"qwa", "ቌ":"qwe",

    # በ
    "በ":"be", "ቡ":"bu", "ቢ":"bi", "ባ":"ba", "ቤ":"be", "ብ":"b", "ቦ":"bo",

    # ቨ
    "ቨ":"ve", "ቩ":"vu", "ቪ":"vi", "ቫ":"va", "ቬ":"ve", "ቭ":"v", "ቮ":"vo",

    # ተ
    "ተ":"te", "ቱ":"tu", "ቲ":"ti", "ታ":"ta", "ቴ":"te", "ት":"t", "ቶ":"to",

    # ቸ
    "ቸ":"che", "ቹ":"chu", "ቺ":"chi", "ቻ":"cha", "ቼ":"che", "ች":"ch", "ቾ":"cho",

    # ኀ
    "ኀ":"ha", "ኁ":"hu", "ኂ":"hi", "ኃ":"ha", "ኄ":"he", "ኅ":"h", "ኆ":"ho",

    # ነ
    "ነ":"ne", "ኑ":"nu", "ኒ":"ni", "ና":"na", "ኔ":"ne", "ን":"n", "ኖ":"no",

    # ኘ
    "ኘ":"nye", "ኙ":"nyu", "ኚ":"nyi", "ኛ":"nya", "ኜ":"nye", "ኝ":"ny", "ኞ":"nyo",

    # አ
    "አ":"a", "ኡ":"u", "ኢ":"i", "ኣ":"a", "ኤ":"e", "እ":"e", "ኦ":"o",

    # ዐ
    "ዐ":"a", "ዑ":"u", "ዒ":"i", "ዓ":"a", "ዔ":"e", "ዕ":"e", "ዖ":"o",

    # ከ
    "ከ":"ke", "ኩ":"ku", "ኪ":"ki", "ካ":"ka", "ኬ":"ke", "ክ":"k", "ኮ":"ko",

    # ኰ
    "ኰ":"kwo", "ኲ":"kwi", "ኳ":"kwa", "ኴ":"kwe",

    # ኸ
    "ኸ":"kha", "ኹ":"khu", "ኺ":"khi", "ኻ":"kha", "ኼ":"khe", "ኽ":"kh", "ኾ":"kho",

    # ደ
    "ደ":"de", "ዱ":"du", "ዲ":"di", "ዳ":"da", "ዴ":"de", "ድ":"d", "ዶ":"do",

    # ዸ
    "ዸ":"dje", "ዹ":"dju", "ዺ":"dji", "ዻ":"dja", "ዼ":"dje", "ዽ":"dj", "ዾ":"djo",

    # ወ
    "ወ":"we", "ዉ":"wu", "ዊ":"wi", "ዋ":"wa", "ዌ":"we", "ው":"w", "ዎ":"wo",

    # ዘ
    "ዘ":"ze", "ዙ":"zu", "ዚ":"zi", "ዛ":"za", "ዜ":"ze", "ዝ":"z", "ዞ":"zo",

    # ዠ
    "ዠ":"zhe", "ዡ":"zhu", "ዢ":"zhi", "ዣ":"zha", "ዤ":"zhe", "ዥ":"zh", "ዦ":"zho",

    # የ
    "የ":"ye", "ዩ":"yu", "ዪ":"yi", "ያ":"ya", "ዬ":"ye", "ይ":"y", "ዮ":"yo",

    # ገ
    "ገ":"ge", "ጉ":"gu", "ጊ":"gi", "ጋ":"ga", "ጌ":"ge", "ግ":"g", "ጎ":"go",

    # ጐ
    "ጐ":"gwo", "ጒ":"gwi", "ጓ":"gwa", "ጔ":"gwe",

    # ጘ
    "ጘ":"gne", "ጙ":"gnu", "ጚ":"gni", "ጛ":"gna", "ጜ":"gne", "ጝ":"gn", "ጞ":"gno",

    # ጀ
    "ጀ":"je", "ጁ":"ju", "ጂ":"ji", "ጃ":"ja", "ጄ":"je", "ጅ":"j", "ጆ":"jo",

    # ጠ
    "ጠ":"te", "ጡ":"tu", "ጢ":"ti", "ጣ":"ta", "ጤ":"te", "ጥ":"t", "ጦ":"to",

    # ጨ
    "ጨ":"che", "ጩ":"chu", "ጪ":"chi", "ጫ":"cha", "ጬ":"che", "ጭ":"ch", "ጮ":"cho",

    # ጰ
    "ጰ":"phe", "ጱ":"phu", "ጲ":"phi", "ጳ":"pha", "ጴ":"phe", "ጵ":"ph", "ጶ":"pho",

    # ጸ
    "ጸ":"tse", "ጹ":"tsu", "ጺ":"tsi", "ጻ":"tsa", "ጼ":"tse", "ጽ":"ts", "ጾ":"tso",

    # ፀ
    "ፀ":"tse", "ፁ":"tsu", "ፂ":"tsi", "ፃ":"tsa", "ፄ":"tse", "ፅ":"ts", "ፆ":"tso",

    # ፈ
    "ፈ":"fe", "ፉ":"fu", "ፊ":"fi", "ፋ":"fa", "ፌ":"fe", "ፍ":"f", "ፎ":"fo",

    # ፐ
    "ፐ":"pe", "ፑ":"pu", "ፒ":"pi", "ፓ":"pa", "ፔ":"pe", "ፕ":"p", "ፖ":"po",

    # ዀ
    "ዀ":"qha", "዁":"qhu", "ዂ":"qhi", "ዃ":"qhwa", "ዄ":"qhe", "ዅ":"qh", "዆":"qho",

    # Punctuation
    "።": "።",
    "፣": "፣",
    "፤": "፤",
    "፥": "፥",
    "፦": "፦",
    "፧": "፧",
    "፨": "፨"
}

def convert_word():
    text = input_box.get("1.0", tk.END).strip()

    converted = ""

    for letter in text:
        converted += geez_to_english.get(letter, letter)

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, converted)


# Create Window
window = tk.Tk()
window.title("Loza")
window.geometry("700x600")
window.configure(bg="white")

# Title
title = tk.Label(
    window,
    text="Loza",
    font=("Arial", 28, "bold"),
    bg="white"
)
title.pack(pady=5)

subtitle = tk.Label(
    window,
    text="Amharic • Tigrinya • Ge'ez → English Letters",
    font=("Arial", 12),
    bg="white"
)
subtitle.pack()

# Language Dropdown
language_label = tk.Label(
    window,
    text="Choose Language:",
    bg="white"
)
language_label.pack(pady=5)

language = ttk.Combobox(
    window,
    values=["Amharic", "Tigrinya", "Ge'ez"],
    state="readonly"
)
language.current(0)
language.pack()

# Input Box
input_label = tk.Label(
    window,
    text="Type your word or sentence:",
    bg="white"
)
input_label.pack(pady=10)

input_box = tk.Text(
    window,
    height=6,
    width=60,
    font=("Arial", 12)
)
input_box.pack()

# Button
convert_button = tk.Button(
    window,
    text="Convert to English Letters",
    command=convert_word,
    font=("Arial", 12)
)
convert_button.pack(pady=15)

# Output Box
output_label = tk.Label(
    window,
    text="English Letters:",
    bg="white"
)
output_label.pack()

output_box = tk.Text(
    window,
    height=6,
    width=60,
    font=("Arial", 12)
)
output_box.pack(pady=10)

# Run App    
window.mainloop()
