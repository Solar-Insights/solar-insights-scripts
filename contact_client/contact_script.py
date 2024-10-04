from argparse import ArgumentParser, Namespace
from typing import Literal

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

args: Namespace = get_parsed_args()


LANGUAGE: LanguageChoices = args.language
ORG_TYPE: OrganizationType = args.org_type

print(LANGUAGE)
print(ORG_TYPE)
