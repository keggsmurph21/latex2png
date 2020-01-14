import nox


@nox.session
def format(session):
    session.install("black")
    session.run("black", "--check", "_latex2png")


@nox.session
def install(session):
    session.install(".")


@nox.session
def typecheck(session):
    session.install(".[dev]")
    session.run("mypy", "_latex2png")


@nox.session
def lint(session):
    session.install(".[dev]")
    session.run("flake8", "_latex2png")


@nox.session
def tests(session):
    session.install(".[dev]")
    session.run("pytest", "_latex2png")
