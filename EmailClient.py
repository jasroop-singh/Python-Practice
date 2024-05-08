# Names: Jasroop Singh, Evin Menendez Vargas, Vatche Balian
# Group 11
# Final Project CS3800.01

# Libraries
import smtplib
import tkinter as tk
from tkinter import messagebox

# method to enable the widgets
def enable(state):
    recipientEmailInput.config(state = state)
    subjectInput.config(state = state)
    messageTxt.config(state = state)

# method to login
def login():
    sender_email = senderEmailInput.get()
    sender_password = senderPassInput.get()
    server_address = serverInput.get()

    try:
        # Connect to the SMTP server provided by the user (usually smtp.gmail.com)
        server = smtplib.SMTP(server_address, 587)
        # Start TCP connection
        server.starttls()
        # Login to our email account
        server.login(sender_email, sender_password)  
        messagebox.showinfo("Success", "Login was successful!")
        # Enable textboxes
        enable(tk.NORMAL) 
        # Enable the send button
        sendBtn.config(state = tk.NORMAL)  
    except Exception as e:
        # Show error
        messagebox.showerror("Error", f"Error: {e}")
        # Disable textboxes
        enable(tk.DISABLED)
        # Disable send button 
        sendBtn.config(state = tk.DISABLED)  
    finally:
        # Close the connection to the SMTP server
        try:
            server.quit()
        except NameError:
            pass


# method to send the mail
def sendEmail():
    # Store values from inputboxes too variables 
    sender_email = senderEmailInput.get()
    sender_password = senderPassInput.get()
    recipient_email = recipientEmailInput.get()
    subject_input = subjectInput.get()
    message_input = messageTxt.get("1.0", "end-1c")
    server_address = serverInput.get()

    try:
        server = smtplib.SMTP(server_address, 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Create the email message
        email_message = f"Subject: {subject_input}\n\n{message_input}"

        # Send the email
        server.sendmail(sender_email, recipient_email, email_message)
        messagebox.showinfo("Success", "Email was sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

    finally:
        # Close the connection to the SMTP server
        try:
            server.quit()
        except NameError:
            pass


# GUI
root = tk.Tk()
root.title("Simple Mail Client")
root.geometry("380x350")
root.resizable(False, False)  

# Calculate the width of the message text widget for sizing entry widgets
text_widget_width = 30

# Create labels and input boxes for email details
senderEmailLbl = tk.Label(root, text = "Sender's Email:")
senderEmailLbl.grid(row = 0, column = 0, padx = (10,5), pady = (15,5), sticky = "e")
senderEmailInput = tk.Entry(root)
senderEmailInput.grid(row = 0, column = 1, padx = (0,10), pady = (15,5), sticky = "we")

senderPassLbl = tk.Label(root, text = "Sender's Password:")
senderPassLbl.grid(row = 1, column = 0, padx = (10,5), pady = 5, sticky = "e")
senderPassInput = tk.Entry(root, show = "*")
senderPassInput.grid(row = 1, column = 1, padx = (0,10), pady = 5, sticky = "we")

serverLbl = tk.Label(root, text = "SMTP Server:")
serverLbl.grid(row = 2, column = 0, padx = (10,5), pady = 5, sticky = "e")
serverInput = tk.Entry(root)
serverInput.grid(row = 2, column = 1, padx = (0,10), pady = 5, sticky = "we")

loginBtn = tk.Button(root, text = "Login", command = login)
loginBtn.grid(row = 3, column = 0, columnspan = 2, pady = 5)

recipientEmailLabel = tk.Label(root, text = "Recipient's Email:")
recipientEmailLabel.grid(row = 4, column = 0, padx = (10,5), pady = 5, sticky = "e")
recipientEmailInput = tk.Entry(root, state = tk.DISABLED)
recipientEmailInput.grid(row = 4, column = 1, padx = (0,10), pady = 5, sticky = "we")

subjectLbl = tk.Label(root, text = "Subject:")
subjectLbl.grid(row = 5, column = 0, padx = (10,5), pady = 5, sticky = "e")
subjectInput = tk.Entry(root, state = tk.DISABLED)
subjectInput.grid(row = 5, column = 1, padx = (0,10), pady = 5, sticky = "we")

messageLbl = tk.Label(root, text = "Message:")
messageLbl.grid(row = 6, column = 0, padx = (10,5), pady = 5, sticky = "e")
messageTxt = tk.Text(root, height = 5, width = text_widget_width, state = tk.DISABLED)
messageTxt.grid(row = 6, column = 1, padx = (0,10), pady = 5, sticky = "we")

sendBtn = tk.Button(root, text = "Send Email", command = sendEmail, state = tk.DISABLED)
sendBtn.grid(row = 7, column = 0, columnspan = 2, pady = 10)

# Run
root.mainloop()