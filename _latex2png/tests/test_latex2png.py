from typing import Generator, IO

import pathlib

from .. import latex2png


time_byte = b"tIME"


def iter_bytes(fp: IO[bytes], word_size: int) -> Generator[bytes, None, None]:
    byte = fp.read(word_size)
    while byte:
        yield byte
        byte = fp.read(word_size)


def test_example(tmp_path: pathlib.Path):

    png_file_path = tmp_path / "generated.png"

    with open("./res/example.tex-snippet") as tex_snippet_fp, png_file_path.open(
        "w+b"
    ) as generated_png_fp:

        latex2png(
            input_fp=tex_snippet_fp,
            output_fp=generated_png_fp,
            png_background="white",
            png_density=90,
            png_quality=100,
            use_latex_template=True,
            latex_template_margin=4,
            verbose=False,
        )

        # Check PNG "magic number"
        generated_png_fp.seek(1)
        assert generated_png_fp.read(3) == b"PNG"
