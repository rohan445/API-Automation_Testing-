import pytest
import allure

@allure.feature("Products")
def test_get_all_products(api_client):
    with allure.step("Get all products"):
        response = api_client.get("/products")

    assert response.status == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@allure.feature("Products")
@pytest.mark.parametrize("product_id", [1, 2, 3])
def test_get_product_by_id(api_client, product_id):
    response = api_client.get(f"/products/{product_id}")

    assert response.status == 200
    assert "title" in response.json()


@allure.feature("Products")
def test_invalid_product(api_client):
    response = api_client.get("/products/9999")
    assert response.status in [400, 404]