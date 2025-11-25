
# 🌍 Multi-Language Translator (Python + Tkinter)

A clean and intuitive desktop translator built with **Python**, **Tkinter**, and **deep-translator**.  
This application allows users to translate text between **dozens of languages** using Google Translate integration.

---

## 🚀 Features

- 🌐 Translate between many supported languages  
- 🔄 Swap source and target languages instantly  
- 🖥️ Simple and modern GUI built with Tkinter  
- ⚡ Fast translations powered by `deep-translator`  
- 🪶 Lightweight and easy to run  
- 📘 Perfect for Python portfolio projects  

---

## 📦 Requirements

- Python 3.x  
- Internet connection  
- `deep-translator` Python package  

---

## 🔧 Installation

Open a terminal inside the project folder and install the required dependency:

```bash
python -m pip install deep-translator
```

> ℹ️ Using `python -m pip` ensures that the package is installed in the correct Python interpreter (recommended for VS Code and Windows users).

---

## ▶️ How to Run

Inside the project folder, run:

```bash
python main.py
```

The graphical translator interface will open.

---

## 📁 Project Structure

```
translator/
│── main.py
│── README.md
└── (optional assets folder)
```

---

## 🧩 How It Works

- The app retrieves all available Google Translate languages using `deep-translator`.
- Languages are displayed in dropdown menus (Combobox widgets).
- When the user clicks **Translate**, the app sends the text to Google Translator and displays the result.
- The **Swap** button instantly exchanges input/output languages and moves translated text back into the input box.

---

## 👨‍💻 Author

Created by **Fabricio Cardozo**  
Designed as a professional Python portfolio project.

---

## 📄 License

MIT License – free to use and modify.
