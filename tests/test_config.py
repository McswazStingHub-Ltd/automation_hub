from src.config import APP_NAME, VERSION, AUTHOR


def test_app_name():
    assert APP_NAME == "Automation Hub"


def test_version():
    assert VERSION == "7.0"


def test_author():
    assert AUTHOR == "McswazStingHub-Ltd"


print("Configuration tests loaded.")
