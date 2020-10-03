class Locator(): # pylint: disable=too-few-public-methods
    """
    Contains all page object and web-elements from https://www.saucedemo.com/ page.
    """
    #login page locators
    login_user_name = "user-name"
    login_password = "password"
    login_button = "login-button"
    error_icon = "/html/body/div[2]/div[1]/div/div/form/h3"

    # home page locators
    menu_button = "menu_button_container"
    product_label = "product_label"
    burger_button = "bm-burger-button"
    logout_button = "logout_sidebar_link"
    back_pack = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button"
    back_pack_id = "item_4_title_link"
    bike_light = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button"
    bike_light_id = "item_0_title_link"
    red_tshirt = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[6]/div[3]/button"
    red_tshirt_id = "item_3_title_link"
    remove_backpack = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button"

    # shopping cart locators
    cart_button = "/html/body/div/div[2]/div[1]/div[2]/a"
    cart_title = "/html/body/div/div[2]/div[2]"
    cart_qty = "/html/body/div/div[2]/div[3]/div/div[1]/div[3]"
    mini_cart_qty = "/html/body/div/div[2]/div[1]/div[2]/a/span"
    remove_first_element = "/html/body/div/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[2]/button"
    remove_second_element = "/html/body/div/div[2]/div[3]/div/div[1]/div[4]/div[2]/div[2]/button"
    remove_third_element = "/html/body/div/div[2]/div[3]/div/div[1]/div[5]/div[2]/div[2]/button"
    checkout_button = "/html/body/div/div[2]/div[3]/div/div[2]/a[2]"

    # personal info locators
    user_info_title = "/html/body/div/div[2]/div[2]"
    first_name = "/html/body/div/div[2]/div[3]/div/form/div[1]/input[1]"
    last_name = "/html/body/div/div[2]/div[3]/div/form/div[1]/input[2]"
    zip_code = "/html/body/div/div[2]/div[3]/div/form/div[1]/input[3]"
    continue_button = "/html/body/div/div[2]/div[3]/div/form/div[2]/input"
    error_message = "/html/body/div/div[2]/div[3]/div/form/h3"
    cancel_button = "/html/body/div/div[2]/div[3]/div/form/div[2]/a"

    # checkout overview locators
    overview_title = "/html/body/div/div[2]/div[2]"
    payment_info = "/html/body/div/div[2]/div[3]/div/div[2]/div[1]"
    overview_cancel_button = "/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[1]"
    overview_finish_button = "/html/body/div/div[2]/div[3]/div/div[2]/div[8]/a[2]"

    # checkout complete locators
    pony_express_image = "/html/body/div/div[2]/div[3]/img"
