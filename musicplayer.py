import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import ttk
from pygame import mixer
from tkinter.filedialog import askopenfilenames
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.geometry("450x350")
        master.resizable(False, False)

        mixer.init()
        self.playing_state = False

#-----------------------------------CREATION DE LA LISTBOX QUI AFFICHE LES SONS--------------------------------------------------------------------------#
        self.song_listbox = tk.Listbox(master,height=7, font="Helvetica 12 bold", bg='#dad7cd', selectmode=tk.SINGLE)
        self.song_listbox.pack(side="top", fill="both", padx=10, pady=10)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
        

#----------------------------------CREATION DU SLIDER DE VOLUME-----------------------------------------------------------------------------------------#
        self.volume_scale = ttk.Scale(master, from_=0, to=1, orient='horizontal', length=400, command=self.volume)
        self.volume_scale.set(0.5)
        self.volume_scale.place(x=25, y=260)
        volume_texte = tk.Label(master, text="Volume :")
        volume_texte.place(x=25, y=240)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------------CREATION DES BOUTONS ET LEURS POSITION--------------------------------------------------------------------------------#
        self.play_button = tk.Button(master, width=10, font=("Times", 15), text="▶", command=self.play)
        self.stop_button = tk.Button(master, width=10, font=("Times", 15), text="■", command=self.stop)
        self.pause_button = tk.Button(master, width=10, font=("Times", 15), text="⏸️", command=self.pause)
        self.boucle_button = tk.Button(master, width=10, font=("Times", 15), text="🔂", command=self.boucle)
        self.supprimer_button = tk.Button(master, width=10, font=("Times", 15), text="🗑️", command=self.supprimer_music)
        self.ajouter_button = tk.Button(master, width=10, font=("Times", 15), text="➕", command=self.ajouter_music)
        self.stop_button.place(x=30,y=200)
        self.play_button.place(x=165,y=200)
        self.pause_button.place(x=300,y=200)
        self.boucle_button.place(x=165,y=300)
        self.supprimer_button.place(x=300, y=300)
        self.ajouter_button.place(x=30, y=300)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#



#------------------------CREATION DU LABEL QUI SERVIRA A AFFICHER LE TITRE DE LA MUSIQUE EN COURS-------------------------------------------------------#
        self.titre_music = tk.Label(master, font="Helvetica 12 bold", text="Aucune musique en cours de lecture")
        self.titre_music.pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------------#



#-------------------------SERT A CHOISIR UN DOSSIER DE MUSIQUE-------------------------------------------------------------------------------------------#
        directory = askdirectory()
        os.chdir(directory)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#



#---------------------------REMPLI LA LIST DES MUSIQUES SELECTIONNEES-----------------------------------------------------------------------------------#
        liste_music = os.listdir()
        for item in liste_music:
            if item.endswith(".mp3"):
                self.song_listbox.insert(tk.END, item)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------LES FONCTIONS-----------------------------------------------------------------------------------#
    def supprimer_music(self):
        selection = self.song_listbox.curselection()
        if selection:
            index = selection[0]
            self.song_listbox.delete(index)
            self.titre_music.config(text="Aucune musique en cours de lecture")
        
    def ajouter_music(self):
        filetypes = (("Fichiers MP3", "*.mp3"), ("Tous les fichiers", "*.*"))
        new_songs = askopenfilenames(filetypes=filetypes)

        for song in new_songs:
            if song.endswith(".mp3"):
                filename = os.path.basename(song)
                self.song_listbox.insert(tk.END, filename)

    def volume(self, val):
        volume = float(val)
        mixer.music.set_volume(volume)

    def play(self):
        self.pause_button.config(text="⏸️")
        self.playing_state = True
        selected_song = self.song_listbox.get(tk.ACTIVE)
        self.titre_music.config(text=selected_song)
        mixer.music.load(selected_song)
        mixer.music.play()

    def stop(self):
        self.pause_button.config(text="⏸️")
        self.playing_state = False
        self.titre_music.config(text="Aucune musique en cours de lecture")
        mixer.music.stop()

    def pause(self):
        if self.playing_state:
            mixer.music.pause()
            self.playing_state = False
            self.pause_button.config(text="⏯️")
        else:
            mixer.music.unpause()
            self.playing_state = True
            self.pause_button.config(text="⏸️")

    def boucle(self):
        if self.playing_state:
            mixer.music.play(loops=-1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------#

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
