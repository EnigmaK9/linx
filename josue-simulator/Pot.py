import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
import sys
import csv

def EPS(PV, dt):  #Init: lista de condiciones iniciales P, V
    '''
    EPS
        Electric Power System

    Subsistema.
        Se encarga de distribuir la energía a los otros sistemas
        con los voltajes y corrientes adecuados y con la regulación adecuada.

    Función iterativa.
        Se usa iterativamente para encontrar la energía que consume el
        subsistema en un paso (step, dt) pequeño de tiempo.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia [W]
            Init[1]: Voltaje [V]
        dt: tiempo [s]. Step, Paso.

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
        P: Potencia del subsistema [W]
    '''

    P = PV[0]
    V = PV[1]

    I = (P/V)*1000 #Corriente = Potencia/Voltaje, *1000 para convertir de A a mA
    E = P*(dt/3600) #Energía = Potencia * tiempo (t en mín se convierte a horas 60 mín = 1 h)
    return E, I, P

def OBC(PV, dt):
    '''
    OBC
        On Board Computer.

    Subsistema.
        CORAL, IA.

    Función de Python iterativa.
        Esta función calcula la energía disipada
        en un paso (dt) y la corriente que demanda.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia [W]
            Init[1]: Voltaje [V]
        dt: tiempo [s]. Step, Paso.

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
        P: Potencia del subsistema [W]
    '''

    P = PV[0]
    V = PV[1]

    I = (P/V) * 1000 # Corriente = Potencia / Voltaje, *1000 para convertir de A a mA
    E = P * (dt / 3600) # Energía = Potencia * tiempo (t en min se convierte a horas 60 min = 1 h)
    return E, I, P

def COMMRX(PV, dt):  #Init: lista de condiciones iniciales P, V, dt. COMMS RX 437 MHz
    '''
    COMMRX
        Communication Receive

    Subsistema.
        Telecomunicaciones.

    Función iterativa:
        Se usa iterativamente para encontrar la energía que consume el
        subsistema en un paso (step, dt) pequeño de tiempo.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia [W]
            Init[1]: Voltaje [V]
        dt: tiempo [s]. Step, Paso.

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
        P: Potencia del subsistema [W]
    '''
    P = PV[0]
    V = PV[1]

    I = (P/V)*1000 #Corriente = Potencia/Voltaje, *1000 para convertir de A a mA
    E = P*(dt/3600) #Energía = Potencia * tiempo (t en mín se convierte a horas 60 min = 1 h)
    return E, I, P

def Camera(PV, Init, t, dt):#Init: lista de condiciones iniciales P, V, t0, T. Cámara Multiespectral
    '''
    Camera
        Cámara Multiespectral

    Subsistema.
        Cámara Multiespectral
        Se poseen tres modelos con diferentes potencias.

    Función de Python iterativa con duración:
        Se realizará un pasaje cada cierta órbita,
        desde un tiempo inicial y durante cierto tiempo dt consumirá energía
        hasta llegar al tiempo final.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia del subsistema [W]. Será negativo el número a ingresar (Consumo),
                    eso puede modificarse si se quiere

            Init[1]:  Voltaje Operacional [V]. Debe ser un número positivo
                *21/02/24 Se supondrá constante V = 5 [V], P = 4.6 [W]

            Init[2]: Órbita, es un numero del 1 al 15, indica la Órbita de inicio del evento.

            Init[3]: es el minuto de inicio. Puede ir de 0 a 94.6 [min]. (Órbita de 500 km).

            Init[4]: Duración de la actividad [min]

        t:  tiempo actual [min].

        dt: Step, Paso. [s].

    Datos de salida:
        E: Energía consumida [Wh]
        I:  Corriente [I]
        P: Potencia del subsistema [W]
    '''
    Logic, Event = VecEventos(t, Init)

    if Logic == 0: #no está activado
        E = 0
        I = 0
        P = 0
    else: # Hay alguna tarea activa, Event indica dicha tarea
        P = PV[0] #Potencia
        V = PV[1] #Voltaje

        I = P / V * 1000 #Corriente = Potencia/Voltaje [mA]
        E = P * (dt / 3600) # Energía = Potencia * tiempo
        # (t en s se convierte a horas: 3600 s = 1 h)
    return E, I, P

