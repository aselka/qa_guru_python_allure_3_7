import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity
from allure_commons.types import AttachmentType


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'aselka')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории, без шагов')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')
    s('.header-search-input').click()
    s('.header-search-input').send_keys('aselka/qa_guru_python_allure_3_7')
    s('.header-search-input').submit()
    s(by.link_text('aselka/qa_guru_python_allure_3_7')).click()
    s('#issues-tab').click()
    s(by.partial_text('#1')).should(be.visible)


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'aselka')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории, с лямбда шагами')
@allure.link('https://github.com', name='Testing')
def test_dinamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('aselka/qa_guru_python_allure_3_7')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('aselka/qa_guru_python_allure_3_7')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 1'):
        s(by.partial_text('#1')).should(be.visible)

    with allure.step('Создаем скриншот'):
        allure.attach(browser.driver.get_screenshot_as_png(), name='Screen', attachment_type=AttachmentType.PNG)


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'aselka')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории, с декораторами')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository('aselka/qa_guru_python_allure_3_7')
    go_to_repository('aselka/qa_guru_python_allure_3_7')
    open_issue_tab()
    should_see_issue_with_number('#1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    s("#issues-tab").click()


@allure.step('Проверяем наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()