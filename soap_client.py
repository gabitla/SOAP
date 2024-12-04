# soap_client.py
import zeep

# Definir la URL del servicio SOAP
client = zeep.Client('http://127.0.0.1:8000/?wsdl')

# Llamar al método del servicio
result = client.service.say_hello("Gabriela", 1)
print(result)
