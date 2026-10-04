from fastapi.testclient import TestClient
from k8sdev.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'replicas': 2, 'image': 'api:1.4.2'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'replicas': 2, 'image': 'api:latest'}).json()
    assert bad["passed"] is False
    assert "image_tag_latest" in bad["failed"]
