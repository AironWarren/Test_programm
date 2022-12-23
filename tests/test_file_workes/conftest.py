import pytest


cnt = 0

@pytest.fixture(autouse=True)
def clean_text_file():
    global cnt
    with open("tests/test_file.txt", 'w') as f_o:
        pass
    print(cnt)
    cnt += 1
