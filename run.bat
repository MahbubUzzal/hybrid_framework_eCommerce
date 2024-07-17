@echo off
cd /d "%~dp0"

:: Option 1: Activate the virtual environment
:: Uncomment and adjust the path to your virtual environment
C:\Users\mahbu\PycharmProjects\hybrid_framework\venv\Scripts\activate

:: Option 2: Ensure Python and pytest are in the PATH when you are not using virtual environment
:: Adjust the paths to your Python installation and Scripts directory
::set PATH=C:\Users\mahbu\AppData\Local\Programs\Python\Python311;C:\Users\mahbu\AppData\Local\Programs\Python\Python311\Scripts;%PATH%

:: Run pytest with arguments
pytest -v -s -m "regression" --html=../reports/report.html test_cases/ --browser chrome

pause

