import os
import pytest


if __name__ == "__main__":

    # Create required folders automatically
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("allure-results", exist_ok=True)

    pytest.main([

        "-v",
        "--tb=short",
        "-n=0",

        # HTML Report
        "--html=reports/report.html",

        # Self-contained HTML Report
        "--self-contained-html",

        # Allure Reporting
        "--alluredir=allure-results",

        # Sequential execution only

        # =========================
        # SEQUENTIAL EXECUTION FLOW
        # =========================

        # Signup Features
        "step_definitions/test_signup_steps.py",

        # Login Features
        "step_definitions/test_login_steps.py",
        "step_definitions/test_invalid_login_steps.py",

        # Homepage Features
        "step_definitions/test_home_steps.py",

        # Product Features
        "step_definitions/test_product_steps.py",

        #failed test case
        "step_definitions/test_failed_steps.py",

        # Cart Features
        "step_definitions/test_cart_steps.py",

        # Checkout Features
        "step_definitions/test_checkout_steps.py",

        # Contact Features
        "step_definitions/test_contact_steps.py",

        # Logout Features
        "step_definitions/test_logout_steps.py",

        # Browser Refresh Validation
        "step_definitions/test_browser_refresh_steps.py",

        # Navigation Validation
        "step_definitions/test_navigation_steps.py"
    ])