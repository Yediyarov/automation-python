# Automated Web Testing Framework

This repository contains an automated testing framework built using Python and Selenium. The framework is designed for end-to-end UI testing of web applications, incorporating modular page objects, reusable locators, and detailed reporting capabilities.

---

## Key Features

- **Page Object Model (POM):** Organized code structure with separate modules for locators and page actions.
- **Test Scenarios:** Covers various UI interactions including form filling, button clicks, file uploads, and downloads.
- **Dynamic Data Generation:** Utilizes Faker to generate random test data for inputs.
- **Allure Reports:** Provides comprehensive test execution reports with screenshots for failed tests.
- **Error Handling:** Robust error handling with automated screenshot capture on test failures.

---

## Project Structure

```plaintext
.
├── README.md             # Project documentation
├── conftest.py           # Pytest fixtures and configurations
├── data/                 # Data classes and helpers
│   └── data.py
├── generator/            # Data generators for test inputs
│   └── generator.py
├── locators/             # Web element locators for pages
│   ├── __init__.py
│   ├── elements_page_locators.py
│   └── form_page_locators.py
├── pages/                # Page object classes
│   ├── __init__.py
│   ├── base_page.py
│   ├── elements_page.py
│   └── form_page.py
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
├── screenshots/          # Screenshots captured during tests
│   ├── test_check_box.png
│   └── test_radio_button.png
└── tests/                # Test cases
    ├── __init__.py
    ├── elements_test.py
    └── form_test.py
```

---

## Prerequisites

- Python 3.8 or higher
- Google Chrome browser and the latest ChromeDriver
- Recommended: Virtual environment for Python dependencies

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Yediyarov/automation-python.git
    ```

2. Navigate to the project directory:
    ```bash
    cd automation-python
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Running Tests

1. Ensure ChromeDriver is installed and available in your PATH.
2. Run the tests using Pytest:
    ```bash
    pytest --alluredir=allure-results
    ```

### Viewing Reports

1. Generate Allure reports:
    ```bash
    allure serve allure-results
    ```
2. Open the generated report in your browser.

---

## Customization

- **Test Data:** Modify `generator/generator.py` to customize random data generation.
- **Locators:** Update locators in `locators/` for web elements specific to your application.
- **Configurations:** Adjust settings in `pytest.ini` and `conftest.py` to match your environment.

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add new feature'
    ```
4. Push to your branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contact

Developed by [Khayal Yediyarov](https://github.com/Yediyarov). Feel free to reach out with any questions or suggestions!
