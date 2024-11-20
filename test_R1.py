# Per wsl

esegui_python() {
    clear
    python -c "
import time
import ctypes
import random

# Definisce la struttura POINT
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

# Funzione per spostare il mouse da un punto A a un punto B e ritorno
def muovi_mouse():
    # Ottieni la posizione attuale del mouse
    pos = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pos))

    # Salva la posizione iniziale
    x_start, y_start = pos.x, pos.y

    # Calcola una posizione casuale (x2, y2) per spostare il mouse
    x2 = x_start + random.randint(10, 100)  # Movimento casuale a destra
    y2 = y_start + random.randint(10, 100)  # Movimento casuale verso il basso

    # Muove il mouse al punto (x2, y2)
    ctypes.windll.user32.SetCursorPos(x2, y2)
    
    # Aspetta un po' per simulare il movimento
    time.sleep(0.5)  # Pausa per visualizzare il movimento

    # Muove il mouse di nuovo al punto originale
    ctypes.windll.user32.SetCursorPos(x_start, y_start)

# Funzione per prevenire la sospensione
def previeni_sospensione():
    while True:
        muovi_mouse()   # Muove il mouse da una posizione a un'altra e poi torna
        time.sleep(60)   # Pausa di 60 secondi (puoi modificarla)

if __name__ == '__main__':
    print(r'PS C:\Users\Alessandro> ', end='', flush=True)
    previeni_sospensione()
"
}

esegui_python

# ----------------------------------------------------------------------------------------------------------

# Per powershell

function esegui_python {
    clear
    python -c "
import time
import ctypes
import random

# Definisce la struttura POINT
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

# Funzione per spostare il mouse da un punto A a un punto B e ritorno
def muovi_mouse():
    # Ottieni la posizione attuale del mouse
    pos = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pos))

    # Salva la posizione iniziale
    x_start, y_start = pos.x, pos.y

    # Calcola una posizione casuale (x2, y2) per spostare il mouse
    x2 = x_start + random.randint(10, 100)  # Movimento casuale a destra
    y2 = y_start + random.randint(10, 100)  # Movimento casuale verso il basso

    # Muove il mouse al punto (x2, y2)
    ctypes.windll.user32.SetCursorPos(x2, y2)
    
    # Aspetta un po' per simulare il movimento
    time.sleep(0.5)  # Pausa per visualizzare il movimento

    # Muove il mouse di nuovo al punto originale
    ctypes.windll.user32.SetCursorPos(x_start, y_start)

# Funzione per prevenire la sospensione
def previeni_sospensione():
    while True:
        muovi_mouse()   # Muove il mouse da una posizione a un'altra e poi torna
        time.sleep(60)   # Pausa di 60 secondi (puoi modificarla)

if __name__ == '__main__':
    print(r'PS C:\Users\Alessandro> ', end='', flush=True)
    previeni_sospensione()
"
}
esegui_python
