import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


accepted_langs = ['ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br',
                  'ro', 'ru', 'sk', 'uk', 'zh-hans']


def get_chrome_options(lang):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    return options


def get_firefox_profile(lang):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", lang)
    return fp


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    lang_help_text = 'Choose language: \n' + '\n'.join(accepted_langs)
    parser.addoption('--language', action='store', default='ru',
                     help=lang_help_text)


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language not in accepted_langs:
        error_message = "--language can be one of the next values: \n" + '\n'.join(accepted_langs)
        raise pytest.UsageError(error_message)

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=get_chrome_options(language))
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=get_firefox_profile(language))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
