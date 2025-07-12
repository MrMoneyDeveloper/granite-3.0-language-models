import sys, pathlib; sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]/"granite-cli-assist"))
from fastapi.testclient import TestClient
from granite_cli_assist.main import app

client = TestClient(app)

def test_livez():
    res = client.get("/livez")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}
