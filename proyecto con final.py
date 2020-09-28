#Autor: Juan Manuel Torrijos González A01706428
#Algoritmo:
#El programa mostrará una interfaz gráfica que le mostrará unas preguntas de examen al usuario para que este las conteste
#y luego pueda ver sus resultados, tendrá tres intento para hacer el examen si es que quiere repetirlo, una vez terminados los
#intentos o que ya no quiera seguir, se le mostrará una ventana con su promedio, nivel y las respuestas correctas, todo esto
#estará en la interfaz que se le mostrará al usuario
#1. Iniciar el examen
#2. El usuario introduce sus respuestas
#3. se muestra si están bien o mal
#4. si el usuario quiere y tiene mas intentos se repite el examen
#5. sino se muestran los resultados finales
#6. fin del programa

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

#===Propiedades de la ventana y botones================================================================================================
# Esta función crea la ventana principal de la interfaz junto con sus botones y demás widgets
def interfaz():
    global ventana
    global texam
    ventana = Tk()
    ventana.geometry('700x550') # anchura x altura
    ventana.configure(bg = 'darkslateblue')
    ventana.resizable(width=False,height=False)
    ventana.title('Examen Diagnóstico')
    Label (ventana,text="Examen Diagnóstico\nInstrucciones:\nContesta las preguntas, usa 3 decimales de ser necesario\nConsidera PI=3.1416",
                     font=("Cooper Black",12),fg="#000000",bg="#3333FF").place(x=120,y=5)  #crear etiqueta de instrucciones
    texam = Text(ventana, width=85, height=25)
    texam.place(x=10,y=100)
    texam.configure(bg = 'darkslateblue')
    bIniciar = ttk.Button(ventana, text='Iniciar', 
                            command=pregunta)
    bIniciar.place(x=620,y=520)
    
    bsalir = ttk.Button(ventana, text='Salir', command=ventana.destroy)
    bsalir.place(x=5,y=520)
    
    ventana.mainloop()
    
#===Funcion para mostrar las preguntas===================================================================================
#Muestra las preguntas y los espacios para las entradas(respuestas) y cambia el botón
def pregunta():
    global preg1
    global resp1
    preg1 = "Pregunta 1:\n -Calcula el área de un triangulo con altura 3 y base 5\n\n\n"
    resp1 = StringVar()
    ttk.Entry(ventana,textvariable=resp1).place(x=20,y=135)
    
    global preg2
    global resp2
    preg2 = "Pregunta 2:\n -¿Cual es el volumen de un prisma rectangular con medidas L=8, A=5, y H=13? 5\n\n\n"
    resp2 = StringVar()
    ttk.Entry(ventana,textvariable=resp2).place(x=20,y=200)
    
    global preg3
    global resp3
    preg3 = "Pregunta 3:\n -Calcula el área de un círculo con diametro 6"
    resp3 = StringVar()
    ttk.Entry(ventana,textvariable=resp3).place(x=20,y=265)
    
    global preg4
    global resp4
    preg4 = "\n\n\nPregunta 4:\n -¿Cual es el volumen de un cilindro con radio 2 y altura 35?"
    resp4 = StringVar()
    ttk.Entry(ventana,textvariable=resp4).place(x=20,y=330)
    
    global preg5
    global resp5
    preg5 = "\n\n\nPregunta 5:\n -Calcula el volumen de un cono con radio 3 y altura 15"
    resp5 = StringVar()
    ttk.Entry(ventana,textvariable=resp5).place(x=20,y=395)
    
    global preg6
    global resp6
    preg6 = "\n\n\nPregunta 6:\n -¿Cual es la unidad fundamental de la vida?(Pregunta de regalo)"
    resp6 = StringVar()
    ttk.Entry(ventana,textvariable=resp6).place(x=20,y=455)
    
    texam.insert("1.0", preg1,resp1,preg2,resp2,preg3,resp3,preg4,
                      resp4,preg5,resp5,preg6,resp6)
    bEnviar = ttk.Button(ventana, text='Enviar',command=calificar).place(x=620,y=520)
    
#===Función para calificar las preguntas==========================================================
#Compara las respuestas dadas con las correctas para mostrar in "correcto" o "incorrecto", agrega esto al archivo con el
#historial y cambia el botón otra vez
def calificar():
    global buenas
    global hist
    #global intento
    
    buenas = 0
    if intento == 1:
        hist = open("historialP.txt","w+")
    else:
        hist = open("historialP.txt","a+")
    
    hist.write("\n -Intento " + str(intento))
    if resp1.get() == "7.5":
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=135)
        buenas += 1
        hist.write("\r\nCorrecto")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=135)
        hist.write("\r\nIncorrecto")
    
    if resp2.get() == "520":
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=200)
        buenas += 1
        hist.write("\r\nCorrecto")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=200)
        hist.write("\r\nIncorrecto")
    
    if resp3.get() == '28.274':
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=265)
        buenas += 1
        hist.write("\r\nCorrecto")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=265)
        hist.write("\r\nIncorrecto")
        
    if resp4.get() == '439.824':
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=330)
        buenas += 1
        hist.write("\r\nCorrecto")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=330)
        hist.write("\r\nIncorrecto")
    
    if resp5.get() == '141.372':
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=395)
        buenas += 1
        hist.write("\r\nCorrecto")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=395)
        hist.write("\r\nIncorrecto")
    
    if resp6.get() == "celula" or resp6.get() == "Celula":
        Label(ventana,text="Correcto",font=("Algerian",20),fg="GREEN").place(x=400,y=460)
        buenas += 1
        hist.write("\r\nCorrecto\n")
    else:
        Label(ventana,text="Incorrecto",font=("Algerian",20),fg="RED").place(x=400,y=460)
        hist.write("\r\nIncorrecto\n")
    hist.close()
    
    bFin = ttk.Button(ventana, text='Resultados',command=resultados).place(x=620,y=520)

