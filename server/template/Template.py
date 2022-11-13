import os
from enum import Enum


class TemplateFile(Enum):
    TEMPLATE_BASIC = f"{os.getcwd()}/template/template_basic.html"
    TEMPLATE_FULL = f"{os.getcwd()}/template/template_full.html"


def loadTemplate(templateFile: TemplateFile) -> str:
    template: str = ""
    if templateFile == TemplateFile.TEMPLATE_BASIC:
        with open(TemplateFile.TEMPLATE_BASIC.value, "r") as f:
            for line in f.readlines():
                template += str(line)
    elif templateFile == TemplateFile.TEMPLATE_FULL:
        with open(TemplateFile.TEMPLATE_FULL.value, "r") as f:
            for line in f.readlines():
                template += str(line)
    else:
        raise FileNotFoundError("Template not found.")
    return template
