# VLines Workspace

Complete development environment for VLines weekly reports system, containing both frontend and automation projects.

## Repository Structure

This workspace uses a **dual-repository approach**:

```
vlines-workspace/ (This GitHub repo)
├── one-data-fe/                    # Frontend (separate GitLab repo)
├── reports-automation/             # Python automation (tracked here)
├── PROJECT_STRUCTURE.md            # Detailed project documentation
├── NEXT_STEPS_FOR_CLAUDE.md       # Development roadmap
└── vlines-workspace.code-workspace # VS Code workspace config
```

## Projects

### 1. Frontend (one-data-fe)
- **Repository**: GitLab - `https://gitlab.com/demo4814803/onedata/one-data-fe.git`
- **Technology**: React + TypeScript + Vite
- **Purpose**: Web UI for weekly reports display
- **Managed independently** - has its own Git repository

### 2. Python Automation (reports-automation)
- **Repository**: Tracked in this GitHub workspace
- **Technology**: Python 3.8+ with python-pptx
- **Purpose**: Automated PowerPoint report generation
- **Fully version controlled** in this repository

## Quick Start for Remote Working

### First Time Setup

```bash
# 1. Clone the workspace from GitHub
git clone https://github.com/austinle99/vimclines_reports_automation.git vlines-workspace
cd vlines-workspace

# 2. Clone the frontend from GitLab
git clone https://gitlab.com/demo4814803/onedata/one-data-fe.git one-data-fe

# 3. Set up Python automation
cd reports-automation
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..

# 4. Set up frontend
cd one-data-fe
npm install
cd ..

# 5. Open workspace in VS Code
code vlines-workspace.code-workspace
```

## Development Workflow

### Working on Frontend

```bash
cd one-data-fe

# Create/switch branch
git checkout -b feature/your-feature

# Make changes, then commit
git add .
git commit -m "Your changes"

# Push to GitLab
git push origin feature/your-feature
```

### Working on Python Automation

```bash
# Make changes to reports-automation/

# Commit from workspace root
cd vlines-workspace
git add reports-automation/
git commit -m "Update Python automation"

# Push to GitHub
git push origin main
```

### Working on Both

If you make changes to both projects:

```bash
# 1. Commit frontend changes
cd one-data-fe
git add .
git commit -m "Frontend changes"
git push origin <branch-name>

# 2. Commit workspace changes
cd ..
git add reports-automation/ PROJECT_STRUCTURE.md
git commit -m "Workspace changes"
git push origin main
```

## Why Dual-Repository?

- **Frontend (GitLab)**: Company/team may already have GitLab workflow
- **Workspace (GitHub)**: Easy sharing for remote work, better for public collaboration
- **Independence**: Each project can be cloned and used separately if needed
- **Simplicity**: No submodule complexity, easier to understand and maintain

## Important Notes

1. **one-data-fe is NOT tracked** in this workspace Git repository
   - It has its own .git directory
   - Pushes/pulls independently to GitLab
   - The workspace .gitignore excludes it

2. **reports-automation IS tracked** in this workspace
   - Version controlled with workspace
   - Pushes to GitHub with workspace commits

3. **Both projects work together** in the same VS Code workspace
   - Open `vlines-workspace.code-workspace` in VS Code
   - Both projects visible in sidebar
   - Separate terminal for each project

## File Locations

- **Frontend code**: `one-data-fe/src/`
- **Python scripts**: `reports-automation/scripts/`
- **PowerPoint templates**: `reports-automation/templates/`
- **Generated reports**: `reports-automation/reports/`
- **Configuration**: `reports-automation/config/`

## Documentation

- [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) - Complete project architecture
- [NEXT_STEPS_FOR_CLAUDE.md](./NEXT_STEPS_FOR_CLAUDE.md) - Development roadmap
- [reports-automation/README.md](./reports-automation/README.md) - Python automation docs
- [reports-automation/QUICKSTART.md](./reports-automation/QUICKSTART.md) - Quick start guide

## Troubleshooting

### Missing one-data-fe folder?
```bash
cd vlines-workspace
git clone https://gitlab.com/demo4814803/onedata/one-data-fe.git one-data-fe
```

### Python dependencies not working?
```bash
cd reports-automation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend not starting?
```bash
cd one-data-fe
npm install
npm run dev
```

## Contributing

### Frontend Changes
- Create feature branch in `one-data-fe`
- Push to GitLab
- Create merge request on GitLab

### Workspace/Automation Changes
- Create feature branch in workspace
- Push to GitHub
- Create pull request on GitHub

---

**Last Updated**: 2025-11-10
**Workspace Version**: 1.0.0
