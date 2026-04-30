import json
from datetime import UTC, datetime
from typing import List

from models.portfolio import Portfolio
from generate_portfolio import load_social_svgs, generate_site
from models.page import Page
from models.skills import Skill


def get_current_year() -> int:
    return datetime.now(tz=UTC).year


def load_file(file_path: str):
    with open(file_path) as f:
        return json.load(f)


def load_portfolio(file_path: str) -> Portfolio:
    portfolio_data = load_file(file_path)
    return Portfolio.model_validate(portfolio_data)


def sort_skills(skills: List[Skill]) -> List[Skill]:
    return sorted(skills, key=lambda s: s.proficiency, reverse=True)


def main():
    portfolio_path: str = 'portfolio.json'
    portfolio: Portfolio = load_portfolio(portfolio_path)

    if portfolio.social_links:
        load_social_svgs(portfolio.social_links)
    if portfolio.skills:
        sorted_skills: list[Skill] = sort_skills(portfolio.skills)
        portfolio.skills = sorted_skills

    pages: List[Page] = [
        Page(template='index_template.html', output='index.html')
    ]
    portfolio_data: dict = {
        'current_year': get_current_year(),
        **portfolio.model_dump(),
    }

    generate_site(portfolio_data, pages)

    print('HTML files generated successfully!')


if __name__ == "__main__":
    main()
