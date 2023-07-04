import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "V29JeQ19BdVmx4keUhijKvDYxNTLW4zW" 

while True:
  orig = input("Ciudad de Origen: ")
  if orig == "quit" or orig == "q":
      break
  dest = input("Ciudad de Destino: ")
  if dest == "quit" or dest == "q":
      break 
  url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
  print("URL: " + (url))
  json_data = requests.get(url).json()
  json_status = json_data["info"]["statuscode"]
  if json_status == 0:
     print("API Status: " + str(json_status) + " = Ruta perfcectamente viable.\n")
     print("=============================================")
     print("Direcciones desde " + (orig) + " hacia " + (dest))
     print("Duración del Viaje:   " + (json_data["route"]["formattedTime"]))
     print("Kilometros:           " + str("{:.3f}".format((json_data["route"]["distance"])*1.61)))
     print("=============================================")
     for each in json_data["route"]["legs"][0]["maneuvers"]:
         print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
     print("=============================================")
