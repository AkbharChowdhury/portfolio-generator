from pydantic import BaseModel
from jinja2.environment import Template
from jinja2 import Environment

class Page(BaseModel):
    """
       Represents a single page in the static site generator.
       Each Page defines:
       - the Jinja template used to render HTML
       - the output file path where the rendered HTML is saved
       """
    model_config = {"frozen": True}
    template: str
    output: str

    def render(self, env: Environment, context: dict):
        template: Template = env.get_template(self.template)
        return template.render(**context)
