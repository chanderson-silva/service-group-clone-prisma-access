import requests

def get_access_token(client_id, client_secret, tsg_id):
    url = 'https://auth.apps.paloaltonetworks.com/oauth2/access_token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'scope': f'tsg_id:{tsg_id}'
    }
    auth = (client_id, client_secret)

    response = requests.post(url, headers=headers, data=data, auth=auth)

    if response.status_code == 200:
        response_data = response.json()
        access_token = response_data.get('access_token')
        return access_token
    else:
        print(f"Failed to get access token. Status code: {response.status_code}")
        return None
