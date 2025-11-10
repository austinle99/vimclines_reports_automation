# Quick Start Guide

Get your VLines weekly reports automation up and running in 5 minutes!

## Prerequisites Check

Before starting, make sure you have:
- [ ] Python 3.8 or higher installed
- [ ] pip (Python package manager) installed
- [ ] Microsoft PowerPoint (to create template)

Check Python version:
```bash
python --version
```

## Step-by-Step Setup

### 1. Set Up Python Environment (2 minutes)

```bash
# Navigate to project
cd reports-automation

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

You should see `(venv)` in your terminal prompt when activated.

### 2. Configure Environment Variables (1 minute)

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Edit `.env` if needed (optional for now - defaults will work).

### 3. Update Configuration (1 minute)

The default `config/config.yaml` is already set up for testing with sample data.

For now, keep it as-is. You can customize later.

### 4. Test the System (1 minute)

```bash
# Test data fetcher
python scripts/data_fetcher.py

# Test report generator (will use sample data)
python scripts/scheduler.py --now
```

Check the `reports/` folder - you should see a generated PowerPoint file!

### 5. Create Your Template (Optional)

For production use, create a PowerPoint template:

1. Open PowerPoint
2. Design your slides
3. Add placeholders like `{{TOTAL_RECEIVABLES}}`
4. Save as `templates/weekly_report_template.pptx`

See `templates/README.md` for detailed instructions.

## Common Commands

```bash
# Generate report immediately
python scripts/scheduler.py --now

# Start scheduler (runs weekly)
python scripts/scheduler.py

# Test data fetcher
python scripts/data_fetcher.py

# Show help
python scripts/scheduler.py --help
```

## Next Steps

1. **Connect to Your Frontend**
   - Option A: Create backend API (see README.md)
   - Option B: Export JSON from React app

2. **Create PowerPoint Template**
   - See `templates/README.md` for guide

3. **Schedule Automation**
   - Windows: Task Scheduler
   - Linux: Cron job
   - See README.md for instructions

4. **Customize Configuration**
   - Edit `config/config.yaml`
   - Set data source (JSON, API, database)
   - Configure schedule (day/time)

## Troubleshooting

**Issue: ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

**Issue: No template file**
- The system will work without template (creates basic slides)
- For production, create template as described above

**Issue: Permission denied**
- Close any open PowerPoint files
- Make sure `reports/` folder exists
- Check file permissions

## Getting Help

1. Read `README.md` for detailed documentation
2. Check `config/config.yaml` comments
3. Review logs in `logs/reports_automation.log`
4. Examine Python script comments

## Success Indicators

You're ready for production when:
- ✅ `python scripts/scheduler.py --now` generates a report
- ✅ Report appears in `reports/` folder
- ✅ Report opens in PowerPoint without errors
- ✅ Template (if created) preserves formatting
- ✅ Data populates correctly

Congratulations! Your automation system is ready.
