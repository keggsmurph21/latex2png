from setuptools import setup, find_namespace_packages


setup(
    name="latex2png",
    author="Kevin Murphy",
    author_email="kevin@murp.us",
    version="0.0.1",
    packages=find_namespace_packages(include="_latex2png"),
    description="A tool for converting LaTeX snippets to PNG images",
    install_requires=[],
    entry_points={"console_scripts": ["latex2png = _latex2png.__main__:main"]},
    extras_require={"dev": ["flake8", "black", "mypy", "pytest"]},
)
