@echo off
:: LeetCode Problem Sorter Batch Script
:: This script makes it easier to use the sort_problem.py utility

setlocal

:: Define base directory
set BASE_DIR=%~dp0

:: Display header
echo.
echo LeetCode Problem Sorter
echo ---------------------
echo.

:: Check if Python is installed
python --version > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
  echo Python is not installed or not in PATH.
  echo Please install Python 3.6 or later.
  goto :eof
)

:: Check and install required packages
echo Checking for required Python packages...
python -m pip install -r requirements.txt > nul 2>&1

:: Get the file path
set /p FILE_PATH=Enter the path to your solution file (e.g., contains_duplicate.cpp): 

:: Check if file exists
if not exist "%FILE_PATH%" (
  echo File not found: %FILE_PATH%
  goto :eof
)

:: Get LeetCode URL
set /p LEETCODE_URL=Enter the LeetCode problem URL: 

:: Ask about using API
choice /C YN /M "Do you want to use OpenAI API for automatic classification"
if %ERRORLEVEL% EQU 1 (
  :: Use API
  set /p API_KEY=Enter your OpenAI API key (or press Enter to skip): 
  
  if not "%API_KEY%"=="" (
    python "%BASE_DIR%utils\sort_problem.py" "%FILE_PATH%" "%LEETCODE_URL%" --api-key "%API_KEY%"
  ) else (
    python "%BASE_DIR%utils\sort_problem.py" "%FILE_PATH%" "%LEETCODE_URL%" --manual
  )
) else (
  :: Manual classification
  python "%BASE_DIR%utils\sort_problem.py" "%FILE_PATH%" "%LEETCODE_URL%" --manual
)

echo.
echo Done.
pause
