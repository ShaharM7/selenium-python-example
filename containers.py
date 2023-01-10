from dependency_injector import containers, providers

from drivers import chrome_browser
from drivers import remote_browser
from drivers import Awaiter
from drivers.chrome_browser import ChromeBrowser
from drivers.options.browser_options import BrowserOptions
from drivers import RemoteBrowser
from navigation.page_navigator import PageNavigator
from pages import GitHubHomePage


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(json_files=["./appsettings.json"])

    browser_options = providers.Singleton(BrowserOptions, config=config)
    chrome_browser = providers.Singleton(ChromeBrowser, options=browser_options)
    remote_browser = providers.Singleton(RemoteBrowser, config=config, browser_options=browser_options)

    # Add a provider that conditionally returns chrome_browser or remote_browser depending on the configuration value
    browser = providers.Factory(
        lambda config: chrome_browser
        if not config.remote_browser_config.use_selenium_grid
        else remote_browser)

    awaiter = providers.Singleton(Awaiter, browser=browser)
    github_home_page = providers.Singleton(GitHubHomePage, browser=browser, awaiter=awaiter)

    page_navigator = providers.Singleton(PageNavigator, browser=browser, github_home_page=github_home_page,config=config)
