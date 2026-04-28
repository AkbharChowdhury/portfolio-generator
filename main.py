import json
from datetime import UTC, datetime
from typing import List

from models.portfolio import Portfolio
from generate_portfolio import load_social_svgs, generate_site
from models.page import Page


def get_current_year() -> int:
    return datetime.now(tz=UTC).year


def load_file(file_path):
    with open(file_path) as f:
        return json.load(f)


def load_portfolio(file_path: str) -> Portfolio:
    portfolio_data = load_file(file_path)
    return Portfolio.model_validate(portfolio_data)


def main():
    portfolio_path: str = 'portfolio.json'
    portfolio_data: dict = load_file(portfolio_path)

    my_portfolio: Portfolio = Portfolio.model_validate(portfolio_data)
    load_social_svgs(my_portfolio.social_links) if my_portfolio.social_links else None

    my_portfolio.skills = sorted(
        my_portfolio.skills or [],
        key=lambda s: s.proficiency,
        reverse=True
    )

    pages: List[Page] = [
        Page(template="index_template.html", output="index.html")
    ]
    portfolio_data: dict = {
        'current_year': get_current_year(),
        **my_portfolio.model_dump(),
    }

    generate_site(portfolio_data, pages)

    print('HTML files generated successfully!')


if __name__ == "__main__":
    main()

