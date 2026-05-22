import os
import shutil
import tkinter as tk

from tkinter import filedialog, messagebox
from tkinter import BooleanVar

# ----------------------------
# FILE CATEGORIES
# ----------------------------

all_folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

# ----------------------------
# MAIN WINDOW
# ----------------------------

root = tk.Tk()

root.title("Smart File Organizer")
root.geometry("620x500")
root.config(bg="#020617")
root.resizable(False, False)

# ----------------------------
# CATEGORY VARIABLES
# ----------------------------

selected_categories = {}

for category in all_folders:
    selected_categories[category] = BooleanVar(value=True)

# ----------------------------
# ORGANIZER FUNCTION
# ----------------------------

def organize_files():

    path = filedialog.askdirectory()

    if not path:
        return

    selected_folders = {}

    for category, extensions in all_folders.items():

        if selected_categories[category].get():

            selected_folders[category] = extensions

    moved_files = 0

    # CREATE FOLDERS
    for folder in selected_folders:

        folder_path = os.path.join(path, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # MOVE FILES
    for file in os.listdir(path):

        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):

            for folder, extensions in selected_folders.items():

                for ext in extensions:

                    if file.lower().endswith(ext):

                        destination = os.path.join(path, folder, file)

                        if not os.path.exists(destination):

                            shutil.move(file_path, destination)

                            moved_files += 1

    messagebox.showinfo(
        "Completed",
        f"Organization Complete.\nFiles moved: {moved_files}"
    )

# ----------------------------
# MAIN FRAME
# ----------------------------

main_frame = tk.Frame(
    root,
    bg="#0f172a",
    padx=40,
    pady=40
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")

# ----------------------------
# TITLE
# ----------------------------

title = tk.Label(
    main_frame,
    text="SMART FILE ORGANIZER",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="white"
)

title.pack(pady=(0, 15))

# ----------------------------
# SUBTITLE
# ----------------------------

subtitle = tk.Label(
    main_frame,
    text="Modern file automation for productivity.",
    font=("Segoe UI", 12),
    bg="#0f172a",
    fg="#94a3b8"
)

subtitle.pack(pady=(0, 35))

# ----------------------------
# CATEGORY SELECTION
# ----------------------------

checkbox_frame = tk.Frame(
    main_frame,
    bg="#0f172a"
)

checkbox_frame.pack(pady=(0, 30))

for category, var in selected_categories.items():

    checkbox = tk.Checkbutton(
        checkbox_frame,
        text=category,
        variable=var,
        font=("Segoe UI", 11),
        bg="#0f172a",
        fg="white",
        activebackground="#0f172a",
        activeforeground="white",
        selectcolor="#111827",
        padx=10
    )

    checkbox.pack(side="left", padx=10)

# ----------------------------
# ORGANIZE BUTTON
# ----------------------------

organize_button = tk.Button(
    main_frame,
    text="Select Folder & Organize",
    font=("Segoe UI", 13, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#3b82f6",
    activeforeground="white",
    padx=28,
    pady=14,
    borderwidth=0,
    cursor="hand2",
    command=organize_files
)

organize_button.pack()

# ----------------------------
# BUTTON HOVER
# ----------------------------

def on_enter(e):
    organize_button.config(bg="#3b82f6")

def on_leave(e):
    organize_button.config(bg="#2563eb")

organize_button.bind("<Enter>", on_enter)
organize_button.bind("<Leave>", on_leave)

# ----------------------------
# INFO CARD
# ----------------------------

info_frame = tk.Frame(
    main_frame,
    bg="#111827",
    padx=20,
    pady=18
)

info_frame.pack(pady=35, fill="x")

info_label = tk.Label(
    info_frame,
    text=(
        "• Organizes images, videos and documents\n"
        "• Custom category selection\n"
        "• Creates folders automatically\n"
        "• Fast and lightweight automation"
    ),
    justify="left",
    font=("Segoe UI", 10),
    bg="#111827",
    fg="#cbd5e1"
)

info_label.pack(anchor="w")

# ----------------------------
# FOOTER
# ----------------------------

footer = tk.Label(
    root,
    text="Created by JeisonTech",
    font=("Segoe UI", 9),
    bg="#020617",
    fg="#64748b"
)

footer.pack(side="bottom", pady=18)

# ----------------------------
# START APP
# ----------------------------

root.mainloop()
