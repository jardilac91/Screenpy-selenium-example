from screenpy import Actor,given, when, then, and_
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open, Enter, Wait, SaveScreenshot
from screenpy.resolutions import ContainsTheText
from screenpy_selenium.questions import Text
from allure_commons.types import AttachmentType

from selenium.webdriver.common.keys import Keys

from features.conftest import URL


from locators.SearchPage import search_input
from locators.ResultPage import result, result_section

@act("realizar una búsqueda en google")
@scene("buscar la documentación de screenpy en google")
def test_search_for_screenpy(Usuario: Actor)->None:
    """Se espera que el usuario inicie el navegador"""
    given(Usuario).was_able_to(Open.their_browser_on(URL))
    """Posteriormente se indican las acciones que el usuario va a realizar"""
    when(Usuario).attempts_to(
        Enter.the_text('screenpy').into_the(search_input).then_hit(Keys.RETURN),
        Wait.for_the(result_section).to_appear(),
        SaveScreenshot.as_("page.png").and_attach_it(
            name="error", attachment_type=AttachmentType.PNG
        ),
        Wait.for_the(result).to_appear()
    )
    """Por último se espera que el usuario pueda ver el texto en el item de búsqueda"""
    then(Usuario).should(
        See.the(Text.of_the(result), ContainsTheText('ScreenPy: Screenplay Pattern for Python!'))
    )
