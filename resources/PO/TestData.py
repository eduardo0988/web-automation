class TestData():  # pylint: disable=too-few-public-methods
    """
    Constants relevant for automation
    """
    # saucedemo site
    BASE_URL = "https://www.saucedemo.com/"

    # geckodriver path
    GECKO_PATH = "drivers/gecko/"

    # expected title in page
    EXPECTED_TITLE = "Swag Labs"

    # list of users
    USERS = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user"]

    # invalid user
    INVALID_USER = "thief"
    # password
    PASSWORD = "secret_sauce"

    # generic 0.3 seconds delay
    DELAY = 0.3

    # User Information
    FIRST_NAME = "Donkey"
    LAST_NAME = "Kong"
    ZIP_CODE = 58535
