from typing import IO

import sys


TEMPLATE = """\
\\documentclass[varwidth,convert,margin={margin}pt]{{standalone}}
\\usepackage{{amsmath}}
\\begin{{document}}
{body}
\\end{{document}}
"""


def text2latex(
    *,
    text_fp: IO[str],
    latex_fp: IO[str],
    use_latex_template: bool,
    margin: int,
    verbose: bool = False,
) -> None:

    if use_latex_template:
        body = text_fp.read()
        if not body.strip():
            raise RuntimeError("Cannot generate image for empty string!")
        content = TEMPLATE.format(body=body, margin=margin)
    else:
        content = text_fp.read()

    if verbose:
        print(f"$ cat {text_fp.name}", file=sys.stderr)
        print(content, file=sys.stderr)

    latex_fp.write(content)
    latex_fp.seek(0)
