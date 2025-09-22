from typing import Any
from bs4 import BeautifulSoup

def get_file_content(file_path: str) -> Any | str | None:
    try:
        with open(file_path, "r") as page_source:
            return page_source.read()
    except FileNotFoundError:
        print(f"File {file_path} doesn't exist!")


def main() -> None:
    page_source = get_file_content("page.html")
    soup = BeautifulSoup(page_source, "html.parser")

    critics_consensus = soup.find('div', {
        "id": "critics-consensus"
    }).find('p')
    print(critics_consensus.text)


if __name__ == '__main__':
    main()