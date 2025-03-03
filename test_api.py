import requests

def test_obtener_recomendacion():
    url = "http://127.0.0.1:8000/recomendacion"
    data = {"consulta": "cuando se celebra el premier padel de Valladolid"}
    response = requests.post(url, json=data)
    
    # Verificar que el código de estado sea 200
    assert response.status_code == 200
    assert isinstance(response.json(), str)
    

# Ejecutar el test
if __name__ == "__main__":
    test_obtener_recomendacion()