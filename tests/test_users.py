import allure

@allure.feature("Users")
def test_get_users(api_client):
    response = api_client.get("/users")

    assert response.status == 200
    assert isinstance(response.json(), list)


@allure.feature("Users")
def test_user_schema(api_client):
    response = api_client.get("/users/1")

    data = response.json()
    assert "email" in data
    assert "username" in data