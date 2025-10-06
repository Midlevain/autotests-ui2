import pytest

from fixtures.pages import registration_form_component
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from components.authentication.registration_form_component import RegistrationFormComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(
    registration_page: RegistrationPage,
    dashboard_page: DashboardPage,
    registration_form_component: RegistrationFormComponent,
    dashboard_toolbar_view_component: DashboardToolbarViewComponent
):
        registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_form_component.fill_registration_form(email="user.name@gmail.com",username="username",password="password")
        registration_page.click_registration_button()
        dashboard_page.dashboard_title.check_visible()