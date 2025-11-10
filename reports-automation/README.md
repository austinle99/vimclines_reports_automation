# VLines Weekly Reports Automation

Automated PowerPoint report generation system for VLines weekly shipping reports using Python and `python-pptx`.

## Features

- **Automated Report Generation**: Generate weekly reports automatically every Monday at 9 AM
- **Template-Based**: Uses PowerPoint templates to preserve formatting and fonts
- **Multiple Data Sources**: Support for JSON files, REST APIs, and databases
- **Flexible Scheduling**: Configurable schedule via YAML configuration
- **Manual Generation**: Run reports on-demand for testing
- **Clean Architecture**: Modular design with separate concerns

## Project Structure

```
reports-automation/
├── config/
│   └── config.yaml              # Main configuration file
├── scripts/
│   ├── __init__.py
│   ├── data_fetcher.py          # Fetches data from various sources
│   ├── generator.py             # Generates PowerPoint reports
│   └── scheduler.py             # Handles scheduling and automation
├── templates/
│   └── weekly_report_template.pptx  # PowerPoint template (create this)
├── reports/                     # Generated reports output here
├── logs/                        # Application logs
├── data/                        # Sample/test data files
├── tests/                       # Unit tests
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore
└── README.md
```

## Prerequisites

- **Python 3.8+** (Recommended: Python 3.11)
- **pip** (Python package installer)
- **PowerPoint** (Microsoft Office) to create the template

## Installation

### Step 1: Set Up Virtual Environment

```bash
# Navigate to the project directory
cd reports-automation

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Create Configuration

```bash
# Copy environment variables template
copy .env.example .env

# Edit .env with your actual values
notepad .env
```

### Step 4: Create PowerPoint Template

1. Open Microsoft PowerPoint
2. Design your weekly report slides with the desired formatting
3. Add placeholder text for dynamic data:
   - Use format: `{{PLACEHOLDER_NAME}}`
   - Example: `{{TOTAL_RECEIVABLES}}`, `{{REPORT_WEEK}}`
4. Save as `templates/weekly_report_template.pptx`

**Placeholder Examples:**
- `{{REPORT_WEEK}}` - Week number (e.g., "2025-W43")
- `{{REPORT_DATE}}` - Report date
- `{{TOTAL_RECEIVABLES}}` - Total receivables amount
- `{{WITHIN_TERM_RECEIVABLES}}` - Receivables within term
- `{{OVERDUE_RECEIVABLES}}` - Overdue receivables
- `{{TOTAL_PAYABLES}}` - Total payables amount
- And more... (see `config/config.yaml`)

## Configuration

Edit `config/config.yaml` to customize:

### Data Source

```yaml
data_source:
  type: json  # Options: json, api, database
  url: http://localhost:3001/api/weekly-reports/data
  json_path: data/weekly_data.json
```

### Schedule

```yaml
schedule:
  day: monday  # Day of the week
  time: "09:00"  # 24-hour format
```

### Output

```yaml
output:
  directory: ./reports
  filename_pattern: VLines_Weekly_Report_{date}.pptx
```

## Usage

### Option 1: Generate Report Immediately

```bash
# Activate virtual environment first
venv\Scripts\activate

# Run report generation now
python scripts/scheduler.py --now
```

### Option 2: Start Scheduled Automation

```bash
# Activate virtual environment
venv\Scripts\activate

# Start scheduler (will run weekly)
python scripts/scheduler.py
```

The scheduler will:
- Run every Monday at 9:00 AM (configurable)
- Fetch data from configured source
- Generate PowerPoint report
- Save to `reports/` directory
- Keep running until you press Ctrl+C

### Option 3: Test Individual Components

```bash
# Test data fetcher
python scripts/data_fetcher.py

