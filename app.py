import pyautogui
import webbrowser
from time import sleep
def open_instagram(site):
    webbrowser.open(site)
def find_last_post():
    pyautogui.click(753,698,duration=1)
def find_and_insert_username_password(username, password):
    # Encontra a posição do username e da password
    usernameLocate = pyautogui.locateCenterOnScreen('./image/username.png')
    passwordLocate = pyautogui.locateCenterOnScreen('./image/password.png')
    # Digita o valor de ambos no campo respectivo
    pyautogui.click(usernameLocate[0], usernameLocate[1], duration=2)
    pyautogui.typewrite(username)

    pyautogui.click(passwordLocate[0], passwordLocate[1], duration=1)
    pyautogui.typewrite(password)
    # Entra com o usuario e senha passados
    sleep(1)
    entrarLocate = pyautogui.locateCenterOnScreen('./image/login.png')
    pyautogui.click(entrarLocate[0], entrarLocate[1], duration=1)
def Refuse_to_save_login_information():
    # Confere se apareceu um popo up pedindo para salvar as informações
    try:
        entrarLocate = pyautogui.locateCenterOnScreen('./image/not_now.png')
        pyautogui.click(entrarLocate[0], entrarLocate[1], duration=1)
    except pyautogui.ImageNotFoundException:
        pass
def like_post():
    try: 
        likeLocate = pyautogui.locateCenterOnScreen('./image/hearth.png')
        pyautogui.click(likeLocate[0], likeLocate[1])
    except:
        pass
def comment_post():
    commentLocate = pyautogui.locateCenterOnScreen('./image/comment.png')
    pyautogui.click(commentLocate[0], commentLocate[1],duration=1)
    sleep(1)
    pyautogui.typewrite('Gostei')
    pyautogui.press('enter')
def close_post():
    closeLocate = pyautogui.locateCenterOnScreen('./image/close.png')
    pyautogui.click(closeLocate[0], closeLocate[1], duration=2)
while True:
    open_instagram('https://www.instagram.com/nike/')
    sleep(4)
    find_last_post()
    sleep(3)
    find_and_insert_username_password('usuario', 'senha')
    sleep(6)
    Refuse_to_save_login_information()
    sleep(2)
    find_last_post()
    sleep(2)
    like_post()
    comment_post()
    sleep(1)
    close_post()
    # Aguarda 24 horas antes de repetir o processo
    sleep(86400)
    