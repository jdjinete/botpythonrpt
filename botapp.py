from selenium import webdriver
import time
import os, time


options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)

driver.get("https://web.whatsapp.com/")

time.sleep(20)

# celular  = "573203005638"

# mensaje = "Hola, mi primer BOT en Udemy"

# driver.get("https://wa.me/"+celular+"?text="+mensaje)

# time.sleep(5)


# # Enviar mensaje botón
# btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
# btn.click()
# time.sleep(5)

# #Botón ir a whatsapp web en link url
# btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
# btn.click()
# time.sleep(15)



#Botón para enviar mensaje.
#btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
#btn.click()



btn = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span")[0]
mensajesNuevos = int(btn.text)
if mensajesNuevos > 0:
        # Consultar primer item en chats
    btn = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div")[0]
    itemTop = btn.text.split("\n", 1)[0]

    print(itemTop)

    btn.click()
    time.sleep(5)

    # Obtener ultimo mensaje 
    ##btn = driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[12]/div/div/div/div[2]/div/span[1]")[0]
    ##btn = driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[37]/div/div/div/div[1]/div/span[1]/span")[0]
    btn = driver.find_elements_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[3]")[0]
    items = btn.text.split("\n")
    last_message = items[len(items)-2]
    if last_message == 'A qué horas ?':

        #Escribir mensaje
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

        btn.send_keys("Tamos melos")

        time.sleep(5)

        #Botón para enviar mensaje.
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
        btn.click()
    elif last_message == 'Hola Jinete':

         #Escribir mensaje
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

        btn.send_keys("¿Como estas?")

        time.sleep(5)

        #Botón para enviar mensaje.
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
        btn.click()


time.sleep(5)
print("valió verga")
driver.close()