def COMMTX_MHz(PV, Init, t, dt):#Init: lista de condiciones iniciales P, V, t0, T. COMMS TX 437 MHz
    '''
    COMMTXMHz
        Communication transmitter

    Subsistema.
        Telecomunicaciones, en MHz.
        Se realizarán pasajes cada cierta órbita,
        desde un tiempo inicial y durante cierto tiempo.

    Función de Python iterativa con duración:
        Se realizará un pasaje cada cierta órbita,
        desde un tiempo inicial y durante cierto tiempo dt consumirá energía
        hasta llegar al tiempo final.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia del subsistema [W]. Será negativo el número a ingresar (Consumo),
                    eso puede modificarse si se quiere

            Init[1]:  Voltaje Operacional [V]. Debe ser un número positivo
                *21/02/24 Se supondrá constante P = 7.2 [W], V = 3.6 [V]

            Init[2]: Órbita, es un numero del 1 al 15, indica la Órbita de inicio del evento.

            Init[3]: es el minuto de inicio. Puede ir de 0 a 94.6 [min]. (órbita de 500 km).

            Init[4]: Duración de la actividad [min]

        t:  tiempo actual [min].

        dt: Step, Paso. [s].

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
        P: Potencia del subsistema [W]
    '''
    Logic, Event = VecEventos(t, Init) # indica si hay alguna tarea activa

    if Logic == 0: # no está activado
        E = 0
        I = 0
        P = 0
    else: #Hay alguna tarea activa, Event indica dicha tarea
        P = PV[0] #Potencia
        V = PV[1] #Voltaje

        I = P/V*1000 #Corriente = Potencia/Voltaje [mA]
        E = P*(dt/3600) #Energía = Potencia * tiempo (t en s se convierte a horas: 3600 s = 1 h)
    return E, I, P

def COMMTX_GHz(PV, Init, t, dt):
    # Init: lista de condiciones iniciales P, V, t0, T. COMMS TX 2.4 GHz
    '''
    COMMTXGHz
        Communication transmitter

    Subsistema.
        Telecomunicaciones, en GHz.
        Se realizarán pasajes cada cierta órbita,
        desde un tiempo inicial y durante cierto tiempo.

    Función de Python iterativa con duración:
        Se realizará un pasaje cada cierta órbita,
        desde un tiempo inicial y durante cierto tiempo dt consumirá energía
        hasta llegar al tiempo final.

    Datos de entrada:
        Init: Condiciones iniciales:
            Init[0]: Potencia del subsistema [W]. Será negativo el número a ingresar (Consumo),
                    eso puede modificarse si se quiere

            Init[1]:  Voltaje Operacional [V]. Debe ser un número positivo
                *21/02/24 Se supondra constante P = 25 [W], V = 5 [V]

            Init[2]: Órbita, es un numero del 1 al 15, indica la Órbita de inicio del evento.

            Init[3]: es el minuto de inicio. Puede ir de 0 a 94.6 [min]. (órbita de 500 km).

            Init[4]: Duración de la actividad [min]

        t:  tiempo actual [min].

        dt: Step, Paso. [s].

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
        P: Potencia del subsistema [W]
    '''
    Logic, Event = VecEventos(t, Init)

    if Logic == 0: # no está activado
        E = 0
        I = 0
        P = 0
    else: # Hay alguna tarea activa, Event indica dicha tarea
        P = PV[0] # Potencia
        V = PV[1] # Voltaje

        I = P / V *1000 # Corriente = Potencia/Voltaje [mA]
        E = P*(dt/3600) # Energía = Potencia * tiempo (t en s se convierte a horas: 3600 s = 1 h)
    return E, I, P

