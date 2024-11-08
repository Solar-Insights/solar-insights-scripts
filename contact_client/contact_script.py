from argparse import ArgumentParser, Namespace
from typing import Literal
import webbrowser
import urllib.parse


LanguageChoices = Literal["fr", "en"]
OrganizationType = Literal["energy", "public", "software"]
 
def add_language_arg(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-l", "--lang", 
        type=str,
        choices=["fr", "en"],
        required=True,
        action="store", 
        dest="language", 
        help="Language of contact"
    )

def add_org_type_arg(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-ot", "--org-type", 
        type=str,
        choices=["energy", "public", "software"],
        required=True,
        action="store", 
        dest="org_type", 
        help="Type of organization"
    )

def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description="A script to generate contact texts for Solar Insights")

    add_language_arg(parser)
    add_org_type_arg(parser)

    return parser

def get_parsed_args() -> Namespace:
    parser = create_parser()
    return parser.parse_args()

def get_full_file_name(file_descriptor: str) -> str:
    SUB_DIR = "./contact_client"
    TEXT_FILE_EXTENSION = "txt"

    return f"{SUB_DIR}/{file_descriptor}-{LANGUAGE}.{TEXT_FILE_EXTENSION}"

def open_mailto(recipient: str, subject: str, body: str) -> None:
    encoded_body = urllib.parse.quote(body)
    webbrowser.open(f"mailto:{recipient}?subject={subject}&body={encoded_body}")


ARGS: Namespace = get_parsed_args()
LANGUAGE: LanguageChoices = ARGS.language
ORG_TYPE: OrganizationType = ARGS.org_type
ORG_NAME = input("organization name: ")
CONTACT_EMAIL = input("contact email: ")
FILES = {
    "title": "title",
    "introduction": "introduction",
    "conclusion": "conclusion",
    "public": "public_org",
    "energy": "energy_org",
    "software": "sofware_org"
}

title_file = get_full_file_name(FILES["title"])
introduction_file = get_full_file_name(FILES["introduction"])
org_file = get_full_file_name(FILES[ORG_TYPE])
conclusion_file = get_full_file_name(FILES["conclusion"])

title = ""
with open(title_file, "r", encoding="utf-8") as f:
    title += f.read()

communication = ""
with open(introduction_file, "r", encoding="utf-8") as f:
    communication += f.read()

with open(org_file, "r", encoding="utf-8") as f:
    communication += f.read()

with open(conclusion_file, "r", encoding="utf-8") as f:
    communication += f.read()

communication = communication.replace("$org_name$", ORG_NAME)
communication = communication.replace("$lang$", LANGUAGE)

open_mailto(CONTACT_EMAIL, title, communication)
