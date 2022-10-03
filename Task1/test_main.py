import requests

def test_get():
    url="http://localhost:8000"
    req_url=url
    response=requests.get(req_url)
    assert response.status_code== 200 
    assert response.text=='{"message":"Fast API in Python"}'
def test_get_user():
    url="http://localhost:8000"
    api_url="/user"
    req_url=url+api_url
    response=requests.get(req_url)
    assert response.status_code== 200 
def test_get_question():
    url="http://localhost:8000"
    api_url="/question/"
    values="1"
    req_url=url+api_url+values
    response=requests.get(req_url)
    assert response.status_code== 200
def test_get_alternatives():
    url="http://localhost:8000"
    api_url="/alternatives/"
    values="1"
    req_url=url+api_url+values
    response=requests.get(req_url)
    assert response.status_code== 200
    assert response.text
def test_get_alternatives_false():
    url="http://localhost:8000"
    api_url="/alternatives/"
    values="4"
    req_url=url+api_url+values
    response=requests.get(req_url)
    assert response.status_code== 200
    assert response.text
def test_get_answers():
    url="http://localhost:8000"
    api_url="/answer"
    params='''{
  "user_id": 0,
  "answers": [
    {
      "question_id": 0,
      "alternative_id": 0
    }
  ]
}'''
    req_url=url+api_url
    response=requests.post(req_url,json=params)
    assert response.status_code== 200

def test_result():
    url="http://localhost:8000"
    api_url="/result/"
    values="1"
    req_url=url+api_url+values
    response=requests.get(req_url)
    con="user" in response.text
    assert con
def test_result_false():
    url="http://localhost:8000"
    api_url="/result/"
    values="0"
    req_url=url+api_url+values
    response=requests.get(req_url)
    con="user" in response.text
    assert con
   