def Panel(Init, t0ciudad, ts, dt):
    # ts: hora de la órbita desde un punto de referencia (Polo sur)
    '''
    Panel
        Paneles Solares

    Subsistema
        Se encarga de modelar el comportamiento del panel solar.
        Durante el día (t <= 47.3 min) el panel simulará la forma de la
        potencia como si estuviera en órbita de 500 km.
        Durante la noche (47.3 min <= t <= 94.6) el panel tendrá
        potencia cero.

    Función Iterativa con if
        Se usa iterativamente para encontrar la energía que consume el
        subsistema en un paso (step, dt) pequeño de tiempo.
        El if sirve para separar el día de la noche.
        El tiempo sera local para el satélite, es decir
                    0 min <= t <= 94.6
    '''
    Vop = Init[0] # V
    a = Init[1] # m^2
    aeff = Init[2] #0.0 - 1.0
    peff = Init[3] #0.0 - 1.0
    Irr = Init[4] # W/m^2

    t0 = t0ciudad[0]*60*60 + t0ciudad[1] + t0ciudad[2]/60
    # Tiempo del pasaje sobre la ciudad
    Omega = t0 * np.pi/720 - np.pi #R.A. Nodo de ascenso [rad]
    incl = 97.40176 * np.pi/180 # inclinación [rad]
    arg = t0ciudad[3] # argumento [rad]

    # función potencia modificada para órbitas circulares SSO a 500 km
    # np.pi/720 rotación de la tierra por minuto [rad]
    Pp = Irr * a * aeff * peff * (np.cos(Omega)*np.cos(0.0011069*60*ts + arg) - \
        np.cos(incl)*np.sin(Omega)*np.sin(0.0011069*60*ts + arg))
    #0.0011069 rad/s: freq, angular orbital

    if Pp > 0: #lado diurno
        Ep = Pp * dt/3600 #Wh
        Ip = Pp / Vop *1000 #mA
    else:
        Ep = 0
        Pp = 0
        Ip = 0
    return Ep, Ip, Pp

def Battery(Init, q, E, I, P):
    '''
    Battery Pack
        Fuente de Poder

    Fuente.
        Durante la noche será una Fuente, se descargarán las baterías, podría
        llegar a ser dependiente del tiempo.
        Durante el día podría tener diferentes estrategias de carga:
            1) Cargar a máximo poder, disminuye el tiempo.
            2) Cargar distribuyendo la carga durante la órbita,
            disminuye la potencia y la corriente de carga.

    Función de Python.
        Se usa iterativamente para encontrar la energía que consume el
        subsistema en un paso (step, dt) pequeño de tiempo.

    Datos de entrada:
        Init: list de condiciones Iniciales:
            Init[0]: Voltaje de Carga [V]
            Init[1]: Corriente de Carga [mA]
            Init[2]: Voltaje de Descarga [V]
            Init[3]: Corriente de Descarga [mA]
            Init[4]: Almacenamiento Total [mAh]

            Los siguientes elementos de Init no se ocupan en esta
            función pero están en la lista:
            Init[5]: Porcentaje inicial de batería entre 0 y 100 [%]
            Init[6]: Porcentaje de seguridad [%]
            Init[7]: Porcentaje mínimo [%]

        q: Almacenamiento actual
        E: Lista de energías de los subsistemas para un dt.
        I: Lista de corrientes de los subsistemas para un dt.
        P: Lista de potencias de los subsistemas para un dt.

        ts: tiempo local del satélite. Va de 0 a 94.6 [min]
        dt: tiempo [s]. Step, Paso.

    Datos de salida:
        E: Energía consumida [Wh]
        I: Corriente necesaria para alimentar el subsistema [mA]
    '''

    # Condiciones iniciales:
    # Carga
    Vc = Init[0] # V
    Ic = Init[1] # mA

    # Descarga
    Vd = Init[2] # V
    Id = Init[3] # mA

    # Almacenamiento
    Q = Init[4] # Wh

    E1 = 0
    I1 = 0
    P1 = 0

    for i in range(len(E)):
        P1 = P1 + P[i] # Potencia Neta
        I1 = I1 + I[i]
        E1 = E1 + E[i] # Energía Neta

    PcMax = Vc * Ic / 1000 # Potencia de carga maxima = Voltaje*corriente [W]
    PdMax = Vd * Id / 1000 # Potencia de descarga maxima = Voltaje*corriente [W]

    q = q + E1 # Energía actual de la batería luego de un dt

    if Q > q: # le falta energía
        E1 = q

    else:  # Carga Máxima
        E1 = Q

    return E1, I1, P1

def Orbita(t): # Número de Órbitas Completadas
    return int(t/94.6) # 94.6 min es el período a 500 km

