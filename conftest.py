import base64
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Interceptează testele și adaugă capturi de ecran în format Base64 
    direct în raportul HTML dacă testul pică.
    """
    outcome = yield
    report = outcome.get_result()
    
    # Verificăm dacă pasul actual a picat (Failing)
    if report.when == "call" and report.failed:
        pytest_html = item.config.pluginmanager.getplugin("html")
        if pytest_html and "page" in item.funcargs:
            page = item.funcargs["page"]
            
            # Realizăm screenshot-ul și îl decodificăm în Base64
            screenshot_bytes = page.screenshot(full_page=True)
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
            
            # Adăugăm imaginea folosind noul sistem de extras din pytest-html v4+
            report.extras = getattr(report, "extras", [])
            report.extras.append(pytest_html.extras.png(screenshot_base64, name="Screenshot Eroare"))
