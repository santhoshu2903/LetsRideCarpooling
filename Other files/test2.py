import tkinter as tk
import socket
import threading

# Function to send messages
def send_message():
    message = my_message.get()
    my_message.set("")
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + message + "\n")
    chat_log.config(state=tk.DISABLED)
    conn.send(message.encode("utf-8"))

# Function to receive messages
def receive_messages():
    while True:
        try:
            message = conn.recv(1024).decode("utf-8")
            chat_log.config(state=tk.NORMAL)
            chat_log.insert(tk.END, "Friend: " + message + "\n")
            chat_log.config(state=tk.DISABLED)
        except ConnectionAbortedError:
            break

# Create a socket for communication
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 12345))  # Change this to your server address

# Create a tkinter window
root = tk.Tk()
root.title("Chat Application")

# Create a text widget for the chat log
chat_log = tk.Text(root, state=tk.DISABLED)
chat_log.pack()

# Create an entry field for typing messages
my_message = tk.StringVar()
message_entry = tk.Entry(root, textvariable=my_message)
message_entry.pack()

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

root.mainloop()
