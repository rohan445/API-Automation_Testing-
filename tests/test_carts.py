import allure

@allure.feature("Carts")
def test_get_carts(api_client):
    response = api_client.get("/carts")

    assert response.status == 200
    assert isinstance(response.json(), list)


@allure.feature("Carts")
def test_user_cart_flow(api_client):
    user = api_client.get("/users/1").json()
    carts = api_client.get("/carts").json()

    user_cart = [c for c in carts if c["userId"] == user["id"]]

    assert isinstance(user_cart, list)