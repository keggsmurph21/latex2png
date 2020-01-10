from typing import IO

import os
import subprocess
import sys


COMMAND = """\
pdflatex \
    -output-directory={output_dir} \
    -jobname={jobname} \
    {input_filepath} \
"""


def latex2pdf(*, latex_fp: IO[str], pdf_fp: IO[bytes], verbose: bool = False) -> None:

    output_dir = os.path.dirname(pdf_fp.name)
    jobname, _ = os.path.splitext(os.path.basename(pdf_fp.name))

    cmd = COMMAND.format(
        output_dir=output_dir, jobname=jobname, input_filepath=latex_fp.name,
    )

    if verbose:
        print(f"$ {cmd}", file=sys.stderr)

    stdout = subprocess.check_output(
        cmd.split(), stderr=sys.stderr if verbose else subprocess.DEVNULL
    )

    if verbose:
        sys.stderr.buffer.write(stdout)
