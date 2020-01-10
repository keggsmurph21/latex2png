import argparse

from . import latex2png


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="input_fp", type=argparse.FileType("r"), default="-")
    parser.add_argument(
        "-o", dest="output_fp", type=argparse.FileType("wb"), default="-"
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "--tex-header", dest="tex_header_fp", type=argparse.FileType("r"), default=None,
    )
    parser.add_argument(
        "--tex-footer", dest="tex_footer_fp", type=argparse.FileType("r"), default=None,
    )
    parser.add_argument("--png-density", type=int, default=300)
    parser.add_argument("--png-quality", type=int, default=100)
    parser.add_argument("--png-background", default="#ffffff")
    args = parser.parse_args()

    latex2png(
        input_fp=args.input_fp,
        output_fp=args.output_fp,
        tex_header_fp=args.tex_header_fp,
        tex_footer_fp=args.tex_footer_fp,
        png_background=args.png_background,
        png_density=args.png_density,
        png_quality=args.png_quality,
        verbose=args.verbose,
    )
