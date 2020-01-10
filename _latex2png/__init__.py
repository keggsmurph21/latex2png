from typing import IO

import tempfile
import sys

from .text2latex import text2latex
from .latex2pdf import latex2pdf
from .pdf2png import pdf2png


def latex2png(
    *,
    input_fp: IO[str],
    output_fp: IO[bytes],
    png_background: str,
    png_density: int,
    png_quality: int,
    use_latex_template: bool = True,
    verbose: bool = False,
) -> None:

    with tempfile.NamedTemporaryFile(
        prefix="l2p-", suffix=".tex", mode="w+"
    ) as latex_fp, tempfile.NamedTemporaryFile(
        prefix="l2p-", suffix=".pdf", mode="w+b"
    ) as pdf_fp:

        text2latex(
            text_fp=input_fp, latex_fp=latex_fp, verbose=verbose,
        )

        latex2pdf(
            latex_fp=latex_fp, pdf_fp=pdf_fp, verbose=verbose,
        )

        png_bytes = pdf2png(
            pdf_fp=pdf_fp,
            png_fp=output_fp,
            background=png_background,
            density=png_density,
            quality=png_quality,
            verbose=verbose,
        )

        if output_fp is sys.stdout:
            sys.stdout.buffer.write(png_bytes)
