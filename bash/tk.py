# -- coding: utf-8 --

import os
from PIL import Image, ImageTk
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import google.generativeai as genai  #GEMINI-1 
from gtts import gTTS  #Texto a audio
from rich.console import Console #HTMLtexto consola
from rich.syntax import Syntax
import time


from io import BytesIO #almacenar img, audio 
import keyboard
import pygame
import pygame.camera
import re
import datetime


from docx import Document
import html2text 
import uuid

import subprocess
import glob
import datetime
import shutil


class CameraApp: 

        
    def hablar(self,texto):
        # Generar el archivo de audio usando gTTS y BytesIO
        print(texto)
        with BytesIO() as f:
            tts = gTTS(text=texto, lang='es', slow= False)
            tts.write_to_fp(f)
            f.seek(0)
            
            # Reproducir el audio usando pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load(f)
            pygame.mixer.music.play()
            
            # Esperar hasta que termine de reproducirse el audio
            while pygame.mixer.music.get_busy():
                if keyboard.is_pressed('Enter'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1)
                        break
                continue
                
    def reproducir_audiores(self,texto):
        # Generar el archivo de audio usando gTTS y BytesIO
        print(texto)
        with BytesIO() as f:
            tts = gTTS(text=texto, lang='es', slow= False)
            tts.write_to_fp(f)
            f.seek(0)
            
            # Reproducir el audio usando pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load(f)
            pygame.mixer.music.play()
            
            # Esperar hasta que termine de reproducirse el audio
            while pygame.mixer.music.get_busy():
                
                continue

    def desconexion_audio(self):
        # Inicializar pygame
        pygame.init()

        try:
            # Iniciar la reproducción del audio
            pygame.mixer.music.load("desconexion.mpeg")
            pygame.mixer.music.play()

            # Esperar hasta que el audio termine de reproducirse
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print("Error al reproducir el audio:", e)
        finally:
            # Detener pygame
            pygame.quit()

    def html_to_docx(self,text):
                # Carpeta donde se guardarán los documentos
                folder_path = "respuestas"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Nombre base del archivo
                base_name = "unl-text"

                # Extensión del archivo
                file_extension = ".docx"

                # Verificar si el archivo ya existe
                counter = 1
                output_path = os.path.join(folder_path, "unl-text"+str(counter)+".docx")

                while os.path.exists(output_path):
                    # Si el archivo ya existe, incrementar el contador y probar con un nuevo nombre
                    counter += 1
                    output_path = os.path.join(folder_path, "unl-text"+str(counter)+".docx")


                # Crear un nuevo documento de Word
                doc = Document()
                text_content = html2text.html2text(text)
                doc.add_paragraph(text_content)
                doc.save(output_path)
                print('Documento Word guardado en:'+ str(output_path))
 
#https://gtts.readthedocs.io/en/latest/cli.html
    def reproducir_audio(self,texto):
        try:
            with BytesIO() as f:
                tts = gTTS(text=texto, lang='es')
                tts.write_to_fp(f)
                f.seek(0) 
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    if keyboard.is_pressed('0'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1)
                        self.desconexion_audio()
                        break
                    
                    if keyboard.is_pressed('+'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos + 1) #adelantar un segundo 
                        
                    if keyboard.is_pressed('-'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos - 1) #adelantar un segundo 
                        
                    # Detectar si se ha pulsado la tecla "Enter"
                    pausado = False
                    if pausado == False:
                        #print("Esperando el . para pause")
                        if keyboard.is_pressed('Enter'):
                            pausado = True
                            pygame.mixer.music.pause()
                            #time.sleep(0.1)
                            print("pause")
                        elif keyboard.is_pressed('0'):
                            pygame.mixer.music.stop()
                            time.sleep(0.1) 
                            break 
                        while pausado == True:
                                print("Esperando el . para play")
                                if keyboard.is_pressed('Enter'):
                                    pausado==False 
                                    pygame.mixer.music.unpause()
                                    #time.sleep(0.1)
                                    print("Play") 
                                    break
                                elif keyboard.is_pressed('0'):
                                    pygame.mixer.music.stop()
                                    break
                    continue    

        except Exception as e:
            print("reproducir_audio(); GTTS ERROR - - ERROR - - ERROR   GTTS")
            print('{type(e).__name__}: '+ str(e))     

 


