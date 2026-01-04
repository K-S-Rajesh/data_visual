import webbrowser
import pyautogui as pag
import time
import win32com.client
import re
import time
import pythoncom



def get_outlook_otp(subject_keyword, sender_email="retaildashboard@indianoil.in"):
    """
    Connects to Outlook, finds the latest email with a specific subject keyword,
    and extracts a 6-digit OTP using regex.

    :param subject_keyword: A keyword present in the email subject.
    :param sender_email: (Optional) The email address of the sender.
    :return: The extracted OTP as a string, or None if not found.
    """
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    # 6 refers to the Inbox folder
    inbox = outlook.GetDefaultFolder(6)
    target_folder = inbox.Folders.Item("retail dashboard")
    messages = target_folder.Items
    # Sort messages by ReceivedTime in descending order (True) to get the latest first
    messages.Sort("[ReceivedTime]", True)

    # Regex pattern to match a 6-digit number
    otp_pattern = re.compile(r'\b\d{7}\b')

        # Iterate through the most recent emails (e.g., top 10)
    for i in range(min(10, len(messages))):
        message = messages.Item(i + 1)
        # Check if the email matches the criteria (subject keyword and optional sender)
        if subject_keyword.lower() in message.Subject.lower():
            if sender_email is None or sender_email.lower() in message.SenderEmailAddress.lower():
                # Extract the OTP from the email body
                match = otp_pattern.search(message.Body)
                if match:
                    otp_variable = match.group(0)
                    print(f"Found OTP: {otp_variable}")
                    return otp_variable

    print("No matching email or OTP found.")
    return None


# --- Example Usage ---
# Replace 'Your OTP Subject' with the actual subject line or keyword of the OTP email
# Replace 'sender@example.com' with the actual sender's email (optional)
# otp_code = get_outlook_otp(subject_keyword='Your OTP Subject', sender_email='sender@example.com')



# webbrowser.open("https://spandan.indianoil.co.in/RetailNew/Login.jsp")
# time.sleep(10)
# pag.press('tab')
# time.sleep(2)
# pag.write('00501203')
# time.sleep(1)
# pag.press('tab',presses=3)
# pag.write((pag.prompt(text='Enter the capcha', title='MSG Box' , default='')))
# time.sleep(2)
pag.hotkey('alt','tab')
time.sleep(3)
for i in range(50):
    pag.press('pageup')
    time.sleep(1)
    pag.click(x=432, y=551)
    time.sleep(1)
    time.sleep(40)
    pag.click(x=1754, y=693)
    # pag.click(x=1751, y=774)
    time.sleep(30)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.press('pagedown')
    time.sleep(1)
    pag.click(x=800, y=616)
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('r')
    time.sleep(1)
    # pag.click(x=601, y=816)
    pag.press('tab')
    time.sleep(2)
    pag.write('Please modify workflow with DRSH as final approving authority')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    pag.press('pagedown')
    time.sleep(3)
    # pag.click(x=969, y=966)
    # pag.click(x=999, y=1009)
    pag.click(x=973, y=1006)  #firefox lenovo
    # pag.click(x=980, y=968)
    time.sleep(3)
    pag.click(x=1308, y=1164)
    time.sleep(3)
    pag.click(x=581, y=160)
    time.sleep(10)
    pag.click(x=581, y=160)
    time.sleep(60)
    pag.hotkey('alt','tab')
    time.sleep(3)
    otp_code = get_outlook_otp(subject_keyword='eProposal Approval OTP')  # Example
    time.sleep(3)
    pag.write(otp_code)
    # pag.write(pag.prompt('enter OTP'))
    time.sleep(3)
    pag.press('tab')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.press('enter')
    time.sleep(13)
    # pag.click(x=921, y=405)

    pag.press('enter')
    time.sleep(13)


