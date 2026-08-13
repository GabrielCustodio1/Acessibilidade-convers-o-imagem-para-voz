import pyautogui

pyautogui.FAILSAFE = True #Cursor no canto superior esquerdo para pausar a execução
pyautogui.PAUSE = 1.5 #Delay para cada comando do pyautogui

#Abrir o navegador Microsoft Edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#Acessar e fazer login no site da Azure Vision
pyautogui.write("https://portal.vision.cognitive.azure.com/demo/image-captioning")
pyautogui.press("enter")
pyautogui.moveTo(1882, 93)
pyautogui.click()
pyautogui.write("{seu email}")
pyautogui.press("enter")

#Enviar a imagem que será analisada e copiar o output
pyautogui.moveTo(248, 561)
pyautogui.click()
pyautogui.moveTo(207, 49)
pyautogui.write("C:/Users/Pichau/Documents/Projetos/projeto_acess/Imagens")
pyautogui.moveTo(239, 158)
pyautogui.click()
pyautogui.press("enter")
pyautogui.moveTo(1056, 915)
pyautogui.click(clicks=3)
pyautogui.hotkey("ctrl", "c")

#Acessar o recurso que converte texto para falas e executá-lo
pyautogui.moveTo(298, 19)
pyautogui.write("https://ai.azure.com/nextgen")
pyautogui.press("enter")
pyautogui.moveTo(890, 104)
pyautogui.write("Azure-Speech-text-to-speech")
pyautogui.moveTo(862, 232)
pyautogui.click()
pyautogui.moveTo(1518, 170)
pyautogui.click()
pyautogui.moveTo(815, 856)
pyautogui.click(clicks=3)
pyautogui.hotkey("ctrl", "v")
pyautogui.moveTo(709, 308)
pyautogui.click()