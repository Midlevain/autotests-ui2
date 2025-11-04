from pages.dashboard.dashboard_page import DashboardPage
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent
import pytest

@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(
        self,
        dashboard_page_with_state: DashboardPage,
        dashboard_toolbar_view_component: DashboardToolbarViewComponent,
        students_chart_component: ChartViewComponent,
        activities_chart_component: ChartViewComponent,
        courses_chart_component: ChartViewComponent,
        scores_chart_component: ChartViewComponent

    ):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_title.check_visible()
        dashboard_page_with_state.students_chart.check_visible('Students')
        dashboard_page_with_state.activities_chart.check_visible('Activities')
        dashboard_page_with_state.courses_chart.check_visible('Courses')
        dashboard_page_with_state.scores_chart.check_visible('Scores')