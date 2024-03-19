
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random 
import pygame

pygame.mixer.init()


class Aplicacion:
    def __init__(self):
        # Ventana principal
        self.window = tk.Tk()
        self.window.title('Juego concéntrate')
        self.window.geometry("520x400")
        self.window.resizable(False, False)
        self.window.config(background='#1f1e30')
        # errores a la hora de hacer match
        self.num_errores = 0
        self.label_errores = tk.Label(self.window, text=f'Errores : {self.num_errores}', font=("Helvetica", 16), width=9, padx=5)
        self.label_errores.grid(row=0,column=0)
        self.label_errores.config(background='white')
        #contar clicks
        self.count = 0
        #contar coincidencias
        self.counter_match = 0
        #Background botones 
        self.standar_background = '#575769'
        self.valor_boton = 0
        self.botones = []
        self.values_couple_buttons = []
        #Marco inferior
        self.botton_frame = ttk.Frame(self.window)
        self.botton_frame.grid(row=5, column=0, columnspan=4, pady=12)
        
        self.create_buttons()
            
        self.hide_buttons = tk.Button(self.botton_frame, text='Ocultar botones', borderwidth=0, relief='flat')
        self.hide_buttons.config(command=self.ocultar_botones, 
                                 width=12,height=2,
                                 background='#ff9703', foreground='white',
                                 activebackground='#ff9703',
                                 activeforeground='white',
                                 cursor="hand1")
        self.hide_buttons.pack(side="bottom")
        self.window.mainloop()
    
    
    
    def create_buttons(self):
        valor_botones = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
        # ya se ha jugado la primera vez
        if len(self.botones) == 16:
            self.botones = []
                
                
        for i in range(1, 17):
            self.valor_boton = valor_botones.pop(random.randrange(len(valor_botones))) 
            if i <= 4:
                self.row_button = 1
                self.colum_buttom = i - 1
            elif i <= 8:
                self.row_button = 2
                self.colum_buttom = i - 5
            elif i <= 12:
                self.row_button = 3
                self.colum_buttom = i - 9
            else:
                self.row_button = 4
                self.colum_buttom = i - 13
    
            self.boton = tk.Button(self.window, text=self.valor_boton, height=3, width=12, borderwidth=0, relief='flat')
            self.boton.grid(column=self.colum_buttom, row=self.row_button, padx=3, pady=3)
            self.boton.config(command=lambda btn=self.boton: self.validate_click_button(btn), 
                              state='disabled',
                              background=self.standar_background, 
                              foreground='white', 
                              disabledforeground="white",
                              )
            self.botones.append(self.boton)
     
    
       
    def ocultar_botones(self):
        for boton in self.botones:
            boton.config(background=self.standar_background, foreground=self.standar_background, activebackground=self.standar_background, activeforeground=self.standar_background, state='normal')
        self.hide_buttons.config(state='disabled')
    
    
    def validate_click_button(self, button):
        self.count += 1
        button.config(background='white', foreground='black',disabledforeground='black', state='disabled')
        self.values_couple_buttons.append(button)
        pygame.mixer.music.load("sounds/click-card.mp3")
        pygame.mixer.music.play(loops=0)
        if self.count > 1:
            self.window.after(700, self.check_match_buttons, self.values_couple_buttons)
            self.count = 0
            self.values_couple_buttons = []
            
            
    
    def check_match_buttons(self, buttons):
        value_first_button = buttons[0].cget('text')
        value_second_button = buttons[1].cget('text')
        
        if value_first_button == value_second_button:
            buttons[0].config(background='#307a5f', disabledforeground='white', state='disabled')
            buttons[1].config(background='#307a5f', disabledforeground='white', state='disabled')
            self.counter_match += 1
            pygame.mixer.music.load("sounds/match.mp3")
            pygame.mixer.music.play(loops=0)
        else:                                                                                                                                              
            buttons[0].config(background=self.standar_background, foreground=self.standar_background, state='normal')
            buttons[1].config(background=self.standar_background, foreground=self.standar_background, state='normal')
            self.num_errores += 1
            self.update_label_errors() 
                    
        if self.counter_match == 8:
            self.num_errores = 0
            nuew_game = messagebox.askyesno("Juego terminado", "¿Quieres jugar de nuevo?")
            if nuew_game:
                self.new_game()
            else:
                messagebox.showinfo("Juego terminado", "Muchas gracias por jugar")

    
    def new_game(self):
        self.create_buttons()
        self.counter_match = 0
        self.hide_buttons.config(state='normal')
        self.label_errores.config(text=f'Errores : {0}') 
        
        
    
    def update_label_errors(self):
        self.label_errores.config(text=f'Errores : {self.num_errores}') 
    
    
    
aplicacion = Aplicacion()
