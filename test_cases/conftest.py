import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):     # This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):   # This will return the browser value to the setup method
    return request.config.getoption("--browser")


##########   Pytest HTML Report   ##########

# It is the hook for adding Environment info to HTML report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Uzzal'


# It is the hook to delete or modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)
