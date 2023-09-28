"""Module: xml."""
from typing import Dict


def element(tag_name: str, attributes: Dict[str, object], content: str = "") -> str:
    """
    Creates an XML element
    :param tag_name The tag name of the element
    :param attributes The attributes of the element
    :param content The content of the element
    """

    attribute_list = []
    for name, value in attributes.items():
        attribute_list.append(f'{name}="{value}"')

    attribute_text = " ".join(attribute_list)

    # If the content is an empty string, return a self-closing tag element
    return (
        f"<{tag_name} {attribute_text} />"
        if content == ""
        else f"<{tag_name} {attribute_text}>{content}</{tag_name}>"
    )
