# ExamGradeEye

This little script automates the process of checking for newly published grades on the [HTW Dresden's exam results page](https://mobil.htw-dresden.de/de/mein-studium/noten-und-pruefungen).

## Here's a detailed walkthrough of its operation:

### 1. **Automated Login:** 
The script uses the Selenium library to automatically navigate to the HTW Dresden login page. It enters the provided username and password, and logs in to access the examination results page.

### 2. **Grade Retrieval:** 
Once logged in, the script navigates to the page containing the exam results. It then waits for the page to fully load and retrieves the number of exam credits earned, which is essentially the total number of passed exams.

### 3. **Grade Comparison:** 
The retrieved number of passed exams is then compared to a previously stored value, read from a local text file ("last_count.txt").

### 4. **Email Notification:** 
If the current exam count is different from the stored value, indicating that a new grade has been published, the script sends an email notification. This email contains the new number of passed exams and a congratulatory message. The script uses the smtplib library to connect to an SMTP server, log in with the provided email credentials, compose an email, and send it.

### 5. **Update Stored Grade Count:** 
If the grades have changed, the script updates the stored count value in the text file ("last_count.txt") to match the latest count.



### **Running the Script**
The script is intended to run at regular intervals, typically every 10 minutes during daytime. This way, as soon as a new grade comes out, you'll be notified via email. You can configure the schedule using a job scheduler like cron on Unix-based systems or Task Scheduler on Windows.


