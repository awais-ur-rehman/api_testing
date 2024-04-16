import requests
import pytest

API_URL = "https://api.themoviedb.org/3"
API_KEY = "ce2c351a2bd26662a98594d87c683aab"

def set_auth_headers():
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZTJjMzUxYTJiZDI2NjYyYTk4NTk0ZDg3YzY4M2FhYiIsInN1YiI6IjY2MWU5OTEyZDE4ZmI5MDE3ZGNhYmNkOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GbDvKORBWuvE_1Zt4M5ByfL6OnSUXwXi1VZKZyFYodw',
        'Content-Type': 'application/json'
    }
    return headers

@pytest.mark.parametrize("api_key", [API_KEY, ""])
def test_get_top_rated_movies(api_key):
    url = f"{API_URL}/movie/top_rated?api_key={api_key}"
    response = requests.get(url)
    if api_key:
        assert response.status_code == 200, "Should return status 200 with valid API key"
    else:
        assert response.status_code == 401, "Should return status 401 with invalid API key"

def test_rate_movie_success():
    """Test successfully rating a movie."""
    headers = set_auth_headers()
    url = f"{API_URL}/movie/{693134}/rating?api_key={API_KEY}"
    data = {"value": 8.5}
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 201, "Should return status 201 when successfully rating a movie"

def test_rate_movie_unauthorized():
    """Test rating a movie without authorization."""
    url = f"{API_URL}/movie/{1011985}/rating?api_key={API_KEY}"
    data = {"value": 8.5}
    response = requests.post(url, json=data)
    assert response.status_code == 401, "Should return status 401 when unauthorized"

def test_rate_movie_bad_input():
    """Test rating a movie with invalid input."""
    headers = set_auth_headers()
    url = f"{API_URL}/movie/{359410}/rating?api_key={API_KEY}"
    data = {"value": 15} 
    response = requests.post(url, headers=headers, json=data)
    assert response.status_code == 400, "Should return status 400 for bad input"
