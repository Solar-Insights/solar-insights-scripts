from argparse import ArgumentParser, Namespace
from typing import Literal

LanguageChoices = Literal["fr", "en"]

def add_language_arg(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-l", "--lang", 
        type=str,
        choices=["fr", "en"],
        required=True,
        action="store", 
        dest="language", 
        help="The desired language of contact"
    )

def create_parser() -> ArgumentParser:
    parser = ArgumentParser(description="A script to generate contact texts for Solar Insights")

    add_language_arg(parser)

    return parser


def get_parsed_args() -> Namespace:
    parser = create_parser()
    return parser.parse_args()

args: Namespace = get_parsed_args()


LANGUAGE: LanguageChoices = args.language[0]

print(args.language)
