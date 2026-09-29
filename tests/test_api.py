from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from api.main import app

VALID = {"experience_level": 2, "job_title": 4, "work_year": 2022,
         "remote_ratio": 100, "company_location": 2, "company_size": 1}


@pytest.fixture
def client():
    # No Ollama or Supabase in tests: stub both side effects.
    with patch("api.main.generate_analysis", return_value="stub analysis"), \
         patch("api.main.save_prediction") as save:
        yield TestClient(app), save


def test_health(client):
    c, _ = client
    assert c.get("/").json() == {"status": "ok"}


def test_predict_returns_salary_and_saves(client):
    c, save = client
    r = c.post("/predict", json=VALID)
    assert r.status_code == 200
    body = r.json()
    assert 0 < body["predicted_salary_usd"] < 1_000_000
    assert body["analysis"] == "stub analysis"
    save.assert_called_once()


def test_predict_survives_llm_outage():
    with patch("api.main.generate_analysis", side_effect=ConnectionError), \
         patch("api.main.save_prediction"):
        r = TestClient(app).post("/predict", json=VALID)
    assert r.status_code == 200
    assert "unavailable" in r.json()["analysis"]


@pytest.mark.parametrize("field, value", [("experience_level", 4), ("job_title", -1),
                                          ("work_year", 2019), ("company_size", 3)])
def test_out_of_range_inputs_rejected(client, field, value):
    c, _ = client
    assert c.post("/predict", json={**VALID, field: value}).status_code == 422


def test_seniority_raises_prediction(client):
    c, _ = client
    entry = c.post("/predict", json={**VALID, "experience_level": 0}).json()["predicted_salary_usd"]
    senior = c.post("/predict", json={**VALID, "experience_level": 2}).json()["predicted_salary_usd"]
    assert senior > entry
