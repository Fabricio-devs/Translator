import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# -------------------------------------------------
# Build language dictionary: {"English": "en", ...}
# -------------------------------------------------
def get_language_dict():
    """
    Returns a dictionary mapping language names (capitalized)
    to their ISO codes, e.g. {"English": "en"}.
    """
    # deep_translator returns something like {"english": "en", ...}
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    return {name.capitalize(): code for name, code in langs.items()}


# Create language dictionary once
LANG_DICT = get_language_dict()
LANG_NAMES = sorted(LANG_DICT.keys())  # for the dropdowns


# -------------------------------------------------
# Main translator function
# -------------------------------------------------
def translate_text():
    """
    Reads text from the input box, source language and target language
    from the dropdowns, and places the translated text in the output box.
    """
    src_lang_name = combo_from.get()
    tgt_lang_name = combo_to.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Empty text", "Please type something to translate.")
        return

    if not src_lang_name or not tgt_lang_name:
        messagebox.showwarning("Language missing", "Please select both languages.")
        return

    src_code = LANG_DICT[src_lang_name]
    tgt_code = LANG_DICT[tgt_lang_name]

    try:
        translator = GoogleTranslator(source=src_code, target=tgt_code)
        translated = translator.translate(text)
    except Exception as e:
        messagebox.showerror("Translation error", f"An error occurred:\n{e}")
        return

    # Clear output and insert result
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)


def swap_languages():
    """
    Swaps the 'from' and 'to' languages and moves translated text
    back to the input box, to allow quick reverse translations.
    """
    src = combo_from.get()
    tgt = combo_to.get()
    combo_from.set(tgt)
    combo_to.set(src)

    current_output = output_text.get("1.0", tk.END).strip()
    if current_output:
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, current_output)
        output_text.delete("1.0", tk.END)


# -------------------------------------------------
# Build GUI
# -------------------------------------------------
root = tk.Tk()
root.title("Multi-language Translator")
root.geometry("800x500")

# ---- Top frame: language selectors ----
top_frame = ttk.Frame(root, padding=10)
top_frame.pack(fill="x")

label_from = ttk.Label(top_frame, text="From:")
label_from.pack(side="left", padx=(0, 5))

combo_from = ttk.Combobox(top_frame, values=LANG_NAMES, state="readonly", width=20)
combo_from.pack(side="left", padx=(0, 20))

label_to = ttk.Label(top_frame, text="To:")
label_to.pack(side="left", padx=(0, 5))

combo_to = ttk.Combobox(top_frame, values=LANG_NAMES, state="readonly", width=20)
combo_to.pack(side="left", padx=(0, 20))

# Default languages (change if you want)
if "Spanish" in LANG_NAMES:
    combo_from.set("Spanish")
if "English" in LANG_NAMES:
    combo_to.set("English")

btn_swap = ttk.Button(top_frame, text="Swap", command=swap_languages)
btn_swap.pack(side="left")

# ---- Middle frame: text areas ----
middle_frame = ttk.Frame(root, padding=10)
middle_frame.pack(fill="both", expand=True)

# Input text
input_label = ttk.Label(middle_frame, text="Input text")
input_label.pack(anchor="w")

input_text = tk.Text(middle_frame, height=10, wrap="word")
input_text.pack(fill="both", expand=True, pady=(0, 10))

# Translate button
btn_translate = ttk.Button(root, text="Translate", command=translate_text)
btn_translate.pack(pady=5)

# Output text
bottom_frame = ttk.Frame(root, padding=10)
bottom_frame.pack(fill="both", expand=True)

output_label = ttk.Label(bottom_frame, text="Translated text")
output_label.pack(anchor="w")

output_text = tk.Text(bottom_frame, height=10, wrap="word")
output_text.pack(fill="both", expand=True)

# Start the app loop
root.mainloop()
