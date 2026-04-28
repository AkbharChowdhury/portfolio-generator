from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from models.page import Page


env = Environment(loader=FileSystemLoader("."), autoescape=True)
DEFAULT_ENCODING = "utf-8"


def load_social_svgs(social_links: list) -> None:
    for link in social_links:
        svg_path = getattr(link, "svg_path", None)
        if svg_path:
            path = Path(svg_path)
            link.svg_data = path.read_text(encoding=DEFAULT_ENCODING) if path.exists() else ''


def save_file(content: str, output_path: str) -> None:
    Path(output_path).write_text(content, encoding=DEFAULT_ENCODING)


def generate_site(portfolio_data: dict, pages: List[Page]) -> None:
    for page in pages:
        html = page.render(env, portfolio_data)
        save_file(html, page.output)
