esegui_python() {
    clear
    python -c "
import time
import ctypes
import random

# Codici per simulare la pressione di un tasto
VK_SPACE = 0x20  # Codice virtuale per la barra spaziatrice
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

# Funzione per simulare la pressione di un tasto
def simula_tasto():
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYDOWN, 0)  # Premere la barra spaziatrice
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)    # Rilasciare la barra spaziatrice

# Funzione per spostare il mouse da un punto A a un punto B e ritorno
def muovi_mouse():
    # Prendi la posizione attuale del mouse
    pos = ctypes.windll.user32.GetCursorPos
    x_start, y_start = pos()

    # Calcola una posizione casuale (x2, y2) per spostare il mouse
    x2 = x_start + random.randint(10, 100)  # movimento casuale a destra
    y2 = y_start + random.randint(10, 100)  # movimento casuale verso il basso

    # Muovi il mouse al punto (x2, y2)
    ctypes.windll.user32.SetCursorPos(x2, y2)
    
    # Aspetta un po' per simulare il movimento
    time.sleep(0.5)  # Pausa per visualizzare il movimento

    # Muovi il mouse di nuovo al punto originale
    ctypes.windll.user32.SetCursorPos(x_start, y_start)

# Funzione per prevenire la sospensione
def previeni_sospensione():
    while True:
        simula_tasto()  # Simula la pressione della barra spaziatrice
        muovi_mouse()   # Muove il mouse da una posizione a un'altra e poi torna
        time.sleep(30)   # Pausa di 30 secondi (puoi modificarla)

if __name__ == '__main__':
    print('\033[92malessandro_linux@DESKTOP-BV5VLUA\033[0m:\033[94m~\033[0m$ ', end='', flush=True)
    previeni_sospensione()
"
}

esegui_python
