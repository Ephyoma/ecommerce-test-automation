![CI](https://github.com/Ephyoma/ecommerce-test-automation/actions/workflows/python-tests.yml/badge.svg)
# E-Commerce Selenium Test Suite

## 💡 Objective
Automate a full purchase flow on [saucedemo.com](https://saucedemo.com) using Selenium and pytest.

## 🔧 Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run tests
```bash
pytest tests/
```

### 3. Generate HTML Report
```bash
pytest --html=report.html --self-contained-html
```

## 📂 Folder Structure
- `pages/` – Page Object Model scripts
- `tests/` – Test cases
- `screenshots/` – Confirmation screenshots
- `report.html` – Optional test report

## 🧪 Test Cases
- Login with valid and locked-out users
- Sort products by price
- Add items to cart and verify
- Complete checkout and validate order confirmation
- Screenshot capture of confirmation
- HTML reports with `pytest-html`

## ✅ Requirements
- Python 3.7+
- Google Chrome
