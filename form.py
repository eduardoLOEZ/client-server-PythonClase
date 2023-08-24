import requests

num_personas = int(input("cuantas personas quieres registar: "))

personas = [] #guardar las personas o registros 

for i in range(num_personas):
    print(f"Registra a la persona numero {i+1} ")
    nombre = input("coloca tu nombre: ")#strings
    edad = int(input("coloca tu edad: ")) #int numeros
    telefono= int(input("coloca tu numero de telefono: ")) #int


    persona= {
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    }

    personas.append(persona)

data = {
    "personas": personas
    }

url= "https://eno3l8n1ueea.x.pipedream.net"

response = requests.post(url, json= data)

if response.status_code == 200:
    print(f"Datos de las personas enviados exitosamente!!")
else:
    print("error al enviar los datos")


    

