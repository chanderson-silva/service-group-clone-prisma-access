# Clonar Service Group entre Folders no Prisma Access
Este script em Python tem o objetivo de clonar um Service Group de uma [Folder](https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-cloud-managed-admin/create-prisma-access-policy/organizing-your-prisma-access-configurations#:~:text=Configuration%20Folders%20You%20can%20apply%20Prisma%20Access%20policy,be%20shared%20or%20are%20specific%20to%20deployment%20types.) (pasta) para outra Folder que você especificar. Através da API, é possível realizar essa tarefa de forma automatizada e rápida.


### Requisitos
* Python 3.x instalado no seu sistema.
* Módulo requests instalado. Caso não tenha, você pode instalá-lo usando o pip:
```python
pip install requests
```
* Módulo re instalado. Caso não tenha, você pode instalá-lo usando o pip:
```python
pip install re
```
* Módulo json instalado. Caso não tenha, você pode instalá-lo usando o pip:
```python
pip install json
```
* Módulo getpass instalado. Caso não tenha, você pode instalá-lo usando o pip:
```python
pip install getpass
```
### Utilização
Certifique-se de que o Python 3.x está instalado no seu sistema e os módulos basicos estejam instalados corretamente.

Clone este repositório ou faça o download dos arquivos para o seu computador.

### O que será necessário

* Seu access_token para autenticação
* Nome do Service Group que deseja clonar
* Nome da Folder de origem
* Nome da Folder de destino (para onde o Service Group será clonado)
* Client ID
* Client Secret
* Execute o script clone_service_group.py:

```python
python clone_service_group.py
```
O script irá clonar o Service Group especificado da Folder de origem para a Folder de destino.

Contribuição
Se você tiver sugestões de melhorias ou encontrar problemas, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.
