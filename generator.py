from selenium import webdriver
from selenium.common import exceptions as sel_exceptions
from LocalStorage import LocalStorage
import time
from DiscordAccount import DiscordAccount
from sys import argv
import datetime
from os import path, mkdir


class Bot():

    register_site = "https://discord.com/register"
    app_home = "https://discord.com/channels/@me"
    register_site_timeout = 3
    email_selector = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(1) > div > input"
    username_selector = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(2) > div > input"
    password_selector = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(3) > div > input"
    terms_selector = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div.flex-1xMQg5.flex-1O1GKY.horizontal-1ae9ci.horizontal-2EEEnY.flex-1O1GKY.directionRow-3v3tfG.justifyStart-2NDFzi.alignCenter-1dQNNs.noWrap-3jynv6.marginTop20-3TxNs6 > label > input"
    register_next_selector = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(5) > button"
    register_next_selector_us = "#app-mount > div.app-1q1i1E > div > div.leftSplit-1qOwnR > div > form > div > div.block-egJnc0.marginTop20-3TxNs6 > div:nth-child(4) > button"

    settings_selector = "#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div > div > div > div.content-98HsJk > div.sidebar-2K8pFh.hasNotice-1XRy4h > section > div > div.flex-1xMQg5.flex-1O1GKY.horizontal-1ae9ci.horizontal-2EEEnY.flex-1O1GKY.directionRow-3v3tfG.justifyStart-2NDFzi.alignStretch-DpGPf3.noWrap-3jynv6 > button:nth-child(3)"
    logout_selector = "#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div:nth-child(2) > div > div.sidebarRegion-VFTUkN > div > div > nav > div > div:nth-child(23)"
    logout_confirm_selector = "#app-mount > div:nth-child(6) > div.modal-3c3bKg > div > form > div.flex-1xMQg5.flex-1O1GKY.horizontalReverse-2eTKWD.horizontalReverse-3tRjY7.flex-1O1GKY.directionRowReverse-m8IjIq.justifyStart-2NDFzi.alignStretch-DpGPf3.noWrap-3jynv6.footer-3rDWdC > button.button-38aScr.lookFilled-1Gx00P.colorRed-1TFJan.sizeMedium-1AC_Sl.grow-q77ONN"
    settings_open_timeout = 2
    logout_timeout = 2
    app_nav_timeout = 8
    skip_tutorial_selector = "#app-mount > div:nth-child(6) > div.modal-3c3bKg > div > form > div > button.btn-2OZqMZ.btnDefault-3gHhPM"
    skip_tutorial_timeout = 2
    shady_logout_selector = "#app-mount > div.app-1q1i1E > div > div.layers-3iHuyZ.layers-3q14ss > div:nth-child(2) > div > div.flex-1xMQg5.flex-1O1GKY.horizontal-1ae9ci.horizontal-2EEEnY.flex-1O1GKY.directionRow-3v3tfG.justifyStart-2NDFzi.alignStretch-DpGPf3.noWrap-3jynv6.marginTop4-2BNfKC.marginBottom20-32qID7 > div:nth-child(3) > a"
    shady_logout_confirm_selector = "#app-mount > div:nth-child(6) > div.modal-3c3bKg > div > form > div.flex-1xMQg5.flex-1O1GKY.horizontalReverse-2eTKWD.horizontalReverse-3tRjY7.flex-1O1GKY.directionRowReverse-m8IjIq.justifyStart-2NDFzi.alignStretch-DpGPf3.noWrap-3jynv6.footer-3rDWdC > button.button-38aScr.lookFilled-1Gx00P.colorRed-1TFJan.sizeMedium-1AC_Sl.grow-q77ONN"
    reclick_delay = 40
    recaptcha_selector = "#rc-anchor-container"

    def __init__(self, driver, display_userdata=False):
        self.driver = driver
        self.display_userdata = display_userdata
        print("Bot initialized")

    def generate_token(self):
        account = self.register_account()

        if account == None:
            print("Was not able to register account. No token generated")
            return None
        else:
            print("Alt-Token: " + account.token)
            return account

    def logout(self, direct=False, stack=0):
        try:
            if not direct:
                self.driver.get(self.app_home)
                time.sleep(self.app_nav_timeout)

            if self.driver.find_elements_by_css_selector(self.shady_logout_selector):
                shady_logout_button = self.driver.find_elements_by_css_selector(
                    self.shady_logout_selector)[0]
                shady_logout_button.click()
                time.sleep(self.logout_timeout)
                shady_logout_confirm = self.driver.find_elements_by_css_selector(self.logout_confirm_selector)[
                    0]
                shady_logout_confirm.click()
                time.sleep(self.logout_timeout)
                return True

            if self.driver.find_elements_by_css_selector(self.skip_tutorial_selector):
                skip_tutorial_button = self.driver.find_elements_by_css_selector(
                    self.skip_tutorial_selector)[0]
                skip_tutorial_button.click()
                time.sleep(self.skip_tutorial_timeout)

            settings = self.driver.find_elements_by_css_selector(self.settings_selector)[
                0]
            settings.click()
            time.sleep(self.settings_open_timeout)
            logout = self.driver.find_elements_by_css_selector(self.logout_selector)[
                0]
            logout.click()
            time.sleep(self.logout_timeout)
            logout_confirm = self.driver.find_elements_by_css_selector(self.logout_confirm_selector)[
                0]
            logout_confirm.click()
            time.sleep(self.logout_timeout)
        except (sel_exceptions.ElementClickInterceptedException, sel_exceptions.NoSuchElementException, sel_exceptions.StaleElementReferenceException) as e:
            if stack < 3:
                self.logout(stack=stack + 1)
            else:
                raise Exception(
                    "Stacktrace 3 reached! Logout not successfull! Message: " + e.message)

        return True

    def register_account(self):
        account = DiscordAccount()
        account.generate_random_credentials()
        if self.display_userdata:
            print("Registering user: " + account.username + " Email: " + account.email +
                  " Password: " + account.password)

        self.driver.get(self.register_site)

        login_site_tmp = self.driver.current_url
        time.sleep(self.register_site_timeout)

        if self.driver.current_url != login_site_tmp:
            if self.driver.current_url == self.app_home:
                print("AUTH ERR: Already logged in!")
                self.logout()
                self.driver.get(self.register_site)
                time.sleep(self.register_site_timeout)
            else:
                print("AUTH ERR: Got unpredicted redirect!")
                return None

        email_textbox = self.driver.find_elements_by_css_selector(
            self.email_selector)[0]
        username_textbox = self.driver.find_elements_by_css_selector(
            self.username_selector)[0]
        password_textbox = self.driver.find_elements_by_css_selector(
            self.password_selector)[0]

        if self.driver.find_elements_by_css_selector(
                self.terms_selector):
            terms_checkbox = self.driver.find_elements_by_css_selector(
                self.terms_selector)[0]
            next_button = self.driver.find_elements_by_css_selector(self.register_next_selector)[
                0]
        else:
            next_button = self.driver.find_elements_by_css_selector(self.register_next_selector_us)[
                0]

        email_textbox.send_keys(account.email)
        username_textbox.send_keys(account.username)
        password_textbox.send_keys(account.password)
        terms_checkbox.click()
        time.sleep(1)
        next_button.click()

        last_reclick = self.reclick_delay
        while self.driver.current_url == login_site_tmp:
            time.sleep(0.5)
            last_reclick -= 1
            if last_reclick == 0:
                if self.driver.find_elements_by_css_selector(self.register_next_selector):
                    next_button.click()
                    print("Retry")
                else:
                    if self.driver.find_elements_by_css_selector(self.recaptcha_selector):
                        recaptcha_box = self.driver.find_elements_by_css_selector(
                            self.recaptcha_selector)[0]
                        recaptcha_box.click()
                last_reclick = self.reclick_delay

        time.sleep(1)

        if self.driver.current_url != self.app_home:
            print("AUTH ERR: Redirect not valid URL! Please press RETURN to continue...")
            input()
            return None

        l_storage = LocalStorage(self.driver)
        token = l_storage.get("token")
        token = token[1:-1]
        account.token = token

        self.logout(direct=True)

        return account


