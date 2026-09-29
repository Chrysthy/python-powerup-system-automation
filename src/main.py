import os
import pyautogui
import time
import pandas as pd

from pathlib import Path
from config import SYSTEM_URL
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produtos.csv"

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write(SYSTEM_URL)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=674, y=447)
pyautogui.write(os.getenv("EMAIL"))
pyautogui.press("tab")
pyautogui.write(os.getenv("PASSWORD"))
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(4)

tabela = pd.read_csv(DATA_FILE)

for linha in tabela.index:

    pyautogui.click(x=653, y=294)
  
    codigo = tabela.loc[linha, "codigo"]   
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter") 

    pyautogui.scroll(5000)