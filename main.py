import pytest

if __name__ == "__main__":
    pytest_args = [
        "Tests/",        # folder containing your test files
        "-q",            # quiet output (no -v spam)
        "--tb=short",    # cleaner tracebacks
        # "--maxfail=1"    # optional: stop after first failure
    ]
    pytest.main(pytest_args)
    