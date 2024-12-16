#CURRENTLY UNTESTED:
@echo off
:: Variables
set usr=%USERNAME%
set dest_dir=C:\Users\%usr%\Desktop\Auto_OS_Test

:: Ensure admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo "This script requires admin rights. Please run as administrator."
    pause
    exit /b 1
)

:: Check and Install Python
echo Checking Python installation...
python --version | find "3.12" >nul
if %errorlevel% neq 0 (
    echo Python 3.12 not detected. Installing Python 3.12...
    choco install python --version=3.12 -y || (
        echo "Failed to install Python. Ensure Chocolatey is installed."
        pause
        exit /b 1
    )
)

:: Install Python Dependencies
echo Installing Python dependencies...
pip install psutil ping3 platform colorama || (
    echo "Failed to install Python dependencies."
    pause
    exit /b 1
)

:: Create Desktop Directory
echo Setting up test directory...
if not exist "%dest_dir%" (
    mkdir "%dest_dir%" || (
        echo "Failed to create test directory."
        pause
        exit /b 1
    )
)
xcopy /E /I /Y ".\Automated_OS_Testing-main" "%dest_dir%" || (
    echo "Failed to copy test files."
    pause
    exit /b 1
)

:: Run Hardware Dump
cd "%dest_dir%"
if exist V2_HW_DUMP.bat (
    echo Running hardware dump...
    call V2_HW_DUMP.bat || (
        echo "Hardware dump failed."
        pause
        exit /b 1
    )
) else (
    echo "V2_HW_DUMP.bat not found!"
    pause
    exit /b 1
)

:: Run Main Test Script
echo Launching main test script...
python "%dest_dir%\Automated_OS_Testing-main\Auto_OS_Test_v2.py" || (
    echo "The script crashed or failed."
    pause
    exit /b 1
)

echo "Testing Completed. Please review logs for any missing information."
pause
