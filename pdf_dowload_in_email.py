import imaplib
import email
from email.header import decode_header

def get_unread_emails(email_address, password, mail_server, mailbox="inbox", criteria="(UNSEEN)"):
    unread_emails = []

    # Connect to the server
    mail = imaplib.IMAP4_SSL(mail_server)

    # Login to your account
    mail.login(email_address, password)

    # Select the mailbox you want to search in (e.g., 'inbox')
    mail.select(mailbox)

    # Search for all unread emails based on the provided criteria
    status, messages = mail.search(None, criteria)

    # Get the list of email IDs
    email_ids = messages[0].split()

    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        email_message = msg_data[0][1]
        msg = email.message_from_bytes(email_message)

        subject = msg["Subject"]
        sender = email.utils.parseaddr(msg["From"])[1]

        # Check if the email has a payload
        if msg.is_multipart():
            body = ""
            for part in msg.walk():
                if part.get_content_type() == "text/plain" and part.get_payload() is not None:
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body_payload = msg.get_payload(decode=True)
            body = body_payload.decode() if body_payload is not None else ""

        email_data = {
            "subject": subject,
            "sender": sender,
            "body": body,
            "email_id": email_id
        }

        unread_emails.append(email_data)

    # Logout from the email server
    mail.logout()

    return unread_emails

def download_pdf_attachments(email_address, password, mail_server, email_ids,
                             save_path="C:\\Users\\Vrdella\\Downloads\\attachment\\"):
    # Connect to the server
    mail = imaplib.IMAP4_SSL(mail_server)

    # Login to your account
    mail.login(email_address, password)

    # Select the mailbox
    mail.select("inbox")

    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        email_message = msg_data[0][1]
        msg = email.message_from_bytes(email_message)

        if msg.get_content_maintype() == "multipart":
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart' or part.get("Content-Disposition") is None:
                    continue
                filename = part.get_filename()
                if filename:
                    filename, encoding = decode_header(filename)[0]
                    if isinstance(filename, bytes):
                        filename = filename.decode(encoding or "utf-8")

                    with open(save_path + filename, "wb") as attachment:
                        attachment.write(part.get_payload(decode=True))

    # Logout from the email server
    mail.logout()

# Example usage
email_address = "bhavanisha@vrdella.com"
password = "dexq ylbk akqq dwyt"
mail_server = "imap.gmail.com"

# Get unread emails
unread_emails = get_unread_emails(email_address, password, mail_server)
email_ids = [email_data["email_id"] for email_data in unread_emails]
download_pdf_attachments(email_address, password, mail_server, email_ids)
