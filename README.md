<h1 align="center" id="title">SPYSEE : A Keylogger Malware 🖼️🖨️</h1>


<p align="center"><img src="https://socialify.git.ci/Minhal128/SPYSEE/image?font=KoHo&language=1&logo=https%3A%2F%2Fimg.freepik.com%2Fpremium-vector%2Fskull-crossbones_951778-2136.jpg&name=1&owner=1&pattern=Solid&stargazers=1&theme=Light"></p>

<p>I am pleased to announce the development of **SPYSEE**, my first malware as a Cyber Security student specializing in red teaming. SPYSEE is a sophisticated keylogger designed to capture and record keystrokes on a target system, gathering sensitive information such as credentials and messages. This project has been a significant milestone in my journey, providing valuable hands-on experience with offensive security techniques. Developing SPYSEE has deepened my understanding of keylogging methods and the importance of defending against such threats, reinforcing my passion for mastering the complexities of cybersecurity..<p/> 


<h1 align="center" id="title">Disclaimer</h1>
<img src="https://imgur.com/TSEi6cr.gif" alt=" You got HACKED !">
<p>SPYSEE is intended solely for educational purposes and ethical cybersecurity research. It is designed to demonstrate keylogging threats in a controlled environment and should not be used for any unauthorized or illegal activity. By using this software, you confirm that you are 18 years or older and fully understand the legal risks involved. Any misuse, such as unauthorized data collection or system compromise, is strictly prohibited and is the sole responsibility of the user. The developer is not liable for any damages or legal consequences arising from improper use. Always obtain permission before using this tool on any system.</p>

<h2>🔎 Project Preview</h2>
<p>To get a sneak peek of the project, go ahead and run this on your device... if you're in the mood for some digital thrill-seeking (don't worry, your keyboard might survive). Just kidding!no need to panic! 😄</p>

<h2>🧐 Features</h2>

Our project SPYSEE offers a range of functionalities " Beware of us "
<ul>
  <li>Keystroke Logging: Records every keystroke pressed by the user, including special keys like space, enter, tab, and control.</li>
  <li>Screenshot Capture: Automatically captures screenshots of the screen every time the spacebar is pressed, providing visual evidence of user activity.</li>
  <li>Camera Snapshots: Takes pictures using the system’s camera whenever the "Enter" key is pressed, capturing the environment in real-time.</li>
  <li>Clipboard Monitoring: Captures the contents of the clipboard when the "Ctrl" key is pressed, logging any copied text or sensitive data.</li>
  <li>Silent Background Operation: The keylogger runs quietly in the background without alerting the user, making it highly discreet.</li>
  <li>Scheduled Shutdown: On pressing the "Tab" key, the system is scheduled to shut down in 60 seconds.</li>
  <li>Email Reporting (Optional): Logs can be sent directly to the specified email address, providing a remote monitoring option.</li>
  <li>Automatic File Logging: Keylogs, screenshots, clipboard data, and camera captures are stored locally in designated folders for easy access.</li>
  <li>Customizable Reporting Interval: Choose the interval for generating reports, with logs being saved or emailed every specified number of seconds.</li>
  <li>Seamless Deployment: Converts SPYSEE and other Python scripts into standalone executables, ensuring cross-platform compatibility and bundling all dependencies into a single file for easy distribution and execution on any system without requiring Python.</li>
  <li>Remote Data Transmission: Sends captured data directly to a specified server IP for centralized collection, eliminating local storage on the attacked machine.</li>
</ul>
<img src="https://imgur.com/sQt5Aev.jpg" alt="E-LOCKS Features">

  
<h2>🛠 Installation Steps:</h2>

<p>1. Clone the repository</p>

```bash
    git clone https://github.com/Minhal128/SPYSEE.git
```

<p>2. Install & Run python Language & its modules</p>

```bash Modules to Install
pip install opencv-python
pip install Pillow
pip install pyperclip
pip install keyboard


 # Run the executable 
python keylogger.py
or 
python3 keylogger.py

```

<h2 align="center">Working </h2>
<p>
  This keylogger captures keystrokes and system events, including screenshots, webcam images, and clipboard data, while sending reports at specified intervals. Below is a detailed breakdown of its functionalities:
<h3><li>Modules Used</li></h3>
<ul>
  <li>opencv-python</li>
  <li>Pillow</li>
  <li>pyperclip</li>
  <li>keyboard</li>
  <li>request</li>
</ul>  

