"""Dashboard config schema regressions."""

from fastapi.testclient import TestClient

from hermes_cli import web_server


def test_approval_mode_schema_exposes_smart_approval_modes():
    field = web_server.CONFIG_SCHEMA["approvals.mode"]
    assert field["type"] == "select"
    assert field["options"] == ["manual", "smart", "off"]


def test_config_schema_endpoint_exposes_smart_approval_modes():
    client = TestClient(web_server.app)
    response = client.get("/api/config/schema")
    assert response.status_code == 200
    fields = response.json()["fields"]
    assert fields["approvals.mode"]["options"] == ["manual", "smart", "off"]