#https://gtts.readthedocs.io/en/latest/cli.html
    def reproducir_audio_y_guardar_audio(self,texto): 
        try:
            with BytesIO() as f:
                tts = gTTS(text=texto, lang='es')
                # Obtener la fecha y hora actual
                now = datetime.datetime.now()

                # Carpeta donde se guardarán los audios 
                folder_path = "respuestas"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # Nombre base del archivo
                base_name = "res-audio"

                # Extensión del archivo
                file_extension = ".mp3" 

      
                nombre_audio = "respuestas/unl-audio"+str(uuid.uuid4()) + ".mp3"


                tts.save(nombre_audio) 
                shutil.copy(nombre_audio, "/media/unl/KINGSTON/") 
                print("."+ "procediendo a escribir el archivo de audio")
                tts.write_to_fp(f)
                f.seek(0)
                
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    if keyboard.is_pressed('Enter'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1)
                        break
                    
                    if keyboard.is_pressed('+'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos + 1) #adelantar un segundo 
                        
                    if keyboard.is_pressed('-'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos - 1) #adelantar un segundo 
                        
                    # Detectar si se ha pulsado la tecla "."
                    pausado = False
                    if pausado == False:
                        #print("Esperando el . para pause")
                        if keyboard.is_pressed('.'):
                            pausado = True
                            pygame.mixer.music.pause()
                            #time.sleep(0.1)
                            print("pause")
                        elif keyboard.is_pressed('Enter'):
                            pygame.mixer.music.stop()
                            time.sleep(0.1)
                            break 
                        while pausado == True:
                                print("Esperando el . para play")
                                if keyboard.is_pressed('.'):
                                    pausado==False 
                                    pygame.mixer.music.unpause()
                                    #time.sleep(0.1)
                                    print("Play") 
                                    break
                                elif keyboard.is_pressed('Enter'):
                                    pygame.mixer.music.stop()
                                    break
                    continue   
                    
        except Exception as e:
            print("reproducir_audio(); GTTS ERROR - - ERROR - - ERROR   GTTS")
            print('{type(e).__name__}: ', +str(e))     


    def gemini_unl(self, mensaje):
                foto, path =self.tomarFoto() 
                os.remove(path)  
                print(" mensaje ",mensaje)  
                print(" foto ",foto)    
                model = genai.GenerativeModel('gemini-pro-vision')  
                # Seguridad https://ai.google.dev/docs/safety_setting_gemini?hl=es-419

                safety_settings = {
                    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
                    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE"} 
                try:
                    response = model.generate_content([mensaje, foto], safety_settings=safety_settings)
                    #time.sleep(1)  
                    #time.sleep(1)  
                    response.resolve() 
                    print(response)  
                    if response.candidates[0].content.parts: #Pa ver si hay más de una respuesta:
                        try: 
                            respuesta= response.candidates[0].content.parts[0].text   
                            respuesta= self.to_plain_string(respuesta) 
                            #Devolviendo respuesta
                            print(respuesta) 
                            return(respuesta)  
                        
                        except Exception as e:
                            print("Entró al Primer CATCH, ERROR - - ERROR - - ERROR")
                            print('f{type(e).__name__}: ',{e})     
                            try:  # Si solo hay una respuesta: 
                                print("!!!!!!!!!!!!!!!")
                                a=response.text    
                                respuestab=self.to_plain_string(a)
                                #Devolviendo respuesta
                                return(respuestab)  

                            except Exception as e:
                                print("Entró al segundo CATCH, ERROR - - ERROR - - ERROR")
                                self.hablar("No se pudo generar una respuesta")
                                print('{type(e).__name__}: '+{e})     

                    else: # Si solo hay una respuesta:
                        try:  
                            print("Parece que solo hay una respuesta. :)")
                            print("!!!!!!!!!!!!!!!")
                            a=response.text   
                            print("response.text")
                            respuesta=self.to_plain_string(respuesta)  
                            #Devolviendo respuesta
                            return(respuesta)  

                        except Exception as e:
                            print("Entró al segundo CATCH, del Else")
                            print('{type(e).__name__}: '+{e})     
                            try:  # Si solo hay una respuesta:
                                print("Parece que solo hay una respuesta. :)")  
                                respuesta= response.candidates[0].content.parts[0].text 
                                #Devolviendo respuesta
                                return(respuesta)  

                            except Exception as e:
                                print("ERROR - - ERROR")
                                self.desconexion_audio()
                                print('f{type(e).__name__}: ',+str(e))     
                    
                except Exception as e:
                    print("No se pudo generar una respuesta")
                    #self.hablarGTTS("No se pudo generar una respuesta")
                    print('f{type(e).__name__}: ',{e})    
                
    
 
 

    def gemini(self, prompt):     
                prompt=prompt
                print("Ejecutar sin guardar")
                
                try:  
                    res = self.gemini_unl(prompt) 
                    #REPRODUCIR 
                    self.reproducir_audio(res) 
                    self.desconexion_audio()

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.desconexion_audio()
                    print('{type(e).__name__}: '+str(e))  

 
 

    def gemini_savetext(self, prompt):     
                prompt=prompt
                print("Ejecutar y guardar texto")
                
                try:  
                    res = self.gemini_unl(prompt) 
                    #REPRODUCIR Y GUARDAR TEXTO
                    self.reproducir_audio(res) 
                    self.html_to_docx(res) 
                    self.desconexion_audio()

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.desconexion_audio()
                    print('{type(e).__name__}: '+str(e))  



    def gemini_saveaudio(self, prompt):     
                print("Ejecutar y guardar audio")
                prompt=prompt
                res = self.gemini_unl(prompt) 
                print("Ejecutar y guardar audio")
                try:  
                    #REPRODUCIR Y GUARDAR EL AUDIO 
                    self.reproducir_audio_y_guardar_audio(res)
                    self.desconexion_audio()

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.desconexion_audio()
                    print('{type(e).__name__}: '+str(e))





    def gemini_savetextandaudio(self, prompt):     
                print("Ejecutar y guardar audio")
                prompt=prompt
                res = self.gemini_unl(prompt) 
                print("Ejecutar y guardar audio")
                try:  
                    #REPRODUCIR Y GUARDAR EL AUDIO 
                    self.reproducir_audio_y_guardar_audio(res)
                    self.html_to_docx(res) 
                    self.desconexion_audio()

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.desconexion_audio()
                    print('{type(e).__name__}: '+str(e))




    def to_plain_string(self,text):
        # Eliminar caracteres especiales excepto letras, números y tildes
        cleaned_text = re.sub(r'[^\w\sáéíóúÁÉÍÓÚ.,;:?!¡¿%]', '', text)
        return cleaned_text 

    def contiene_palabra(self, cadena, palabra):
        # Verificar si la cadena no es None antes de intentar la comparación
        if cadena is not None:
            cadena = cadena.lower()  # Convertir la cadena a minúsculas
            palabra = palabra.lower()  # Convertir la palabra a minúsculas
            return palabra in cadena
        else:
            return False   

    def cerrar_ventana(self, event):
        self.master.destroy() 
    lento=False

    def __init__(self, window, window_title):  
            
            #GEMINI-2                       AQUI Tu KEY DE GOOGLE      
            #GOOGLE_API_KEY='AIzaSyAa1jzaUezK-Z3eOL4EuHkoiCslkySb-lo' llave de cuenta 2 
            GOOGLE_API_KEY='AIzaSyCI5hk_LHr8V49BjaI4pm6BxpZBwJplxII'
            genai.configure(api_key=GOOGLE_API_KEY) 
            self.window = window
            self.window.title(window_title)
                
                # Obtener el tamaño de la pantalla principal
            ancho_pantalla = self.window.winfo_screenwidth()
            alto_pantalla = self.window.winfo_screenheight()

            # Centrar la ventana de chat
            # ancho_ventana_chat = 600  
            # alto_ventana_chat = 300
            x = (ancho_pantalla - ancho_pantalla) // 2
            y = (alto_pantalla - alto_pantalla) // 2
            #TAMAÑO
            self.window.geometry('{}x{}+{}+{}'.format(ancho_pantalla, alto_pantalla, x, y))

            self.window.configure(bg='#000000')  #Color d fondo
            #Cámara por defecto de la PC
            self.vid = cv2.VideoCapture(1)
          
            #Solucion NVIDIA
            #self.vid = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw (memoria: NVMM), width=(int)1280, height=(int)720,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! appsink")
            self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.canvas.pack() 
            # Mover la imagen a la izquierda (coordenadas x=0)
            self.canvas.place(x=0, y=60) 
                # Ruta de la imagen que deseas mostrar
            image_path = ImageTk.PhotoImage(file="img.jpeg")
 
            self.photo = image_path

            # Crear un widget Label para mostrar la imagen
            self.image_label = tk.Label(window, image=self.photo)
            self.image_label.pack()

            # Mover la imagen a la izquierda (coordenadas x=0)
            self.image_label.place(x=650, y=90) 


            self.delay = 10
            self.update()
            
  
## COMANDS  >>> 
            self.window.bind('<Escape>', lambda e: self.exit()) 
            self.window.bind('1', lambda e: self.gemini("extrae el texto que encuentres")) 
            self.window.bind('2', lambda e: self.gemini_saveaudio("describe detalladamente la imagen")) 
            self.window.bind('3', lambda e: self.gemini_savetexto("describe detalladamente la imagen")) 
            self.window.bind('9', lambda e: self.gemini_savetextandaudio("Extrae todo el texto que detectes en la imagen.")) 
            self.window.mainloop()

## COMANDS <<< 
            

            
    def tomarFoto(self):
        self.subprocess()
        # Busca todos los archivos JPG en el directorio
        archivos_jpg = glob.glob(os.path.join(".", "*.jpg"))

        # Ordena los archivos por fecha de creación
        archivos_jpg.sort(key=os.path.getmtime)
        
        # Obtiene el último archivo creado
        ultimo_archivo_jpg = archivos_jpg[-1]
        
        # Abre el último archivo JPG
        imagen = Image.open(ultimo_archivo_jpg)  
        
        #os.remove(ultimo_archivo_jpg)
         
        return (imagen,ultimo_archivo_jpg) 
           
            
    def tomarFoto3(self):
        ret, frame = self.vid.read()
        if ret:
            retval, buffer = cv2.imencode('.jpg', frame)
            img_bytes = BytesIO(buffer.tobytes())
            img_pil = Image.open(img_bytes) 
            return img_pil
        else:
            print("Error al capturar la foto.")
           
    def subprocess(self):
        subprocess.run(["nvgstcapture-1.0 --automate --capture-auto"], shell=True, capture_output=False, text=False) 
            
    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)
        
    def exit(self):
        if self.vid.isOpened():
            self.vid.release()
        self.window.destroy()

App = CameraApp(tk.Tk(), "Gemini + Azure Cognitive Services")