def VecEventos(t, Init):
    '''
    Función auxiliar
        Devuelve el numero del evento programado (la fila en la matriz).
        Se utiliza en los subsistemas con eventos programados durante el día

        Compara el tiempo del Main Program con los diferentes intervalos de los
        eventos programados. Devuelve 1 si el evento esta en ejecución y
        0 en caso contrario.

        También puede DETENER la ejecución del programa si encuentra algún inicio
        del programa aún cuando no ha acabado el anterior

        Luego revisa cuantas tareas van a ejecutarse en ese momento.
            Si no hay ninguna tarea, devuelve 0
            Si hay una tarea, devuelve 1 y el número del evento (la fila)
            Si hay mas de una tarea detiene la ejecución y manda error.

        Datos de Entrada:
        t: Tiempo [min] el tiempo total de ejecución del Main Program
        Init: Lista de eventos, cada evento está compuesto de:
            Init[0]: Tiempo inicial en formato ISO 8601 'HH:MM:SS'
    '''
    Vec = [] # Este vector tendrá unos y ceros, dependiendo si el programa se activa o no
    for i in Init:
        T_Inicio = i[0]*60 + i[1] + i[2]/60
        # Convierte las horas y los segundos a minutos
        T_final = T_Inicio + i[3]
        if t >= T_Inicio and t <= T_final:
            Vec.append(1)
        else:
            Vec.append(0)

    j = 0
    # contador, sirve para verificar el estado de los eventos programados
    for k in Vec:
        # Suma todos los elementos del vector
        j = j + k

    cont = 0 # Contador
    event = 0 # el número del evento activo

    if j == 0:
        # si el tiempo no entra en ningún rango
        # entonces la energía del subsistema es cero
        event = 0
    elif j == 1: # si hay un evento activo
        for m in Vec:
            if m == 1:
                event = cont # número del evento activo (Int[event])
            cont = cont + 1
        # print("El evento es el numero %2d" % (event))
    else: # dos o más eventos se inician sin haber acabado un evento
        sys.exit("Error. Dos o más eventos se superponen")
        # cancela la ejecución
    return j, event

def AsignarPV(Archivo):
    PV_EPS =     [] # P, V
    PV_OBC =     [] # P, V
    PV_COMMRX =  [] # P, V
    PV_Camera =  [] # P, V
    PV_COMMTX_MHZ =  [] # P, V
    PV_COMMTX_GHZ =  [] # P, V

    List = []

    # Abrir archivo de Potencia y Voltaje
    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Nombre'] == 'EPS':
                PV_EPS.append(float(row['P']))
                PV_EPS.append(float(row['V']))
                List.append(PV_EPS)
            elif row['Nombre'] == 'OBC':
                PV_OBC.append(float(row['P']))
                PV_OBC.append(float(row['V']))
                List.append(PV_OBC)
            elif row['Nombre'] == 'COMMRX':
                PV_COMMRX.append(float(row['P']))
                PV_COMMRX.append(float(row['V']))
                List.append(PV_COMMRX)
            elif row['Nombre'] == 'Camera':
                PV_Camera.append(float(row['P']))
                PV_Camera.append(float(row['V']))
                List.append(PV_Camera)
            elif row['Nombre'] == 'COMMTX_MHZ':
                PV_COMMTX_MHZ.append(float(row['P']))
                PV_COMMTX_MHZ.append(float(row['V']))
                List.append(PV_COMMTX_MHZ)
            elif row['Nombre'] == 'COMMTX_GHZ':
                PV_COMMTX_GHZ.append(float(row['P']))
                PV_COMMTX_GHZ.append(float(row['V']))
                List.append(PV_COMMTX_GHZ)
    return List

def Asignar_Evento_Camara(Archivo):
    List = []

    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l1 = []
            l1.append(float((row['Hora'])))
            l1.append(float((row['Minuto'])))
            l1.append(float((row['Segundo'])))
            l1.append(float(row['Duracion']))
            List.append(l1)
    return List

def Asignar_Evento_COMMTX_MHz(Archivo):
    List = []

    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l1 = []
            l1.append(float((row['Hora'])))
            l1.append(float((row['Minuto'])))
            l1.append(float((row['Segundo'])))
            l1.append(float(row['Duracion']))
            List.append(l1)
    return List

