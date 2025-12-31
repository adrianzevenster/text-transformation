from __future__ import annotations
import re

_CODE_LIKE = re.compile(r"^\s*(class|def|import|from|SELECT|WITH|CREATE|INSERT|UPDATE|DELETE|@staticmethod)\b", re.I)

def clean_page_text(raw: str) -> str:
    """
    Cleans common PDF extraction artifacts
    """
    if not raw:
        return ""

    txt = raw.replace("\r\n", "\n").replace("\r", "\n")
    txt = re.sub(r"[ \t]+", " ", txt) # norms
    txt = re.sub(r"(\w)-\n(\w)", r"\1\2", txt) #hypens
    txt = re.sub(r"\n{3,}", "\n\n", txt) # blanks
    txt = "\n".join(line.rstrip() for line in txt.split("\n"))
    return txt.strip()

def looks_like_code(line: str) -> bool:
    return bool(_CODE_LIKE.search(line))
