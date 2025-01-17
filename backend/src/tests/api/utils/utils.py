from fastapi.testclient import TestClient

def req_type_to_function(client: TestClient, req_type: str):
    return {
        "GET": client.get,
        "POST": client.post,
        "PUT": client.put,
        "DELETE": client.delete
    }[req_type]


def get_response_items_list(response):
    return response.json()["data"]["items"]

def get_response_reservas_list(response):
    return response.json()["data"]

def get_response_avaliacoes_list(response):
    return response.json()["data"]
# TODO: create more utils functions