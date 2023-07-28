from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from email.mime.text import MIMEText
import smtplib
import time

# Funktion, um E-Mails zu senden
def send_email(content):
    from_email = "youremail@outlook.de"
    password = "yourpassword"
    to_email = from_email 
    subject = "Änderung der Prüfungszahl"
    
    msg = MIMEText(content)
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# Automatisierung mit Selenium
def get_pruefung_count():
   # Setup the Chrome webdriver
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)

    browser.get("https://mobil.htw-dresden.de/de/mein-studium/noten-und-pruefungen")

    # Login
    browser.find_element(By.ID, "usernameInput").send_keys("sXXXXX")
    browser.find_element(By.ID, "passwordInput").send_keys("yourpassword")
    browser.find_element(By.NAME, "submit").click()

    # Wait for the page to load and the desired element to be present
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".badge.badge-credits"))
    )
    pruefung_elements = browser.find_elements(By.CSS_SELECTOR, ".badge.badge-credits")
    pruefung_text = pruefung_elements[2].text  # Get the text of the second element
    pruefung_count = int(pruefung_text.split()[0])
    
    browser.close()
    return pruefung_count


current_count = get_pruefung_count()

try:
    with open("last_count.txt", "r") as f:
        last_count = int(f.read())
except:
    last_count = 0

if current_count != last_count:
    send_email(f"Du hast nun {current_count} Prüfungsleistungen erbracht, WOW!")
    with open("last_count.txt", "w") as f:
        f.write(str(current_count))
