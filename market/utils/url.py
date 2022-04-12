from yarl import URL


def get_full_url(base_url: str, url_path: str) -> str:
    return str(URL(base_url) / url_path)