</p>
<h3>Working</h3>
<ul>
    <li>
        <strong>Key Logging:</strong> The keylogger uses the keyboard library to listen for keyboard events.
        When a key is pressed, the <code>key_press</code> method captures the key name and appends it to the log.
    </li>
    <li>
        <strong>Logging Mechanism:</strong>
        <ul>
            <li>Continuously logs keystrokes to a string variable.</li>
            <li>
                At regular intervals (defined by <code>SEND_REPORT_EVERY</code>, set to 40 seconds), the <code>report</code> method is invoked to handle log data:
                <ul>
                    <li>Sends logs via email or saves them to a file based on the specified report method.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <strong>File and Email Reporting:</strong>
        <ul>
            <li>Logs can be sent through email using the <code>smtplib</code> library, formatted in both plain text and HTML:</li>
            <li><strong>Email Configuration:</strong> Requires valid email credentials for sending logs.</li>
            <li>Alternatively, logs are appended to <code>keylog.txt</code> in the designated shared folder (<code>H:\Development\logme</code>).</li>
        </ul>
    </li>
    <li>
        <strong>Screenshot and Webcam Capture:</strong>
        <ul>
            <li>Captures screenshots using <code>ImageGrab</code> from the <code>PIL</code> library, saving them in the <code>screenshots</code> directory.</li>
            <li>Takes webcam pictures using <code>OpenCV</code>, storing them in the <code>camera_pics</code> directory.</li>
        </ul>
    </li>
    <li>
        <strong>Clipboard Monitoring:</strong>
        <ul>
            <li>Monitors the clipboard for changes and saves its content to <code>clipboard.txt</code> each time the Ctrl key is pressed:</li>
            <li>Timestamps each entry for tracking when the clipboard data was captured.</li>
        </ul>
    </li>
    <li>
        <strong>Scheduled Shutdown:</strong>
        <ul>
            <li>Offers the ability to shut down the computer 60 seconds after pressing the Tab key:</li>
            <li>Ensures users are notified of the scheduled shutdown.</li>
        </ul>
    </li>
    <li>
        <strong>Silent Operation:</strong>
        <ul>
            <li>Designed to operate discreetly without user interaction or visible output:</li>
            <li>The logging process continues in the background until stopped by pressing the <code>Esc</code> key.</li>
        </ul>
    </li>
</ul>

<h3>Usage</h3>
<p>To run the keylogger:</p>
<ul>
    <li>Ensure the necessary libraries are installed (<code>opencv-python</code>, <code>Pillow</code>, <code>pyperclip</code>, <code>keyboard</code>).</li>
    <li>Update the email settings with valid credentials.</li>
    <li>Execute the script to allow it to run in the background, capturing the specified data.</li>
</ul>

<h3>Important Note</h3>
<p>This keylogger is intended for educational purposes and ethical hacking. Always obtain explicit permission from users before running such software on their devices.</p>

</p>

<p>Run it to know the features 😈</p>
<img src ="https://imgur.com/Bh38Ot3.png">

<h2>🤝Team Contribution</h2>
<h3>Minhal Rizvi</h3> 
<ul>
  <li>Keylogger Implementation, Log Management, Timer and Reporting, Error Handling, Deployment, Testing. </li>
</ul>
<h3>Mufaddal Huzaifa</h3> 
<ul>
  <li>Screenshot Functionality, Camera Capture, Clipboard Management, Email logs, Integration of venv. </li>
  
<h2>⚠️Limitations</h2>
<li>Performance Overhead</li>
<li>No Data Encryption</li>
<li>Single Reporting Method</li>
<li>Not able to bypass MAC os</li>

<h2>🔮Future Enhancements</h2>
<li>Dynamic Configuration</li>
<li>Data Visualization</li>
<li>Cloud User Management Database</li>
<li>Reverse shell (27/11/2024 😈)</li>
<p>

<h2>What I Learned from the <br>SPYSEE</br></h2>

<h3>Technical Skills</h3>
<ul>
  <li><strong>Python Programming</strong>: Enhanced proficiency in Python, particularly with libraries like <code>keyboard</code>, <code>cv2</code>, and <code>PIL</code>.</li>
  <li><strong>Event Handling</strong>: Gained experience in handling keyboard events and creating responsive applications.</li>
  <li><strong>File Management</strong>: Learned to read from and write to files, including managing different file types for logging data.</li>
  <li><strong>Email Functionality</strong>: Implemented email features using the <code>smtplib</code> library for sending logs, gaining insights into how email protocols work.</li>
  <li><strong>Image Processing</strong>: Developed skills in capturing screenshots and camera images using <code>PIL</code> and <code>OpenCV</code>.</li>
  <li><strong>Error Handling</strong>: Improved ability to anticipate potential errors and implement exception handling to create more robust applications.</li>
  <li><strong>Multithreading</strong>: Gained understanding of using threading to perform background tasks, like periodic reporting.</li>
</ul>

<h3>Conceptual Understanding</h3>
<ul>
  <li><strong>Keylogging Ethics</strong>: Understood the ethical implications and potential legal issues surrounding keylogging software.</li>
  <li><strong>Data Privacy</strong>: Learned about the importance of data security, especially when handling sensitive information like keystrokes and clipboard data.</li>
  <li><strong>System Resources</strong>: Gained awareness of how background processes can impact system performance.</li>
</ul>

<h3>Development Practices</h3>
<ul>
  <li><strong>Modular Design</strong>: Applied principles of modular programming by organizing code into functions and classes for better readability and maintainability.</li>
  <li><strong>Version Control</strong>: If using version control (like Git) for the project, learned about managing code changes and collaboration.</li>
  <li><strong>Testing and Debugging</strong>: Improved skills in testing and debugging code to ensure functionality and reliability.</li>
</ul>

<h3>Future Skills to Explore</h3>
<ul>
  <li><strong>Data Encryption</strong>: Consider learning about data encryption techniques to secure logged information.</li>
  <li><strong>Cross-Platform Development</strong>: Explore how to make applications compatible across different operating systems.</li>
  <li><strong>User Interface Design</strong>: Consider diving into UI/UX design to enhance user interaction with applications.</li>
  <li><strong>Networking Concepts</strong>: Deepen understanding of networking and protocols to improve the communication aspect of applications.</li>
</ul>

  
<h2>💖Hope you Like our work!</h2>

This project needs a ⭐ from you. Don't forget to leave a star ⭐
