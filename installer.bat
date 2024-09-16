@echo off
setlocal

REM Function to prompt for yes/no input
:prompt
echo Installing TurtleWowSim...

REM Check for requirements.txt file
echo Checking for requirements...
if not exist requirements.txt (
    echo requirements.txt file not found. Please make sure it is in the same directory as this script.
    goto end
) else (
    echo requirements.txt found.
)

REM Check for Python installation
echo Checking for python...
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python is not installed. Installing Python...
    winget install python
    REM python
    REM Adding Python to PATH
    REM setx PATH "%PATH%;C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps"
) ELSE (
    echo Python is already installed.
)

REM Check for venv module
echo Checking for venv...
python -m venv --help >nul 2>&1
IF ERRORLEVEL 1 (
    echo venv module is not available. Ensure Python is installed properly.
) ELSE (
    echo venv module is available.
)

echo Creating virtual environment...
REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Upgrade pip
echo upgrading pip...
python -m pip install --upgrade pip

REM Install the requirements
echo Installing requirements...
echo This may take a few minutes...
pip install -r requirements.txt

goto end

:no
echo Installation canceled.

:end

REM Installation Complete
endlocal
pause