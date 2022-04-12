from utils.url import get_full_url


def test_get_full_url():
    assert (
        get_full_url("http://local:3000/v1/", "accounts")
        == "http://local:3000/v1/accounts"
    )
    assert (
        get_full_url("http://local:3000/v1/", "accounts/1234")
        == "http://local:3000/v1/accounts/1234"
    )
