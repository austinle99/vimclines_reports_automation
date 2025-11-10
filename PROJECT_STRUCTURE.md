# VLines Workspace - Project Structure

This workspace contains two separate projects for VLines weekly reports system.

## Workspace Overview

```
vlines-workspace/
├── one-data-fe/                      # React Frontend (Git tracked)
│   ├── .git/                         # Git repository
│   ├── src/
│   │   ├── features/
│   │   │   └── shipping/
│   │   │       └── components/       # Weekly reports UI components
│   │   │           ├── TCKT/
│   │   │           ├── OPS/
│   │   │           ├── KinhDoanh/
│   │   │           ├── EQC/
│   │   │           ├── ThuongVu/
│   │   │           └── TongQuanTinhHinhTau/
│   │   └── modules/
│   │       └── Miscellaneous/
│   │           ├── ReportsSelectionPage/
│   │           └── ShippingPage/
│   ├── package.json
│   └── ...
│
├── reports-automation/               # Python Automation (Can be Git tracked separately)
│   ├── scripts/
│   │   ├── __init__.py
│   │   ├── data_fetcher.py          # Fetches data from API/JSON/DB
│   │   ├── generator.py             # Generates PowerPoint reports
│   │   └── scheduler.py             # Weekly scheduling automation
│   ├── templates/
│   │   ├── README.md                # Template creation guide
│   │   └── weekly_report_template.pptx  # (Create this file)
│   ├── reports/                     # Generated reports (gitignored)
│   ├── logs/                        # Application logs (gitignored)
│   ├── data/
│   │   └── sample_data.json         # Sample data for testing
│   ├── config/
│   │   └── config.yaml              # Main configuration
│   ├── tests/                       # Unit tests (to be added)
│   ├── requirements.txt             # Python dependencies
│   ├── .env.example                 # Environment variables template
│   ├── .gitignore
│   ├── README.md                    # Full documentation
│   ├── QUICKSTART.md                # Quick start guide
│   ├── setup.bat                    # Windows setup script
│   └── setup.sh                     # Linux/Mac setup script
│
└── vlines-workspace.code-workspace   # VS Code workspace file
```

## Two Independent Projects

### 1. Frontend (one-data-fe)
- **Technology**: React + TypeScript + Vite
- **Purpose**: Web UI for weekly reports display
- **Git**: Tracked, pushes to GitLab
- **Data**: Currently hardcoded in components
- **Location**: `one-data-fe/`

### 2. Python Automation (reports-automation)
- **Technology**: Python 3.8+ with python-pptx
- **Purpose**: Automated PowerPoint report generation
- **Git**: Not tracked (optional separate repo)
- **Data**: Fetches from API/JSON/Database
- **Location**: `reports-automation/`

## Git Tracking Explanation

### Current Setup:
```
vlines-workspace/              ← No .git (just a folder)
├── one-data-fe/              ← HAS .git → Pushes to GitLab
└── reports-automation/       ← NO .git → Stays local
```

### When You Push from one-data-fe:
```bash
cd vlines-workspace/one-data-fe
git add .
git commit -m "Update reports"
git push origin feature/vlines-weekly-reports
```
**Result**: Only `one-data-fe` files are pushed. The `reports-automation` folder is invisible to Git.

### Optional: Track Python Project Separately
If you want to version control the Python project:
```bash
cd vlines-workspace/reports-automation
git init
git remote add origin <your-new-gitlab-repo-url>
git add .
git commit -m "Initial Python automation project"
git push -u origin main
```

## How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│                                                               │
│  React Frontend (one-data-fe)                                │
│  - Displays weekly reports in browser                        │
│  - Hardcoded data (to be changed to API)                    │
│                                                               │
└──────────────────┬────────────────────────────────────────────┘
                   │
                   │ Future: REST API
                   │ GET /api/weekly-reports/data
                   │
┌──────────────────▼────────────────────────────────────────────┐
│                                                               │
│  Backend API (To be created)                                 │
│  - Express.js or FastAPI                                     │
│  - Serves report data as JSON                                │
│  - Connects to database                                      │
│                                                               │
└──────────────────┬────────────────────────────────────────────┘
                   │
                   │ HTTP Request
                   │
┌──────────────────▼────────────────────────────────────────────┐
│                                                               │
│  Python Automation (reports-automation)                      │
│  - Fetches data from API                                     │
│  - Generates PowerPoint (.pptx) files                        │
│  - Runs weekly via scheduler                                 │
│  - Preserves formatting from template                        │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## Development Workflow

### Working on Frontend
```bash
cd vlines-workspace/one-data-fe
npm run dev

# Make changes...

git add .
git commit -m "Update UI"
git push
```

### Working on Python Automation
```bash
cd vlines-workspace/reports-automation
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Test immediately
python scripts/scheduler.py --now

# Start weekly scheduler
python scripts/scheduler.py
```

### Opening Both in VS Code
```bash
cd vlines-workspace
code vlines-workspace.code-workspace
```

This opens both projects in a single VS Code window with:
- Separate folders in sidebar
- Python virtual environment auto-detected
- Integrated terminals for each project
- Debug configurations for Python scripts

## Next Steps

1. **Move Frontend Project** (if not done yet):
   ```bash
   # Close VS Code first
   cd C:\Users\LêNgọcMinh\Downloads
   mv one-data-fe vlines-workspace/
   ```

2. **Set Up Python Environment**:
   ```bash
   cd vlines-workspace/reports-automation
   setup.bat  # Windows
   ./setup.sh  # Mac/Linux
   ```

3. **Test Python Automation**:
   ```bash
   cd vlines-workspace/reports-automation
   venv\Scripts\activate
   python scripts/scheduler.py --now
   ```

4. **Create PowerPoint Template**:
   - See `reports-automation/templates/README.md`

5. **Connect Frontend to Backend**:
   - Create API to serve data
   - Update React components to fetch from API
   - Python script fetches from same API

## Key Files to Review

### Configuration:
- `reports-automation/config/config.yaml` - Main settings
- `reports-automation/.env.example` - Environment variables

### Documentation:
- `reports-automation/README.md` - Full documentation
- `reports-automation/QUICKSTART.md` - Quick start
- `reports-automation/templates/README.md` - Template guide

### Code:
- `reports-automation/scripts/data_fetcher.py` - Data fetching
- `reports-automation/scripts/generator.py` - PowerPoint generation
- `reports-automation/scripts/scheduler.py` - Automation scheduling

## Important Notes

1. **Git Tracking**:
   - `one-data-fe` is tracked and pushes to GitLab
   - `reports-automation` is NOT tracked (stays local unless you init Git)

2. **Data Flow**:
   - Current: Hardcoded in React components
   - Future: React → API → Database ← Python script

3. **Template Required**:
   - Python scripts work without template (creates basic slides)
   - For production: Create `templates/weekly_report_template.pptx`

4. **Scheduling**:
   - Development: Run manually with `--now` flag
   - Production: Windows Task Scheduler or Linux cron

## Support

- Frontend issues: Check React code in `one-data-fe/src/`
- Python issues: Check logs in `reports-automation/logs/`
- Configuration: Review `config/config.yaml`
- Setup help: See `QUICKSTART.md`

## Version Control

### Frontend (one-data-fe):
```bash
cd one-data-fe
git status          # Check changes
git add .           # Stage changes
git commit -m "..."  # Commit
git push            # Push to GitLab
```

### Python (reports-automation):
Option 1: Keep local (no Git)
Option 2: Create separate repo
```bash
cd reports-automation
git init
git remote add origin <url>
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

**Status**: ✅ Complete and ready to use!

**Last Updated**: 2025-10-29
