from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from models.page import Page
from models.portfolio import SocialLink

env = Environment(loader=FileSystemLoader("."), autoescape=True)
DEFAULT_ENCODING = "utf-8"


class PortfolioGenerator:
    def load_social_svgs(self, social_links: List[SocialLink]) -> None:
        for link in social_links:
            svg_path = link.svg_path
            if svg_path:
                path = Path(svg_path)
                link.svg_data = path.read_text(encoding=DEFAULT_ENCODING) if path.exists() else ''

    def __save_file(self, content: str, output_path: str) -> None:
        path = Path(output_path)
        path.write_text(content, encoding=DEFAULT_ENCODING)

    def generate_site(self, portfolio_data: dict, pages: List[Page]) -> None:
        for page in pages:
            html = page.render(env, portfolio_data)
            self.__save_file(html, page.output)