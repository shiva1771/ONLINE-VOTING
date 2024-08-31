import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Sample parties for voting with symbols
parties = {
    "BJP": {"votes": 0, "symbol": "C:\\Users\\shiva\\OneDrive\\Documents\\bjp.jpeg"},
    "CONGRESS": {"votes": 0, "symbol": "C:\\Users\\shiva\\OneDrive\\Documents\\congress.jpeg"},
    "BRS": {"votes": 0, "symbol": "C:\\Users\\shiva\\OneDrive\\Documents\\brs.jpeg"}
}

voter_details = {}
symbol_images = {}
image_height = 100  # Adjust this height as needed

def switch_frame(hide_frame, show_frame):
    """Switch visibility between two frames."""
    hide_frame.pack_forget()
    show_frame.pack(pady=20)

def submit_voter_details():
    """Validate and submit voter details."""
    name, email = name_var.get(), email_var.get()
    
    if not name or not email:
        messagebox.showwarning("Error", "Please enter all details.")
        return

    voter_details.update({"name": name, "voterid": email})
    switch_frame(voter_frame, auth_frame)

def authenticate_face():
    """Simulate face authentication."""
    face_authenticated = True  # Simulate result
    if face_authenticated:
        authenticate_fingerprint()
    else:
        messagebox.showwarning("Authentication Failed", "Face authentication failed.")

def authenticate_fingerprint():
    """Simulate fingerprint authentication."""
    fingerprint_authenticated = True  # Simulate result
    if fingerprint_authenticated:
        switch_frame(auth_frame, main_frame)
    else:
        messagebox.showwarning("Authentication Failed", "Fingerprint authentication failed.")

def cast_vote():
    """Cast a vote for the selected party."""
    selected_party = party_var.get()
    if selected_party:
        parties[selected_party]["votes"] += 1
        messagebox.showinfo("Success", f"Vote casted for {selected_party}!")
    else:
        messagebox.showwarning("Error", "Please select a party to vote.")

def load_symbols():
    """Load party symbols and create radio buttons."""
    for party, info in parties.items():
        try:
            image = Image.open(info["symbol"])
            image_width = int((image_height / image.height) * image.width)
            image = image.resize((image_width, image_height), Image.LANCZOS)
            symbol_images[party] = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image for {party}: {e}")
            symbol_images[party] = None

        create_party_radio_button(party)

def create_party_radio_button(party):
    """Create a radio button for each party."""
    frame = tk.Frame(main_frame)
    frame.pack(anchor=tk.W)

    tk.Radiobutton(frame, text=party, variable=party_var, value=party, font=("Arial", 12)).pack(side=tk.LEFT)
    
    if symbol_images[party]:
        tk.Label(frame, image=symbol_images[party]).pack(side=tk.LEFT)

# Initialize main application window
root = tk.Tk()
root.title("Online Voting System")

# Frame for voter details
voter_frame = tk.Frame(root)
tk.Label(voter_frame, text="Enter your details:", font=("Arial", 14)).pack(pady=10)

name_var, email_var = tk.StringVar(), tk.StringVar()
for label, var in [("Name:", name_var), ("Email:", email_var)]:
    tk.Label(voter_frame, text=label, font=("Arial", 12)).pack(anchor=tk.W, padx=10)
    tk.Entry(voter_frame, textvariable=var, font=("Arial", 12)).pack(padx=10, pady=5)

tk.Button(voter_frame, text="Submit", command=submit_voter_details, font=("Arial", 12)).pack(pady=10)

# Frame for authentication
auth_frame = tk.Frame(root)
tk.Label(auth_frame, text="Authenticate Yourself:", font=("Arial", 14)).pack(pady=10)

for label, command in [("Face Authentication", authenticate_face), ("Fingerprint Authentication", authenticate_fingerprint)]:
    tk.Button(auth_frame, text=label, command=command, font=("Arial", 12)).pack(pady=5)

# Frame for the voting page
main_frame = tk.Frame(root)
tk.Label(main_frame, text="Choose a party to vote:", font=("Arial", 14)).pack(pady=10)

party_var = tk.StringVar(value="")
load_symbols()

tk.Button(main_frame, text="Cast Vote", command=cast_vote, font=("Arial", 12)).pack(pady=10)

# Show the voter details form initially
voter_frame.pack(pady=20)

root.mainloop()