# args
argument_list = argv[1:]
if len(argument_list) > 0 and argument_list[0] == "help":
    print(":: HELP ::\n$ generator.py <number of alt-tokens to generate> <your windows username> [register delay (seconds) | default: 30] [save userdata |default: false] [tokens file name (Without extension) | default: t_<timecode>]\n\n:: INFO ::\nFor this generator, you need to have Chrome installed on this machine. Then you need to go to https://chromedriver.chromium.org/downloads and download the version of chromedriver according to your installed version of Chrome and put chromedriver.exe in the same folder with this script.\n\nYour windows username is required to get your Chrome config to bypass recaptcha.\n\nThe alt-tokens get saved into the tokens folder\n")
    exit(0)

if len(argument_list) < 2:
    print("ERROR!\n$ generator.py help\nfor more infos.\n")
    exit(1)

if len(argument_list) > 2 and argument_list[2].isnumeric():
    register_delay = int(argument_list[2])
    print("Register delay:", register_delay)
else:
    register_delay = 30

if len(argument_list) > 3 and argument_list[3].lower() in ['true', '1', 't', 'y', 'yes']:
    save_userdata = True
    print("Save userdata")
else:
    save_userdata = False

if len(argument_list) > 4:
    tokens_file_name = argument_list[4] + ".txt"
    print("Tokens filename:", tokens_file_name)
else:
    file_id = int(datetime.datetime.utcnow().timestamp())
    tokens_file_name = "t_" + str(file_id) + ".txt"

if not argument_list[0].isnumeric():
    print("ERROR!\n$ generator.py help\nfor more infos.\n")
    exit(1)

alt_tokens_count = int(argument_list[0])
windows_username = argument_list[1]
chrome_user_data_dir = "C:\\Users\\" + \
    windows_username + "\\AppData\\Local\\Google\\Chrome\\User Data - Discord Alt-Token Generator"


# setup
print("Setup...")

if not path.isdir("tokens"):
    mkdir("tokens")

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + chrome_user_data_dir)
driver = webdriver.Chrome(options=options)
current_bot = Bot(driver, display_userdata=save_userdata)
if not path.isfile("tokens/" + tokens_file_name):
    f = open("tokens/" + tokens_file_name, "w")
    f.close()

# loop
print("\nStarting loop...\n")
for i in range(0, alt_tokens_count):
    account = current_bot.generate_token()

    if account != None:
        with open("tokens/" + tokens_file_name, "a+") as f:
            if save_userdata:
                f.write("Mail: " + account.email + " Username: " +
                        account.username + "Password: " + account.password + "Token: " + account.token + "\n")
            else:
                f.write(account.token + "\n")

        time.sleep(register_delay)

print("\nDONE Generarating " + str(alt_tokens_count) + " alt-tokens.")

driver.close()
driver.quit()
