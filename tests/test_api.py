from fastapi.testclient import TestClient
from src.app.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "online"
    
# def test_agent_tool_selection():
#     # We ask a math question to see if it triggers the 'multiply' tool logic
#     response = client.post("/chat", json={"message": "What is 10 times 10?"})
#     assert response.status_code == 200
#     # We check if the answer '100' is somewhere in the natural language reply
#     assert "100" in response.json()["reply"]