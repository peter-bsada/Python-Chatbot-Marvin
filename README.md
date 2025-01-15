# Marvin: A Python Chatbot

Marvin is a command-line chatbot assistant written in Python. It provides an interactive menu where users can perform various tasks such as temperature conversion, text manipulations, inventory management, and random quotes.

## Features
- **Interactive Menu** – Navigate through different chatbot functionalities.
- **Inventory System** – Add, remove, and list items.
- **Quote Generator** – Get random quotes from *The Hitchhiker's Guide to the Galaxy*.
- **Text-based Utilities** – Convert text, manipulate words, check for isograms, and more.
- **Randomized Mood Messages** – Generates dynamic text based on moods and smileys.

## Installation
### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Python-Chatbot-Marvin.git
cd Python-Chatbot-Marvin
```

### Run the Program
Ensure you have Python installed (version 3.x recommended).
```bash
python3 main.py
```

## Usage
Once the script is running, you will see an ASCII art of Albert (Marvin's alias) and a menu with options.

- Select a number from the menu to perform an action.
- Type `q` to quit the program.
- Use `inv pick ITEM` to add an item to your inventory.
- Use `inv drop ITEM` to remove an item.

### Example Interaction:
```
Hello my name is Albert. I know about everything in the world. What can I do for you?

1) Present yourself to Marv Albert.
2) Celsius to Fahrenheit.
3) Multiply a word.
...
inv pick Sword
inv drop Shield
q
```

## File Structure
```
📂 Python-Chatbot-Marvin
├── 📄 main.py           # Main script with menu handling
├── 📄 marvin.py         # Core chatbot functions
├── 📄 inventory.py      # Inventory management system
├── 📄 menyval12.py      # Randomized text generator
├── 📄 quote.py          # Quote generator module
├── 📄 quotes.txt        # File containing quotes
├── 📄 format.txt        # Text format template
└── 📄 inv.data          # Inventory data storage
```

## Contributing
Feel free to fork the repository and contribute by submitting pull requests. Suggestions and improvements are always welcome!

## License
This project is open-source and available under the MIT License.

---
✨ *Don't panic! Just let Marvin do the thinking.*

