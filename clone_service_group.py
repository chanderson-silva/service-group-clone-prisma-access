####Security Rule enable logs
import sys
import re
import requests
from criandotoken import get_access_token
import json
import getpass
# import argparse

banner = '''
 #####                                       
#     # ###### #####  #    # #  ####  ###### 
#       #      #    # #    # # #    # #      
 #####  #####  #    # #    # # #      #####  
      # #      #####  #    # # #      #      
#     # #      #   #   #  #  # #    # #      
 #####  ###### #    #   ##   #  ####  ###### 
                                             
 #####                                     
#     # #####   ####  #    # #####   ####  
#       #    # #    # #    # #    # #      
#  #### #    # #    # #    # #    #  ####  
#     # #####  #    # #    # #####       # 
#     # #   #  #    # #    # #      #    # 
 #####  #    #  ####   ####  #       ####  
                                           
'''
print("\n")
print(banner)
print("\n")


# ####VARIABLES
name_service = input("Digite o Name_Service: ")
folder_origem = input("Digite o Folder_Origem: ")
folder_destino = input("Digite o Folder_Destino: ")

client_id = input("Digite o client_id: ")
# client_secret = input("Digite o client_secret: ")
client_secret = getpass.getpass("Digite o client_secret: ")
tsg_id = input("Digite o tsg_id: ")

# ###GERAR TOKEN

access_token = get_access_token(client_id, client_secret, tsg_id)

if access_token:
    print("Token de acesso obtido com sucesso!")
    # print(f"Token: {access_token}")
else:
    print("Falha ao obter o token de acesso.")

# return access_token
# ####LISTAR REGRAS
def list_service_group():
    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/service-groups?name={}&folder={}".format(name_service,folder_origem)

    payload={}
    headers = {
      'Accept': 'application/json',
      'Authorization': f'Bearer {access_token}'
    }

    listobject = requests.request("GET", url, headers=headers, data=payload)
    list_object = listobject.text

    list_object_json = json.loads(list_object)

    # print(type(list_object_json))
    # print(list_object_json)
    return list_object_json

    # for valor in list_object:                                                                                            
    #     print(valor)  

    return list_object



def list_service_object(list_object_json):
    # print ("Funcao2 ", list_object_json)

    data = list_object_json['members']
    # data= ['DCE-RPC']
    for name_valor in data:     
            url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?name={}&folder={}".format(name_valor,folder_origem)
            # url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?name=IDAQUI&folder=Mobile Users"
            payload={}
            headers = {
              'Accept': 'application/json',
              'Authorization': f'Bearer {access_token}'
            }
            service = requests.request("GET", url, headers=headers, data=payload)
            service_result = service.text
            list_service_json = json.loads(service_result)
            # print(service.status_code)
            # print(list_service_json)  
            ###
            ###filter
            ###
            if service.status_code == 200:
                name = list_service_json['name']
                
                # print("ESTE E O NOME" + name)
                # description = list_service_json['id']
                descr = "Generete By Copy" + str(name) +" from " +str(folder_origem)
                protocol = list_service_json['protocol']
                # protocol_string = protocol.replace("'", '"')

                # list_service_json['protocol'] = protocol_string
                # print (type(protocol))
                mudando = str(protocol)
                alterado = mudando.replace("'", '"')
                # print (type(str(protocol)))
                # print(alterado)
                list_service_json['protocol'] = alterado
                
                # carregamento = json.dumps(alterado)
                # print(carregamento)
                # protocol_string = print(protocol)
                # regex_protocol = protocol_string.replace("'", '"')
                # list_service_json['protocol'] = protocol_string
                # proto = protocol.replace("'",'"')
                # port =
                # tags =
                if re.search("tcp", alterado):
                    port = protocol['tcp']['port']
                    those = "tcp"
                    print("Create Protocol TCP: " + name)
                else:
                    port = protocol['udp']['port']
                    those = "udp"
                    print("Create Protocol UDP: " + name)
                    # filte = r"\d+"
                    # resultado = re.search(filte, alterado)
                    # print(resultado)
                payload = json.dumps({
                  "description": f"{descr}",
                  "name": f"{name}",
                  "protocol": {
                    f"{those}": {
                      "port": f"{port}"
                    }},

                })
                url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?folder={}".format(folder_destino)
                
                headers = {
                  'Content-Type': 'application/json',
                  'Authorization': f'Bearer {access_token}'
                }
                response = requests.request("POST", url, headers=headers, data=payload)

                print(response.text)
                # print(payload)
                #return list_service_json
            elif service.status_code == 400 | service.status_code == 404:
                print("\n"+"Create SubGroup")
                url = "https://api.sase.paloaltonetworks.com/sse/config/v1/service-groups?name={}&folder={}".format(name_valor,folder_origem)
            # url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?name=IDAQUI&folder=Mobile Users"
                payload={}
                headers = {
                  'Accept': 'application/json',
                  'Authorization': f'Bearer {access_token}'
                }
                service2 = requests.request("GET", url, headers=headers, data=payload)
                service2_result = service2.text
                list_service2_json = json.loads(service2_result)
