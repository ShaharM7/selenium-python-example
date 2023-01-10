from dependency_injector import providers, containers

from p_automation.drivers.awaiter import Awaiter
from p_automation.drivers.chrome_browser import ChromeBrowser
from p_automation.drivers.options.browser_options import BrowserOptions
from p_automation.drivers.remote_browser import RemoteBrowser
from p_automation.pages.github_home_page import GitHubHomePage


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration(json_files=["./appsettings.json"])


class Drivers(containers.DeclarativeContainer):
    awaiter = providers.Singleton(Awaiter)
    chrome_browser = providers.Singleton(ChromeBrowser)
    remote_browser = providers.Singleton(RemoteBrowser)


class Pages(containers.DeclarativeContainer):
    git_hub_home_page = providers.Singleton(GitHubHomePage, Configs.config)


class Options(containers.DeclarativeContainer):
    browser_options = providers.Singleton(BrowserOptions, Configs.config)
