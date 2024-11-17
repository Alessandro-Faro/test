function esegui_python {
    clear
    python -c "
import time
import ctypes

# Codici per simulare la pressione della barra spaziatrice
VK_SPACE = 0x20
KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002

# Funzione per simulare la pressione di un tasto
def simula_tasto():
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYDOWN, 0)  # Premere la barra spaziatrice
    ctypes.windll.user32.keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)    # Rilasciare la barra spaziatrice

# Funzione per prevenire la sospensione
def previeni_sospensione():
    while True:
        # Simula la pressione della barra spaziatrice
        simula_tasto()  # Premere e rilasciare la barra spaziatrice
        
        time.sleep(30)  # Pausa di 30 secondi

if __name__ == '__main__':
    print(r'PS C:\Users\Alessandro> ', end='', flush=True)
    previeni_sospensione()
"
}
esegui_python