# Simulacion Movilidad Urbana 
Modelación de sistemas multiagentes con gráficas computacionales TC2008B




##  Índice 

- [Introduccion](#introduccion)
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Funcionamiento del Codigo](#funcionamiento-del-codigo)
- [Autores](#autores)



## Introduccion

En las cuidades modernas, los peatones enfretan obstaculos que comprometen su movilidad, seguridad y accesbilidad, especialmente en entornos donde interactuan con vehiculos por lo que se requiere una infraestructura y comunicacion adecuada.



## Instalacion

        git clone git@github.com:MiguelCabreraVictoria/Equipo1_TC2008B.git


### Requisitos 

- [Entorno Virtual Python](https://docs.python.org/es/3.13/tutorial/venv.html)
    - [AgentPy](https://agentpy.readthedocs.io/en/latest/installation.html)   
    - [WebSockets](https://websockets.readthedocs.io/en/stable/index.html)

- Unity Version-6000
    - [ProBuilder](https://docs.unity3d.com/Packages/com.unity.probuilder@4.0/manual/installing.html) 
    - [Nuget](https://github.com/GlitchEnzo/NuGetForUnity)
    - [NewtonSoft](https://docs.unity3d.com/Packages/com.unity.nuget.newtonsoft-json@2.0/manual/index.html)

## Uso 

        source setup.sh 

        > Abrir la carpeta City en Unity
            - Ejecutar el proyecto 

        python Web-Socket/python_client.py

## Funcionamiento del Codigo

#### Diagrama de clases
![Diagramas de clase](images/diagrama.png)

#### Protocolos de interaccion ( Comunicacion bidireccional )
![Protocolos](images/protocolo.png)

## Autores

- Miguel Angel Cabrera Victoria

- Julia María Stephanie Duenkelsbuehler Castillo

- Elit Shadday Acosta Pastrana