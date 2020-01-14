import argparse

from . import latex2png
from .text2latex import TEMPLATE


class MyFormatter(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter
):
    pass


def main():

    parser = argparse.ArgumentParser(
        prog="latex2png",
        formatter_class=MyFormatter,
        description="""\
This script allows the quick conversion of LaTeX snippets into PNG documents.

By default, any input text (either on stdin or from the `-i` file) is inserted
into the following template:

```
{latex_template}
```

This document is then rendered via `pdflatex` into a PDF document, which is
then converted via `imagemagick` into a PNG document, which is then written
to either stdout or a `-o` file (if provided).

Basic usage:
 $ echo '$ e^{{i\\pi}} + 1 = 0 $' | ./latex2png > /tmp/eulers-identity.png

For more info, check out the README.md file or the source repository at
    https://github.com/keggsmurph21/latex2png

""".format(
            latex_template=TEMPLATE.format(body="YOUR TEXT HERE", margin=4).strip()
        ),
    )
    parser.add_argument(
        "-i",
        dest="input_fp",
        type=argparse.FileType("r"),
        default="-",
        help="file containing text to be either inserted into the LaTeX template or \
        interpreted as a standalone a LaTeX document (if passed also `--no-latex-template`)",
    )
    parser.add_argument(
        "-o",
        dest="output_fp",
        type=argparse.FileType("wb"),
        default="-",
        help="file to write our PNG document into",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display output from each successive command run by latex2png",
    )
    parser.add_argument(
        "--no-latex-template",
        dest="use_latex_template",
        action="store_false",
        help="interpret input as a standalone LaTeX document (i.e., don't interpolate it into the template)",
    )
    parser.add_argument(
        "--latex-template-margin",
        type=int,
        default=4,
        help="margins for the PNG file, in `pt`s",
    )
    parser.add_argument(
        "--png-density", type=int, default=300, help="see `man convert` for details"
    )
    parser.add_argument(
        "--png-quality", type=int, default=100, help="see `man convert` for details"
    )
    parser.add_argument(
        "--png-background",
        default="#ffffff",
        help="background color for the PNG document -- can be any string parseable by `convert` (see `man convert` for details)",
    )
    args = parser.parse_args()

    latex2png(
        input_fp=args.input_fp,
        output_fp=args.output_fp,
        use_latex_template=args.use_latex_template,
        latex_template_margin=args.latex_template_margin,
        png_background=args.png_background,
        png_density=args.png_density,
        png_quality=args.png_quality,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()
