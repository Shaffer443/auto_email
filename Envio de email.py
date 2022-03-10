#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Automatizando Envio de Emails

Premissa incial de enviar emails de forma altomatica.

Configurado para o LINUX !

Fase 1:
    
    Manualmente:
        
        1.1 - Solicitar Quatidade de email(s)(Facultativo?)
        1.2 - Solicitar email(s)
        2.1 - Abrir Navegador alvo
        2.2 - Entrar na página para envio do email (ex: www.google.com.br)
        2.3 - Local para envio de email (clicks - local na página)
        3.1 - Preencher o destinatário
        3.2 - Preencher Assunto
        3.3 - Preencher Corpo do Email.
        3.4 - Anexar arquivo (currículo)
        4.1 - Envio do email.
        
    
    Automática (Busca das vagas e envio automático)


# In[2]:


# Intalações de bibliotecas pyautogui:

get_ipython().system('pip install pyautogui')


# In[5]:


# Intalações de bibliotecas selenium:

get_ipython().system('pip install -U selenium')


# In[7]:


# não achei a biblioteca time no pip feezer.
# observar, no caso de usada, se vai dar bugs

get_ipython().system('pip install time')


# # Importações de Bibliotecas:
# 
# import pyautogui
# import time
# import pyperclip
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# 
# # abrindo pelo OS:
# 
# pyautogui.PAUSE = 1
# 
# pyautogui.press('menu')
# pyautogui.write('chrome')
# pyautogui.press('enter')
# 
# 
# 
# #navegadorgoogle = webdriver.Chrome()
# #navegador.get("https://www.google.com/") # abrindo sem digitar a página no navegador aberto.

# In[ ]:


# Importações de Bibliotecas:

import pyautogui
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# In[34]:


# Fase 1 - Navegador: Caminho 2:

navegadorgoogle = webdriver.Chrome()
navegadorgoogle.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox") 
navegadorgoogle.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("rafalegouveiamelo@gmail.com")
# navegadorgoogle.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]').send_keys(Keys.ENTER)

# OBS: Automação com o login do google o protege de logar em contas. Logo, não conseguimos entrar no email por este caminho.


# In[41]:


# pegar posição:
time.sleep(10)
pyautogui.position()


# In[42]:


# abrindo pelo OS:

pyautogui.PAUSE = 1

# fase 1 - abrir navegador Google:

pyautogui.click(x=27, y=880)
time.sleep(2)
pyautogui.write('Google chrome')
pyautogui.press('enter')

# fase 2 - Entrar no Web Mail:

time.sleep(2)
pyautogui.click(x=707, y=538)
time.sleep(2)
pyautogui.click(x=1243, y=104)

# fase 3 - abrir novo email:

time.sleep(2)
pyautogui.click(x=85, y=180)


# In[ ]:




