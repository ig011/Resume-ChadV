import argparse

from generator import ResumeGenerator

RESUME_CONFIG_FILE = "resume.config.yml"
OUTPUT_FILENAME = "CV.pdf"


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--build", action="store_true")
    arguments = argument_parser.parse_args()

    resume_generator = ResumeGenerator(RESUME_CONFIG_FILE, OUTPUT_FILENAME)
    resume_generator.generate_html_resume()

    if arguments.build:
        resume_generator.generate()


if __name__ == "__main__":
    main()
