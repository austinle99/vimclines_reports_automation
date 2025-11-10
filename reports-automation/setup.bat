@echo off
REM VLines Weekly Reports Automation - Windows Setup Script

echo ========================================
echo VLines Weekly Reports Automation Setup
echo ========================================
echo.

REM Check Python installation
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
python --version
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo Virtual environment created successfully
)
echo.

REM Activate virtual environment and install dependencies
echo [3/5] Installing dependencies...
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo.

REM Create .env file if it doesn't exist
echo [4/5] Setting up configuration...
if exist .env (
    echo .env file already exists, skipping...
) else (
    copy .env.example .env
    echo .env file created from template
)
echo.

REM Create necessary directories
echo [5/5] Creating directories...
if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist data mkdir data
echo Directories created successfully
echo.

echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Create PowerPoint template: templates\weekly_report_template.pptx
echo 2. Test the system: venv\Scripts\activate then python scripts\scheduler.py --now
echo 3. Configure data source in config\config.yaml
echo 4. Review QUICKSTART.md for detailed instructions
echo.
echo To activate the virtual environment:
echo   venv\Scripts\activate
echo.
echo To generate a report now:
echo   python scripts\scheduler.py --now
echo.
pause
