import requests


def num_courses(url):
    r = requests.get(url)
    data = r.json()

    return len(data["courses"])


# Dependency Injection
def num_courses1(url, getter=requests.get):
    r = getter(url)
    data = r.json()

    return len(data["courses"])
