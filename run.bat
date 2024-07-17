@echo off
echo Changing directory to the batch file location
cd /d %~dp0
echo Running pytest
pytest -v -s -m "sanity" --html=../reports/report.html test_cases/ --browser chrome
rem pytest -v -s -m "sanity" --html=../reports/report.html test_cases/ --browser firefox
echo Pytest finished
pause
