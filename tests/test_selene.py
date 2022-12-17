import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'aselka')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
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