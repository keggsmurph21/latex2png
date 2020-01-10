from typing import IO

import subprocess
import sys


COMMAND = """\
convert \
    -flatten \
    -density {density} \
    {input_filepath} \
    -quality {quality} \
    -background {background} \
    -colorspace RGB \
    -colorspace Gray \
    {output_filepath} \
"""


def pdf2png(
    *,
    pdf_fp: IO[bytes],
    png_fp: IO[bytes],
    background: str,
    density: int,
    quality: int,
    verbose: bool = False,
) -> bytes:

    cmd = COMMAND.format(
        input_filepath=pdf_fp.name,
        output_filepath="png:-" if png_fp is sys.stdout else png_fp.name,
        background=background,
        density=density,
        quality=quality,
    )

    if verbose:
        print(f"$ {cmd}", file=sys.stderr)

    try:
        return subprocess.check_output(
            cmd.split(), stderr=sys.stderr if verbose else subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as e:
        raise ValueError(
            f'command "{cmd}" returned with code {e.returncode}:\n{e.output.decode()}'
        ) from e
