import tkinter as tk
from random import choice
from tkinter import PhotoImage

# Okno główne
root = tk.Tk()
root.title("Papier-Kamień-Nożyce")

paper_image = PhotoImage(file="paper.png")
rock_image = PhotoImage(file="rock.png")
scissors_image = PhotoImage(file="scissors.png")

# Mapowanie obrazów
choices_images = {
    'Papier': paper_image,
    'Kamień': rock_image,
    'Nożyce': scissors_image
}

# Funkcja gry
def play_game(user_choice):
    options = ['Papier', 'Kamień', 'Nożyce']
    computer_choice = choice(options)

    # Aktualizacja etykiet
    user_choice_image_label.config(image=choices_images[user_choice])
    computer_choice_image_label.config(image=choices_images[computer_choice])

    # Wynik
    if user_choice == computer_choice:
        result_text_label.config(text="Remis!", fg="black")
    elif (user_choice == 'Papier' and computer_choice == 'Kamień') or \
         (user_choice == 'Kamień' and computer_choice == 'Nożyce') or \
         (user_choice == 'Nożyce' and computer_choice == 'Papier'):
        result_text_label.config(text="Wygrałeś!", fg="#45B501")
    else:
        result_text_label.config(text="Przegrałeś!", fg="red")

# Ramka dla etykiet wyborów
labels_frame = tk.Frame(root)
labels_frame.pack(pady=(10, 100))

# Ramki
left_frame = tk.Frame(labels_frame)
left_frame.pack(side=tk.LEFT, padx=20)

center_frame = tk.Frame(labels_frame)
center_frame.pack(side=tk.LEFT, padx=20)

right_frame = tk.Frame(labels_frame)
right_frame.pack(side=tk.LEFT, padx=20)

# Ramka dla przycisków
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=20)

# Etykiety wyborów
user_choice_label = tk.Label(left_frame, text="Twój wybór:\n", font=("Helvetica", 14), width=20) # Stała szerokość
user_choice_label.pack()

computer_choice_label = tk.Label(right_frame, text="Wybór komputera:\n", font=("Helvetica", 14), width=20)
computer_choice_label.pack()

result_label = tk.Label(center_frame, text="Wynik:\n", font=("Helvetica", 14), width=20)
result_label.pack()

# Etykiety z obrazkami
user_choice_image_label = tk.Label(left_frame)
user_choice_image_label.pack(side=tk.BOTTOM)

computer_choice_image_label = tk.Label(right_frame)
computer_choice_image_label.pack(side=tk.BOTTOM)

# Etykieta z wynikiem
result_text_label = tk.Label(center_frame, text="", font=("Helvetica", 14))
result_text_label.pack(side=tk.BOTTOM)

# Przyciski
papier_button = tk.Button(button_frame, text="Papier", height=4, width=15, command=lambda: play_game('Papier'))
papier_button.pack(side=tk.LEFT, padx=15)

kamien_button = tk.Button(button_frame, text="Kamień", height=4, width=15, command=lambda: play_game('Kamień'))
kamien_button.pack(side=tk.LEFT, padx=15)

nozyce_button = tk.Button(button_frame, text="Nożyce", height=4, width=15, command=lambda: play_game('Nożyce'))
nozyce_button.pack(side=tk.LEFT, padx=15)

root.mainloop()
