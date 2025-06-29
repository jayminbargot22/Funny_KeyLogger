# 🧠 Just a Fun lil Keylogger 🧠

> **DISCLAIMER:**  
> This was made *just for fun*, literally to test if I could build one. That’s it. I’m not a hacker or some villain from Mr. Robot lol.  
> **⚠️ DO NOT use this for any shady or wrong purposes.** Seriously. Respect people’s privacy.

---

## ✨ What's This?

So yeah, I built a basic keylogger in Python using the `pynput` library.  
It listens to whatever keys you type on your keyboard and logs them into a `.txt` file (`keyfile.txt`).

Why?  
Cause I was bored and curious, and wanted to see if I could pull it off 👀

---

## 💻 How It Works (Lowkey Explained)

Here’s the rundown of what the code does:

### `on_press(key)`
- This runs *every time* a key is pressed.
- If it's a normal key like `a`, `1`, etc., it grabs the character and logs it.
- If it's a **special key** (like space, enter, or backspace), it handles those differently:
  - `space` → adds a space (`" "`)
  - `enter` → adds a new line (`\n`)
  - `backspace` → removes the last character from the file

### `on_release(key)`
- If you press the **Esc key**, it ends the program. Simple exit control.

### `log_key(char)`
- Opens the `keyfile.txt` in append mode and adds whatever character was typed.

### `delete_last_char()`
- Reads the whole file, chops off the last character (basically mimics backspace), and rewrites it.

---

## 🚀 How to Run This

1. Install pynput if you haven’t already:
   ```bash
   pip install pynput

2. Then just run the script:
   ```bash
   python keylogger.py

3. It’ll keep listening until you press Esc.


# 📁 Output
All the keys you type will be saved in a file called:

[View the logged keys here (keyfile.txt)](keyfile.txt)

![Screenshot 2025-06-29 235111](https://github.com/user-attachments/assets/0c03a83d-4693-4cfd-90f0-ed2b648ddc8c)

Terminal will look like this.

![Screenshot 2025-06-30 001103](https://github.com/user-attachments/assets/5a693b87-fff6-4052-8db7-9cd7e1bbb36d)



It’ll even handle backspaces and enter keys properly.

# 🤫 Again, Don’t Be Weird
This was made purely outta curiosity and for learning purposes.
Please don't use this for spying on people, stealing data, or anything illegal.
That’s not cool, and it’s literally illegal 💀
