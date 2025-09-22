from typing import Any
from bs4 import BeautifulSoup

def get_file_content(file_path: str) -> Any | str | None:
    try:
        with open(file_path, "r") as page_source:
            return page_source.read()
    except FileNotFoundError:
        print(f"File {file_path} doesn't exist!")


def get_critics_consensus(soup: BeautifulSoup) -> str:
    return soup.find('div', {
        "id": "critics-consensus"
    }).find('p').text


def get_movie_data(soup: BeautifulSoup) -> dict[str, Any]:
    info_categories = soup.find('section', {
        "class": "media-info"
    }).find('dl').find_all('div', {
        "class": "category-wrap"
    })

    output = {}
    for category in info_categories:
        info_key = category.find('rt-text', {
            "class": "key"
        }).text
        info_value = category.find('dd').text.strip().split(', \n')
        output[info_key] = info_value

    return output


def main() -> None:
    page_source = get_file_content("page.html")
    soup = BeautifulSoup(page_source, "html.parser")

    critics_consensus = get_critics_consensus(soup)
    movie_data = get_movie_data(soup)
    print(critics_consensus)

    for key, values in movie_data.items():
        print(f"{key}: {", ".join(values)}")


if __name__ == '__main__':
    main()