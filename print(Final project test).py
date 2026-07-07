from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# Basic Ge'ez transliteration table
GE_EZ = {
    "ሀ": "ha", "ሁ": "hu", "ሂ": "hi", "ሃ": "ha", "ሄ": "he", "ህ": "h", "ሆ": "ho",
    "ለ": "le", "ሉ": "lu", "ሊ": "li", "ላ": "la", "ሌ": "le", "ል": "l", "ሎ": "lo",
    "መ": "me", "ሙ": "mu", "ሚ": "mi", "ማ": "ma", "ሜ": "me", "ም": "m", "ሞ": "mo",
    "ሰ": "se", "ሱ": "su", "ሲ": "si", "ሳ": "sa", "ሴ": "se", "ስ": "s", "ሶ": "so",

    "ቀ": "qe", "ቁ": "qu", "ቂ": "qi", "ቃ": "qa", "ቄ": "qe", "ቅ": "q", "ቆ": "qo",

    "አ": "a", "ኡ": "u", "ኢ": "i", "ኣ": "a", "ኤ": "e", "እ": "e", "ኦ": "o",

    "በ": "be", "ቡ": "bu", "ቢ": "bi", "ባ": "ba", "ቤ": "be", "ብ": "b", "ቦ": "bo",

    "የ": "ye", "ዩ": "yu", "ዪ": "yi", "ያ": "ya", "ዬ": "ye", "ይ": "y", "ዮ": "yo",

    "ረ": "re", "ሩ": "ru", "ሪ": "ri", "ራ": "ra", "ሬ": "re", "ር": "r", "ሮ": "ro",

    "ገ": "ge", "ጉ": "gu", "ጊ": "gi", "ጋ": "ga", "ጌ": "ge", "ግ": "g", "ጎ": "go",

    " ": " ",
    "።": ".",
    "፣": ","
}


def transliterate(text):
    result = ""

    for letter in text:
        if letter in GE_EZ:
            result += GE_EZ[letter]
        else:
            result += letter

    return result


class LozaApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.input_box = TextInput(
            hint_text="Type Amharic/Tigrinya/Ge'ez here",
            size_hint_y=0.4
        )

        self.output = Label(
            text="Loza output will appear here",
            size_hint_y=0.4
        )

        button = Button(
            text="Convert",
            size_hint_y=0.2
        )

        button.bind(
            on_press=self.convert_text
        )

        layout.add_widget(self.input_box)
        layout.add_widget(button)
        layout.add_widget(self.output)

        return layout


    def convert_text(self, instance):

        original = self.input_box.text

        converted = transliterate(original)

        self.output.text = converted



LozaApp().run()