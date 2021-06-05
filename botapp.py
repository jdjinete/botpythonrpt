from selenium import webdriver
import time
import os, time
from selenium.webdriver.common.by import By
import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "private_key_rpt.json"

DIALOGFLOW_PROJECT_ID = "ecommerce-rpt"
DIALOG_LANGUAGE_CODE = "es"
SESSION_ID = "me"



options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-data-dir=C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
#pane-side
driver.get("https://web.whatsapp.com/")

def thereIsNewMessage(driver):
    #Pararse al comienzo de los mensajes.
    listChatsDiv = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div")[0]
    #Salta al comienzo
    listChatsDiv.location_once_scrolled_into_view
    if len(driver.find_elements(By.CLASS_NAME, "_38M1B")) > 0:
        return True
    else:
        contact = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div")[0]
        contact.click()
        chats = driver.find_elements_by_class_name("copyable-text")
        last_chat = chats[len(chats)-2]
        mensaje = last_chat.text
        if mensaje=='':
            return False
        items = last_chat.find_element_by_xpath("..").find_element_by_xpath("..").get_attribute("data-pre-plain-text").split("] ")
        items[len(items)-1]
        name_contact_send_last_message = items[len(items)-1].split(":")[0]
        if name_contact_send_last_message != "Regalo Para Ti":
            return True
        else:
            return False

def getLastMessageInChat():
    contact = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div")[0]
    contact.click()
    chat = driver.find_elements_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[3]")[0]
    items = chat.text.split("\n")

    #obtiene todos los mensajes del chat 
    #chats =driver.find_elements_by_class_name("copyable-text")
    #saca el ultimo chat
    #last_chat = chats[len(chats)-2]
    # mensaje = last_chat.text
    #obtiene quien envio el mensa
    # nt_by_xpath("..").find_element_by_xpath("..").get_attribute("data-pre-plain-text").split("] ").split(":")
    #items[len(items)-1]
    #nombre_contacto_que_envia = items[len(items)-1].split(":")[0]
    
    return items[len(items)-2]


time.sleep(20)

# if thereIsNewMessage(driver):
#         time.sleep(5)
#         last_message = getLastMessageInChat()
#         session_client = dialogflow.SessionsClient()
#         session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#         text_input = dialogflow.types.TextInput(text=last_message, language_code=DIALOG_LANGUAGE_CODE)
#         query_input = dialogflow.types.QueryInput(text=text_input)
#         try:
#             response = session_client.detect_intent(session=session, query_input=query_input)
#         except InvalidArgument:
#             raise

#         print("Query Text: ", response.query_result.query_text)
#         print("Detected intent: ", response.query_result.intent.display_name)
#         print("Detected intent confidence: ", response.query_result.intent_detection_confidence)
#         print("Fullfilment text: ", response.query_result.fulfillment_text)
#         print("Query Text: ", response.query_result.query_text)
#          #Escribir mensaje
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

#         btn.send_keys(response.query_result.fulfillment_text)

#         time.sleep(5)
#         #Botón para enviar mensaje.
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
#         btn.click()



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



#...................................................Para saber si hay un mensaje.
#len(driver.find_elements(By.CLASS_NAME, "_38M1B"))



#................................................... pararse al comienzo del chat


#btn.location_once_scrolled_into_view

#Pararse al comienzo de los mensajes.
# btn = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div")[0]
# #Salta al comienzo
# btn.location_once_scrolled_into_view

# btn = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div/div/div[2]/div[2]/div[2]/span[1]/div/span")[0]
# mensajesNuevos = int(btn.text)

while True:
    if thereIsNewMessage(driver):
        time.sleep(5)
        last_message = getLastMessageInChat()
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(text=last_message, language_code=DIALOG_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(session=session, query_input=query_input)
        except InvalidArgument:
            raise

        print("Query Text: ", response.query_result.query_text)
        print("Detected intent: ", response.query_result.intent.display_name)
        print("Detected intent confidence: ", response.query_result.intent_detection_confidence)
        print("Fullfilment text: ", response.query_result.fulfillment_text)
        print("Query Text: ", response.query_result.query_text)
         #Escribir mensaje
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

        btn.send_keys(response.query_result.fulfillment_text)

        time.sleep(5)
        #Botón para enviar mensaje.
        btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
        btn.click()







# if thereIsNewMessage(driver):
#     # Consultar primer item en chats
#     btn = driver.find_elements_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[11]/div/div")[0]
#     itemTop = btn.text.split("\n", 1)[0]

#     print(itemTop)

#     btn.click()
#     time.sleep(5)

#     # Obtener ultimo mensaje 
#     ##btn = driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[12]/div/div/div/div[2]/div/span[1]")[0]
#     ##btn = driver.find_elements_by_xpath("//*[@id='main']/div[3]/div/div/div[3]/div[37]/div/div/div/div[1]/div/span[1]/span")[0]
#     last_message = getLastMessageInChat()
#     if last_message == 'Clase pa que':

#         #Escribir mensaje
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

#         btn.send_keys("Tamos melos")

#         time.sleep(5)

#         #Botón para enviar mensaje.
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
#         btn.click()
#     elif last_message == 'Hola Jinete':

#          #Escribir mensaje
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")[0]

#         btn.send_keys("¿Como estas?")

#         time.sleep(5)

#         #Botón para enviar mensaje.
#         btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")[0]
#         btn.click()


time.sleep(5)
print("valió verga")
driver.close()