def Asignar_Evento_COMMTX_GHz(Archivo):
    List = []

    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            l1 = []
            l1.append(float((row['Hora'])))
            l1.append(float((row['Minuto'])))
            l1.append(float((row['Segundo'])))
            l1.append(float(row['Duracion']))
            List.append(l1)
    return List

def AsignarPanel(Archivo):
    List = []
    #Abrir archivo de Panel
    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            List.append(float(row['Voltaje']))
            List.append(float(row['Area']))
            List.append(float(row['A_efectiva']))
            List.append(float(row['Panel_efectivo']))
            List.append(float(row['Irradiancia']))
    return List

def AsignarBateria(Archivo):
    List = []
    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            List.append(float(row['Voltaje_carga']))
            List.append(float(row['Corriente_carga']))
            List.append(float(row['Voltaje_descarga']))
            List.append(float(row['Corriente_descarga']))
            List.append(float(row['Capacidad']))
            List.append(float(row['Porcentaje_inicial_Carga']))
            List.append(float(row['Porcentaje_seguridad']))
            List.append(float(row['Porcentaje_minimo']))
    return List

def Config(Archivo):
    List = []
    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            List.append(float(row['Step(dt)']))
            List.append(float(row['Horas_Totales']))
    return List

def Ciudad(Archivo):
    List = []
    with open(Archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            List.append(float(row['Hora_Pasaje']))
            List.append(float(row['Minuto_Pasaje']))
            List.append(float(row['Segundo_Pasaje']))
            List.append(float(row['Latitud']))
    return List

def argumento(incl, Lat):
    # Método numérico para obtener el angulo inicial de la simulación (la fase)
    aux = 2
    arg = 0
    while np.abs(aux - np.cos(np.pi/2 - Lat*np.pi/180) ) > 0.0001:
        aux = np.sin(incl*np.pi/180)*np.sin(arg)
        arg = arg + 0.0001
    return arg

#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# Condiciones Iniciales

# PV= [P, V]
# Condiciones iniciales subsistemas
ListaPV = AsignarPV('InitPV.csv')

PV_EPS =     ListaPV[0] #P, V
PV_OBC =     ListaPV[1] #P, V
PV_COMMRX =  ListaPV[2] #P, V
PV_Camera =  ListaPV[3] #P, V
PV_COMMTX_MHz =  ListaPV[4] #P, V
PV_COMMTX_GHz =  ListaPV[5] #P, V


# Evento: ['HH:MM:SS', T]
#-------------------------------------------
# Cámara
Init_Camera = Asignar_Evento_Camara('EventCamera.csv')

#-------------------------------------------
# Telemetría
Init_COMMTX_MHz = Asignar_Evento_COMMTX_MHz('EventTelemetry.csv')

#-------------------------------------------
# Telemetría
Init_COMMTX_GHz = Asignar_Evento_COMMTX_GHz('EventCOMMGHZ.csv')

#-------------------------------------------
# condiciones iniciales Panel
# Init[ V [V], area [m^2], a efectiva = [0,78], P eff = [0.31], Irr = [1365] ]
Init_Panel = AsignarPanel('Panel.csv')

#-------------------------------------------
# Condiciones Iniciales Batería
# Vc, Ic, Vd, Id, Q, Q% inicial, Q% de Seguridad, Q% mínimo
Init_Battery = AsignarBateria('Bateria.csv')

# -------------------------------------------
# Ciudad
CDMX = Ciudad('CDMX.csv')
arg = argumento(97.4, CDMX[3])
print(arg)

t0CDMX = [CDMX[0], CDMX[1], CDMX[2], arg] #tiempo cero, HH,MM,SS,Latitud del Pasaje sobre México


#-------------------------------------------
# Configuración

Configuracion = Config('Config.csv')

t = 0 # tiempo cero [min]. Reloj de la simulación
dt = Configuracion[0] # segundos. Step
Tiempo = Configuracion[1] # horas de visualización
#-------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------
# MAIN PROGRAM

EGraph = [] #lista de energías de la batería para graficar[Wh]
PGraph = [] #lista de la suma de las potencias [W] en el tiempo
IGraph = [] #lista de la suma de corrientes [mA] en el tiempo
tGraph = [] #lista del tiempo para gráficar [mín]


E_Batt_actual = Init_Battery[4]*Init_Battery[5] # Energía inicial
P_actual = 0 #Potencia Inicial
I_actual = 0 #corriente Inicial

EGraph.append(E_Batt_actual)
PGraph.append(P_actual)
IGraph.append(I_actual)
tGraph.append(t)

#----------------------------------------------------------------------------------------
# loop principal

while t <= Tiempo*60: # se convierte Tiempo a minutos
    Edt = [0]*8 # Energía consumida por cada subsistema en un dt
    Idt = [0]*8 # Corriente demandada por cada subsistema en un dt
    Pdt = [0]*8 # Potencia por cada subsistema en un dt

    Orbit = Orbita(t) # órbita actual

    taux = t - Orbit*94.6 # Tiempo del día local del satélite taux = [0, 94.6).

    Edt[0], Idt[0], Pdt[0] = EPS(PV_EPS, dt)
    Edt[1], Idt[1], Pdt[1] = OBC(PV_OBC, dt)
    Edt[2], Idt[2], Pdt[2] = COMMRX(PV_COMMRX, dt)
    Edt[3], Idt[3], Pdt[3] = Camera(PV_Camera, Init_Camera, t, dt)
    Edt[4], Idt[4], Pdt[4] = COMMTX_MHz(PV_COMMTX_MHz, Init_COMMTX_MHz, t, dt)
    Edt[5], Idt[5], Pdt[5] = COMMTX_GHz(PV_COMMTX_GHz, Init_COMMTX_GHz, t, dt)
    Edt[6], Idt[6], Pdt[6] = Panel(Init_Panel, t0CDMX, taux, dt)

    E_Batt_actual, I_actual, P_actual = Battery(Init_Battery, E_Batt_actual, Edt, Idt, Pdt)


    EGraph.append(E_Batt_actual)
    PGraph.append(P_actual)
    IGraph.append(I_actual)

    t = t + dt/60
    tGraph.append(t)

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Gráfico
def min2hour(x):
    return x / 60

def hour2min(x):
    return x * 60

fig, ax1 = plt.subplots(figsize=(50,10))

fig.suptitle('Carga de la batería y Potencia Neta en función del tiempo')

#--------------------------------------------------------------------------------------------
# Carga de la batería vs tiempo

ax1.plot(tGraph,EGraph,'r', label ='Batería')
ax1.set_xlabel("$Tiempo \; [mín]$")
ax1.set_ylabel("$Carga \; de \; la \; Batería \; [Wh]$")

secax_x = ax1.secondary_xaxis('top', functions=(min2hour, hour2min))
secax_x.set_xlabel('Tiempo [h]')

ax1.set_ylim(0,40)
ax1.tick_params(axis='y', colors='red')
ax1.spines['left'].set_color('red')
ax1.spines['right'].set_color('blue')

Qmax = Init_Battery[4]
Qsec = Init_Battery[4]*Init_Battery[6]
Qmin = Init_Battery[4]*Init_Battery[7]

ax1.axhline(Qmax, color = 'g')
ax1.axhline(Qsec, color = 'y')
ax1.axhline(Qmin, color = 'r')
y1ticks = [*ax1.get_yticks(), Qmax, Qsec, Qmin]
y1ticklabels = [*ax1.get_yticklabels(), "%5.2f Wh (max)" % (Qmax),
                "%5.2f Wh (sec)" % (Qsec), "%5.2f Wh (mín)" % (Qmin)]
ax1.set_yticks(y1ticks, labels=y1ticklabels)

ax1.grid(color = 'r', linestyle = '--', linewidth = 0.5)
ax1.legend(loc = 'lower left')

#--------------------------------------------------------------------------------------------
# Potencia Neta vs Tiempo

ax2 = ax1.twinx()
ax2.plot(tGraph,PGraph, label ='Potencia Neta')

ax2.axhline(0, color = 'black', linestyle = '-.')
ax2.set_ylabel("$Potencia \; Neta \; [W]$")

ax2.tick_params(axis='y', colors='blue')
ax2.spines['left'].set_color('red')
ax2.spines['right'].set_color('blue')

ax2.grid(color = 'b', linestyle = '-.')
ax2.legend(loc = 'lower right')

plt.show()