#===Función que muestra los resultados============================================================
#abre otra ventana que muestra el historial, las preguntas que contestó correctamente y da la opción de repetir el examen
def resultados ():
    ventana.withdraw()
    global resul, bRepetir
    hist = open("HistorialP.txt",'r')
    resul = Toplevel()
    resul.geometry('700x550') # anchura x altura

    resul.configure(bg = 'darkslateblue')
    resul.resizable(width=False,height=False)
    resul.title('Resultados')
    Label (resul,text="Resultados\nA continuación se te presentan los resultados \nobtenidos en este intento del examen",
                     font=("Britannic Bold",15),fg="BLACK",bg="#3333FF").place(x=120,y=5)  #crear etiqueta de instrucciones
    tResul = Text(resul, width=85, height=25)
    tResul.place(x=10,y=100)
    tResul.configure(bg = 'darkslateblue')
    
    histo = hist.read()
    tResul.insert("1.0", histo)
    resultados ="Respuestas correctas: " + str(buenas) + "\nHistorial:"
    tResul.insert("1.0", resultados)
    
    Label (resul, text = "Aún te quedan " + str(3-intento) + " intentos", font=("Brittanic Bold",13)
           ,fg="BLACK",bg="#3333FF").pack(side=BOTTOM)
    
    bsalir = ttk.Button(resul, text='Salir', command=final)
    bsalir.place(x=5,y=520)
    
    if intento > 2:
        bRepetir = ttk.Button(resul, text = "Finalizar" ,command=final).pack(side = BOTTOM)
    else:
        bRepetir = ttk.Button(resul, text = "Repetir Examen" ,command=repetir).pack(side = BOTTOM)

#===Función para volver a hacer el examen según los intentos restantes==========================
#Evalua si aun quedan intentos para repetir el examen
def repetir():
    global intento
    intento += 1
    if intento > 3:
        ventana.destroy()
        
    else:
        ventana.destroy()
        interfaz()

#===Función que muestra el nivel, consejo y respuestas correctas================================
#despliega otra ventana con los resultados finales, promedio, respuestas correctas, etc.
def final():
    RespCorr=["1- 7.5","2- 520","3- 28.274","4- 439.824","5- 141.372","6- Celula"]
    rc = ""
    resul.withdraw()
    fin = Toplevel()
    fin.geometry('400x400') # anchura x altura

    fin.configure(bg = 'darkslateblue')
    fin.resizable(width=False,height=False)
    fin.title('Final')
    Label(fin, text= "Promedio: " + str(prom(buenas)) +
          "\n\nTu nivel es: " + (str(nivel(prom))).upper(), font=("Brittanic Bold",15),fg="WHITE",
          bg="darkslateblue").pack(side=TOP)
    for i in range(len(RespCorr)):
        rc += "\n"+RespCorr[i]
    Label(fin, text= "Respuestas correctas: " + str(rc), font=("Brittanic Bold",15),fg="WHITE",
          bg="darkslateblue").place(x=95,y=150)
    
    bCerrar = ttk.Button(fin, text = "Cerrar" ,command=ventana.destroy).pack(side = BOTTOM)


#===Función para obtener el promedio=============================================================
def prom(buenas):
    #obtiene el promedio de los puntajes de los dos examenes
    return round(((buenas/6) * 100),2)
#casos de prueba
"""print(prom(6))
print(prom(0))
print(prom(4))
print(prom(9))"""

#===Función para obtener el nivel y consejo acerca de el promedio==========================================
def nivel(prom):
    #devuelve el nivel de conocimientos de acuerdo al promedio obtenido en los dos examenes
    if(prom(buenas) >= 95):
        return "Excelente\n\n¡Sigue así!"
    elif((prom(buenas) >= 80) and (prom(buenas) < 95)):
        return "Bueno\n\nRepasa tus apuntes"
    elif((prom(buenas) >= 60) and (prom(buenas) < 80)):
        return "Regular\n\nProcura estudiar más"
    else:
        return "malo\n\nRequiere nivelación"    
#casos de prueba
"""print(nivel(9))
print(nivel(0))
print(nivel(-4))
print(nivel(6567))"""

#===Función main=============================================================================
#manda llamar a la función de interfaz(ventana principal)
def main():
    interfaz()
    return 0

#===Código principal (main)=======================================================================
#Manda a llamar al main e inicializa variables importantes
if __name__ == '__main__':
    global intento
    intento = 1
    main()