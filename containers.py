from dependency_injector import containers, providers

from p_automation.drivers.awaiter import Awaiter
from p_automation.drivers.chrome_browser import ChromeBrowser
from p_automation.drivers.options.browser_options import BrowserOptions
from p_automation.drivers.remote_browser import RemoteBrowser
from p_automation.pages.github_home_page import GitHubHomePage


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(json_files=["./appsettings.json"])

    browser_options = providers.Singleton(BrowserOptions, config=config)

    chrome_browser = providers.Singleton(ChromeBrowser, browser_options=browser_options, config=config)
    remote_browser = providers.Singleton(RemoteBrowser, config=config, browser_options=browser_options)
    awaiter = providers.Singleton(Awaiter, config=config)

    git_hub_home_page = providers.Singleton(GitHubHomePage, chrome_browser=chrome_browser, awaiter=awaiter)
