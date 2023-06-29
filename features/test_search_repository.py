from screenpy import Actor,given, when, then, and_
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open, Enter, Wait, SaveScreenshot
from screenpy.resolutions import ContainsTheText
from screenpy_selenium.questions import Text
from allure_commons.types import AttachmentType

from selenium.webdriver.common.keys import Keys

from locators.GithubHomePage import search_input, URL
from locators.ResultPage import results

@act("realizar una búsqueda en github")
@scene("buscar el repositorio del tutorial de selenium en github")
def test_search_for_screenpy_selenium_tutorial_repository(Usuario: Actor)->None:
    """Se espera que el usuario inicie el navegador"""
    given(Usuario).was_able_to(Open.their_browser_on(URL))
    """Posteriormente se indican las acciones que el usuario va a realizar"""
    when(Usuario).attempts_to(
        Enter.the_text('jardilac91/Screenpy-selenium-example').into_the(search_input).then_hit(Keys.RETURN),
        Wait.for_the(results).to_appear()
    )
    """Por último se espera que el usuario pueda ver el texto en el item de búsqueda"""
    then(Usuario).should(
        See.the(Text.of_the(results), ContainsTheText('repository result'))
    )