#                print(service2)
                data2 = list_service2_json['members']
                for name_valor in data2:     
                        url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?name={}&folder={}".format(name_valor,folder_origem)
                        # url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?name=IDAQUI&folder=Mobile Users"
                        payload={}
                        headers = {
                          'Accept': 'application/json',
                          'Authorization': f'Bearer {access_token}'
                        }
                        service3 = requests.request("GET", url, headers=headers, data=payload)
                        service3_result = service3.text
                        list_service3_json = json.loads(service3_result)
                        # print(service)
                        # print(list_service_json)  
                        ###
                        ###filter
                        ###
                        if service3.status_code == 200:
                            name = list_service3_json['name']
                            
                            # print("ESTE E O NOME" + name)
                            description = list_service3_json['id']
                            protocol = list_service3_json['protocol']
                            # protocol_string = protocol.replace("'", '"')

                            # list_service_json['protocol'] = protocol_string
                            # print (type(protocol))
                            mudando = str(protocol)
                            alterado = mudando.replace("'", '"')
                            # print (type(str(protocol)))
                            # print(alterado)
                            list_service3_json['protocol'] = alterado
                            
                            # carregamento = json.dumps(alterado)
                            # print(carregamento)
                            # protocol_string = print(protocol)
                            # regex_protocol = protocol_string.replace("'", '"')
                            # list_service_json['protocol'] = protocol_string
                            # proto = protocol.replace("'",'"')
                            # port =
                            # tags =
                            if re.search("tcp", alterado):
                                port = protocol['tcp']['port']
                                those = "tcp"
                                print("Create Protocol TCP: " + name)
                            else:
                                port = protocol['udp']['port']
                                those = "udp"
                                print("Create Protocol UDP: " + name)
                                # filte = r"\d+"
                                # resultado = re.search(filte, alterado)
                                # print(resultado)
                            payload = json.dumps({
                              "description": f"{description}",
                              "name": f"{name}",
                              "protocol": {
                                f"{those}": {
                                  "port": f"{port}"
                                }},

                            })
                            url = "https://api.sase.paloaltonetworks.com/sse/config/v1/services?folder={}".format(folder_destino)
                            
                            headers = {
                              'Content-Type': 'application/json',
                              'Authorization': f'Bearer {access_token}'
                            }
                            response = requests.request("POST", url, headers=headers, data=payload)

                            print(response.text)
                            # print(payload)
                            #return list_service_json
                        else: 
                            print("Dont Work ......")

    ####Agregando no grupo
                name_group = list_service2_json['name']
                # print("ESTE E O NOME: " + name_group)
                # print(data2)

                url = "https://api.sase.paloaltonetworks.com/sse/config/v1/service-groups?folder={}".format(folder_destino)
                # print("\n")
                mudando = str(data2)
                # alterado = mudando.replace("[", "")
                # alterado = alterado.replace("]","")
                
                remover=r"\[|\]"
                validado = re.sub(remover, "", mudando)

                # print(validado)
                # print(validado)
                print("\n")
                payload = json.dumps({
                  "members": 
                    data2
                  ,
                  "name": f"{name_group}"
                })

                # print("\n")
                # print(payload)
                headers = {
                  'Content-Type': 'application/json',
                  'Authorization': f'Bearer {access_token}'
                }
                # print("\n")
                # print(payload)
                response = requests.request("POST", url, headers=headers, data=payload)

                print(response.text)
            else:
                print("Error Status")

def create_services_Group_object(list_object_json):
    
    data = list_object_json['members']
    name_group = list_object_json['name']
    # print("ESTE E O NOME: " + name_group)

    url = "https://api.sase.paloaltonetworks.com/sse/config/v1/service-groups?folder={}".format(folder_destino)
    # print("\n")
    mudando = str(data)
    # alterado = mudando.replace("[", "")
    # alterado = alterado.replace("]","")
    
    remover=r"\[|\]"
    validado = re.sub(remover, "", mudando)

    # print(validado)
    print("\n")
    payload = json.dumps({
      "members": 
        data
      ,
      "name": f"{name_group}"
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {access_token}'
    }
    # print("\n")
    # print(payload)
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)



resultado_da_funcao1 = list_service_group()

# Chama a segunda função passando o resultado da primeira como argumento
list_service_object(resultado_da_funcao1)
# list_service_group()
create_services_Group_object(resultado_da_funcao1)


# create_services_Group_object()