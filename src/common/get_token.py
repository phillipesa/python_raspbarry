import requests
import json

def TestGet():
    try:
        print('Aqui')
        url_get = 'http://api.supermix.com.br/operacao/telemetria/betoneira/slumpmix/viagem/BT-1706'
        response = requests.get(url_get, timeout=10, verify=False)
        response.raise_for_status()
    except Exception as err:
         print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response.status_code)
        response = str(response.json())    
        print('teste:'+response)
    

