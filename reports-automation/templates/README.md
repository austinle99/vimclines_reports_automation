# PowerPoint Templates

## Creating Your Weekly Report Template

### Step 1: Design the Template

1. Open Microsoft PowerPoint
2. Create slides for each department:
   - Title Slide
   - TCKT (Accounting)
   - OPS (Operations)
   - Kinh Doanh (Business)
   - EQC
   - Thuong Vu
   - Tong Quan Tau

3. Apply your desired formatting:
   - Fonts (e.g., Arial, Calibri)
   - Colors (VLines brand colors)
   - Layouts
   - Company logo

### Step 2: Add Placeholders

Use double curly braces for dynamic data:

```
{{PLACEHOLDER_NAME}}
```

#### Example Placeholders:

**Metadata:**
- `{{REPORT_WEEK}}` - e.g., "2025-W43"
- `{{REPORT_DATE}}` - e.g., "2025-10-29"
- `{{GENERATED_DATE}}` - When report was generated

**TCKT (Accounting):**
- `{{TOTAL_RECEIVABLES}}` - Total receivables
- `{{WITHIN_TERM_RECEIVABLES}}` - Within term amount
- `{{OVERDUE_RECEIVABLES}}` - Overdue amount
- `{{TOTAL_PAYABLES}}` - Total payables
- `{{WITHIN_TERM_PAYABLES}}` - Within term payables
- `{{OVERDUE_PAYABLES}}` - Overdue payables
- `{{CURRENT_MONTH_CASH}}` - Current month cash
- `{{PREVIOUS_MONTH_CASH}}` - Previous month cash

**OPS (Operations):**
- `{{SHIP_NAME_1}}`, `{{SHIP_NAME_2}}`, etc.
- `{{VOYAGE_1}}`, `{{VOYAGE_2}}`, etc.
- Tables for ship schedules

**Kinh Doanh (Business):**
- `{{VLINES_MARKET_SHARE_HPH_HCM}}`
- `{{VLINES_MARKET_SHARE_HCM_HPH}}`
- Charts for market data

### Step 3: Embed Fonts

To ensure fonts display correctly on any machine:

1. Go to **File** > **Options** > **Save**
2. Check **"Embed fonts in the file"**
3. Select **"Embed all characters"** (increases file size but safer)
4. Click **OK**

### Step 4: Save Template

Save the file as:
```
weekly_report_template.pptx
```

Place it in this directory (`templates/`).

### Step 5: Test

Run the generator to test:
```bash
python scripts/scheduler.py --now
```

Check the output in `reports/` folder.

## Tips

1. **Keep it Simple**: Use placeholders for numbers/text that change weekly
2. **Static Content**: Leave explanatory text as-is in template
3. **Charts**: For now, generate as images and replace image placeholders
4. **Tables**: Use placeholders in table cells for dynamic data
5. **Formatting**: All formatting should be done in the template, not in code

## Template Naming Convention

- `weekly_report_template.pptx` - Main template (required)
- `weekly_report_template_backup.pptx` - Backup (optional)
- `monthly_report_template.pptx` - For future monthly reports

## Current Template Status

⚠️ **Action Required**: Please create `weekly_report_template.pptx`

The Python scripts are ready, but they need a template file to work with.
