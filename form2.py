import requests 

def enviar_datos(url, data):
    response = requests.post(url, json=data)
    return response.status_code

def input_datos_persona(numero):

    print(f"Registro de la persona número {numero}")
    nombre = input("Coloca tu nombre: ")
    edad = int(input("Coloca tu edad: "))
    telefono = int(input("Coloca tu número de teléfono: "))
    
    return {
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono
    }

#funcion principal
def main():
    num_personas = int(input("cuantas personas quieres registrar: "))

    personas = []

    for i in range(num_personas):
        persona = input_datos_persona(i+1)
        personas.append(persona)
    
    data = {
        "personas": personas
    }

    url= "https://eno3l8n1ueea.x.pipedream.net"

    status_code = enviar_datos(url, data)

    if status_code == 200:
        print("Los datos han sido enviados exitosamente!!")
    else:
        print("Error al enviar los datos")


if __name__ == "__main__":
    main()