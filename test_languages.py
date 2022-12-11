from subprocess import run


def test_python_no() -> None:
    result = run(["python", "test.py"], capture_output=True)
    assert b'SyntaxError' in result.stderr


def test_rust_no() -> None:
    result = run(["rustc", "test.rs"], capture_output=True)
    assert b'identifiers cannot contain emoji' in result.stderr
