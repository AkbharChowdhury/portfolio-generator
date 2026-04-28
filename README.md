# Portfolio Generator

A Python-based static portfolio site generator using Pydantic for structured data validation and Jinja2 for HTML templating.

---

## 🚀 Features

- Type-safe portfolio structure using Pydantic models
- HTML generation using Jinja2 templates
- Modular content system (skills, projects, education, etc.)
- Automatic SVG embedding for social links
- Clean separation of data and presentation

---

## 📁 Project Structure

models/ # Pydantic models (Portfolio, Skill, etc.)
templates/ # Jinja2 HTML templates
portfolio.json # Portfolio content data
main.py # Entry point
generate_site.py # Site generation logic