def is_valid_url(url):
    """
    Checks if a given string is a valid URL using basic string operations.

    :param url: The input string to check.
    :return: True if valid, False otherwise.
    """

    valid_extensions = [".com", ".org", ".net", ".edu", ".gov", ".io"]

    if not (url.startswith("http://") or url.startswith("https://")):
        return False


    if not any(url.endswith(ext) for ext in valid_extensions):
        return False


    if " " in url:
        return False

    return True


# Testing the function
test_urls = [
    "http://example.com",
    "https://mywebsite.org",
    "ftp://invalid.com",
    "http://site with spaces.com",
    "https://website.fake",
]


results = {url: is_valid_url(url) for url in test_urls}
results
print(results)