# Test report generator
python scripts/generator.py
```

## Data Structure

The system expects data in the following format:

```json
{
  "metadata": {
    "week": "2025-W43",
    "generated_at": "2025-10-29T10:00:00",
    "report_type": "weekly"
  },
  "tckt": {
    "overview": {
      "receivables": {
        "total": 112282563,
        "within_term": 107816808,
        "overdue": 3465756
      },
      "payables": {
        "total": 157050197,
        "within_term": 73185728,
        "overdue": 83864469
      }
    }
  },
  "ops": {
    "ship_schedule": [ /* ... */ ]
  },
  "kinh_doanh": {
    "market_overview": { /* ... */ }
  }
}
```

See `scripts/data_fetcher.py` for complete data structure.

## Connecting to Your Frontend

### Option A: Create Backend API

Add an Express API to serve data:

```javascript
// In one-data-fe/backend/server.js
app.get('/api/weekly-reports/data', (req, res) => {
  const data = fetchDataFromDatabase(); // Your logic
  res.json(data);
});
```

Then configure:
```yaml
data_source:
  type: api
  url: http://localhost:3001/api/weekly-reports/data
```

### Option B: Export JSON from Frontend

Create a data export function in React and save as JSON file:

```typescript
// In your React app
export const exportWeeklyData = () => {
  const data = getAllReportData();
  downloadJSON(data, 'weekly_data.json');
};
```

Then configure:
```yaml
data_source:
  type: json
  json_path: data/weekly_data.json
```

## Deployment

### Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Weekly, Monday, 9:00 AM
4. Action: Start a program
   - Program: `C:\Path\to\venv\Scripts\python.exe`
   - Arguments: `scripts\scheduler.py --now`
   - Start in: `C:\Path\to\reports-automation`

### Linux Cron Job

```bash
# Edit crontab
crontab -e

# Add line (runs every Monday at 9 AM)
0 9 * * 1 /path/to/venv/bin/python /path/to/scripts/scheduler.py --now
```

### Cloud Deployment (AWS Lambda, Azure Functions)

1. Package the project with dependencies
2. Create Lambda function / Azure Function
3. Set up CloudWatch Event / Timer Trigger for weekly execution
4. Store template in S3 / Azure Blob Storage

## Troubleshooting

### Issue: Template not found

**Solution:** Create `templates/weekly_report_template.pptx` or update path in `config/config.yaml`

### Issue: Fonts don't match template

**Solution:**
1. Ensure template fonts are embedded: File > Options > Save > Embed fonts
2. Install the same fonts on the server where script runs
3. Use system fonts (Arial, Calibri) as fallbacks

### Issue: Data not loading

**Solution:**
1. Check `config/config.yaml` data source settings
2. Verify API is running (if using API)
3. Check JSON file exists (if using JSON)
4. Review logs in `logs/reports_automation.log`

### Issue: Import errors

**Solution:**
```bash
# Ensure virtual environment is activated
venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

## Development

### Running Tests

```bash
# Install dev dependencies
pip install pytest

# Run tests
pytest tests/
```

### Adding New Features

1. **New Data Source**: Extend `DataFetcher` class in `data_fetcher.py`
2. **New Slide Type**: Add methods to `WeeklyReportGenerator` in `generator.py`
3. **Notifications**: Implement in `scheduler.py` `_post_process()` method

## Best Practices

### Font Preservation

Always update text at the **run level** to preserve formatting:

```python
# ❌ BAD - Loses formatting
shape.text = "New text"

# ✅ GOOD - Preserves formatting
for paragraph in shape.text_frame.paragraphs:
    for run in paragraph.runs:
        if "{{PLACEHOLDER}}" in run.text:
            run.text = run.text.replace("{{PLACEHOLDER}}", "Actual value")
```

### Template Design

- Use consistent placeholder naming: `{{UPPER_CASE_WITH_UNDERSCORES}}`
- Document all placeholders in template
- Test with sample data before production
- Embed fonts in template file

### Data Validation

Always validate data before generating reports:

```python
def validate_data(data):
    required_keys = ['metadata', 'tckt', 'ops', 'kinh_doanh']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
```

## Support

For issues or questions:
1. Check this README
2. Review `config/config.yaml` comments
3. Check logs in `logs/reports_automation.log`
4. Review code comments in Python scripts

## License

Internal use only - VLines Corporation

## Version History

- **v1.0.0** (2025-10-29): Initial release
  - Basic PowerPoint generation
  - Support for JSON and API data sources
  - Weekly scheduling
  - Template-based formatting preservation
