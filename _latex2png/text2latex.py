from typing import IO, Optional

import os
import sys


DEFAULT_HEADER = os.path.join(os.path.dirname(__file__), "../res/header.tex")
DEFAULT_FOOTER = os.path.join(os.path.dirname(__file__), "../res/footer.tex")


def text2latex(
    *,
    body_fp: IO[str],
    latex_fp: IO[str],
    header_fp: Optional[IO[str]] = None,
    footer_fp: Optional[IO[str]] = None,
    verbose: bool = False,
) -> None:

    if header_fp is None:
        with open(DEFAULT_HEADER) as header_fp:
            header = header_fp.read()
    else:
        header = header_fp.read()

    body = body_fp.read().strip()
    if not body:
        raise RuntimeError("Cannot generate image for empty string!")

    if footer_fp is None:
        with open(DEFAULT_FOOTER) as footer_fp:
            footer = footer_fp.read()
    else:
        footer = footer_fp.read()

    if verbose:
        print(f"$ cat {body_fp.name}", file=sys.stderr)
        print(header, file=sys.stderr)
        print(body, file=sys.stderr)
        print(footer, file=sys.stderr)

    latex_fp.write(header)
    latex_fp.write(body)
    latex_fp.write(footer)

    latex_fp.seek(0)
