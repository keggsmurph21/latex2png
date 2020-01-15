# latex2png

A tiny command-line utility for generating PNG files from LaTeX snippets.  The entrypoint is `./latex2png`.

```bash
$ echo 'Hello! Would you like a slice of $ \pi $?' | l2p
```

[![Build Status](https://circleci.com/gh/keggsmurph21/latex2png.svg?style=shield)](https://circleci.com/gh/keggsmurph21/latex2png)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

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

To install on MacOS or Debian-based systems, run
```bash
./scripts/install
```

If you'd like to add support for another operating system, just [open an issue](https://github.com/keggsmurph21/latex2png/issues/new) or submit a pull request :^).

### Troubleshooting

If you have any problems, feel free to [file an issue](https://github.com/keggsmurph21/latex2png/issues)!
