esegui_python() {
    clear
    python -c "
import time

def previeni_sospensione():
    while True:
        time.sleep(30)

if __name__ == '__main__':
    print('\033[92malessandro_linux@DESKTOP-BV5VLUA\033[0m:\033[94m~\033[0m$ ', end='', flush=True)
    previeni_sospensione()
"
}

esegui_python
