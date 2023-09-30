from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader
from yaml import Loader, load

DEFAULT_HTML_FILENAME = "index.html"

PERSONAL_DETAILS = "personal_details"
WORK_EXPERIENCE = "work_experience"
EDUCATION = "education"


class ResumeGenerator:
    def __init__(
        self,
        config_filename: str,
        output_pdf_filename: str,
        output_html_filename: str = DEFAULT_HTML_FILENAME,
    ) -> None:
        self.config_filename = config_filename
        self.output_pdf_fiename = output_pdf_filename
        self.output_html_filename = f"assets/html/{output_html_filename}"

        self.config: Dict[str, Any] = None
        self.__load_configuration_file()

    def __load_configuration_file(self) -> None:
        with open(self.config_filename, "r") as file_:
            self.config = load(file_.read(), Loader)

    def generate_html_resume(self) -> None:
        environment = Environment(loader=FileSystemLoader("templates"))
        template = environment.get_template(f"{self.config.get('template')}.jinja")
        output = template.render(
            profile_picture=f"../images/{self.config.get(PERSONAL_DETAILS, {}).get('image', '')}",
            name=self.config.get(PERSONAL_DETAILS, {}).get("name", ""),
            surname=self.config.get(PERSONAL_DETAILS, {}).get("surname", ""),
            job_title=self.config.get(PERSONAL_DETAILS, {}).get("job_title", ""),
            about_me=self.config.get(PERSONAL_DETAILS, {}).get("about_me", ""),
            contact=self.config.get(PERSONAL_DETAILS, {}).get("contact", []),
            techstack=self.config.get(PERSONAL_DETAILS, {}).get("techstack", []),
            languages=self.config.get(PERSONAL_DETAILS, {}).get("languages", []),
            interests=self.config.get(PERSONAL_DETAILS, {}).get("interests", []),
            education=self.config.get(EDUCATION, []),
            work_experience=self.config.get(WORK_EXPERIENCE, []),
        )
        with open(self.output_html_filename, "w") as file_:
            file_.write(output)

    def __generate_pdf(self) -> None:
        print("Coming soon.")

    def generate(self) -> None:
        self.generate_html_resume()
        self.__generate_pdf()
