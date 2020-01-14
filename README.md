# latex2png

A tiny command-line utility for generating PNG files from LaTeX snippets.  The entrypoint is `./latex2png`.

```bash
$ echo 'Hello! Would you like a slice of $ \pi $?' | l2p
```

### Usage

Let's assume we have the following file:
```bash
$ cat res/example.tex-snippet
The best equation is $ e^{i\pi} = -1 $! It uses $ e^{x+iy} = e^x\left(\cos{y} + i\sin{y}\right) $.
```

This program uses stdin/stdout by default.  For example, to write a LaTeX snippet to `res/example.png`, you could do

```bash
$ cat res/example.tex-snippet | ./latex2png > res/example.png
```

In order to generate this snippet: ![example.png](res/example.png)

It's also useful to pipe this directly to your clipboard.  You can do that with

```bash
$ cat res/example.tex-snippet | ./latex2png | xclip -selection c -t image/png -i  # Ubuntu
$ cat res/example.tex-snippet | ./latex2png | pbcopy                              # MacOS
```

To get the most out of this, we could add the following to our `.bashrc` (on Linux)
```bash
l2p() {
    /path/to/latex2png/latex2png "$@" | xclip -selection c -t image/png -i
}
```

Then we'll be able to get a snippet into our system clipboard with just
```bash
$ cat res/example.tex-snippet | l2p
```

To use filepaths, you can pass `-i $input_file` and `-o $output_file`, as in
```bash
$ ./latex2png -i res/example.tex-snippet -o res/example.png
```

For the full API, check
```bash
$ ./latex2png --help
```

### Installation

This script relies on the system binaries `pdflatex` (LaTeX &rarr; PDF) and `convert` (PDF &rarr; PNG, provided by [ImageMagick](https://imagemagick.org/index.php)).  On Ubuntu, you can install those with
```bash
$ sudo apt-get update
$ sudo apt-get install texlive-latex-extra imagemagick
```

Further, it uses the [`standalone`](https://ctan.org/pkg/standalone) LaTeX package, which may or may not be included in your distribution.

### Troubleshooting

If you have any problems, feel free to [file an issue](https://github.com/keggsmurph21/latex2png/issues)!
