import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add app to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "CompEng Aspirant" in response.text

def test_get_profile_api():
    response = client.get("/api/profile")
    assert response.status_code == 200
    data = response.json()
    assert "Computer Engineering" in data["target_career"]
    assert "Advanced Level (A/L) Student" in data["status"]

def test_get_academics_api():
    response = client.get("/api/academics")
    assert response.status_code == 200
    data = response.json()
    assert data["stream"] == "Physical Science"
    assert len(data["subjects"]) == 5

def test_get_projects_api():
    response = client.get("/api/projects")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3

def test_submit_contact_api():
    payload = {
        "name": "Prof. Fernando",
        "email": "fernando@university.edu",
        "subject": "Engineering Workshop",
        "message": "Interested in your IoT project."
    }
    response = client.post("/api/contact", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"

def test_download_cv_api():
    response = client.get("/api/download-cv")
    assert response.status_code == 200
    assert "attachment; filename=" in response.headers["content-disposition"]
    assert "ACADEMIC CV" in response.text

def test_static_assets_and_progress_bars():
    response = client.get("/")
    assert response.status_code == 200
    assert "progress-bar-fill" in response.text
    assert "data-progress=" in response.text

    for asset_path in [
        "/static/css/style.css", 
        "/static/js/app.js", 
        "/static/manifest.json", 
        "/static/favicon.ico",
        "/static/images/certificates/ol_exam.jpg",
        "/static/images/certificates/scholarship.jpg",
        "/static/images/certificates/girl_guides.jpg",
        "/static/images/certificates/st_john.jpg",
        "/static/images/certificates/singing.jpg",
        "/static/images/certificates/daham_pasala.jpg",
        "/static/images/certificates/chess.svg",
        "/static/images/certificates/youth_leadership.svg"
    ]:
        res = client.get(asset_path)
        assert res.status_code == 200

def test_get_extracurriculars_api():
    response = client.get("/api/extracurriculars")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 3

    # Check root page renders extracurricular content
    root_res = client.get("/")
    assert "Girl Guides" in root_res.text
    assert "St. John Ambulance" in root_res.text
    assert "Singing Competitions" in root_res.text
    assert "Chess" in root_res.text

def test_academics_page_certificate_links():
    root_res = client.get("/")
    assert root_res.status_code == 200
    assert "/certificates/ol-examination" in root_res.text
    assert "/certificates/scholarship" in root_res.text
    assert "/certificates/girl-guides" in root_res.text
    assert "/certificates/st-john-ambulance" in root_res.text
    assert "View Certificate" in root_res.text

def test_get_certificates_api():
    res = client.get("/api/certificates")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 8
    assert "ol-examination" in data
    assert "scholarship" in data
    assert "girl-guides" in data
    assert "st-john-ambulance" in data
    assert "singing-competitions" in data
    assert "daham-pasala" in data
    assert "chess-tournaments" in data
    assert "youth-leadership" in data

def test_get_single_certificate_api():
    res = client.get("/api/certificates/ol-examination")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "ol-examination"
    assert "9A Passes" in data["badge"]
    assert len(data["images"]) >= 1

    # Test 404
    err_res = client.get("/api/certificates/non-existent-cert")
    assert err_res.status_code == 404

def test_certificate_page_rendering():
    # Test valid cert page
    res = client.get("/certificates/ol-examination")
    assert res.status_code == 200
    assert "text/html" in res.headers["content-type"]
    assert "G.C.E. Ordinary Level" in res.text
    assert "Official Certificate Photo" in res.text
    assert "/static/images/certificates/ol_exam.jpg" in res.text
    assert "Return to Academics" in res.text

    # Test another cert page
    res2 = client.get("/certificates/st-john-ambulance")
    assert res2.status_code == 200
    assert "St. John Ambulance Cadets" in res2.text
    assert "First Aid and Cadet Training" in res2.text

    # Test 404 for nonexistent cert
    err_res = client.get("/certificates/unknown-credential")
    assert err_res.status_code == 404


