#!/bin/bash
# VLines Weekly Reports Automation - Linux/Mac Setup Script

echo "========================================"
echo "VLines Weekly Reports Automation Setup"
echo "========================================"
echo ""

# Check Python installation
echo "[1/5] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
python3 --version
echo ""

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "Virtual environment created successfully"
fi
echo ""

# Activate virtual environment and install dependencies
echo "[3/5] Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt
echo ""

# Create .env file if it doesn't exist
echo "[4/5] Setting up configuration..."
if [ -f ".env" ]; then
    echo ".env file already exists, skipping..."
else
    cp .env.example .env
    echo ".env file created from template"
fi
echo ""

# Create necessary directories
echo "[5/5] Creating directories..."
mkdir -p reports logs data
echo "Directories created successfully"
echo ""

echo "========================================"
echo "Setup completed successfully!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Create PowerPoint template: templates/weekly_report_template.pptx"
echo "2. Test the system: source venv/bin/activate && python scripts/scheduler.py --now"
echo "3. Configure data source in config/config.yaml"
echo "4. Review QUICKSTART.md for detailed instructions"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To generate a report now:"
echo "  python scripts/scheduler.py --now"
echo ""
