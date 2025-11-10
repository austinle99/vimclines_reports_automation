"""
Report Scheduler
Handles automated scheduling of weekly report generation
"""

import schedule
import time
from datetime import datetime
from typing import Dict, Any
import yaml
from data_fetcher import DataFetcher
from generator import WeeklyReportGenerator


class ReportScheduler:
    """Schedules and executes weekly report generation"""

    def __init__(self, config_path: str = 'config/config.yaml'):
        self.config_path = config_path
        self.config = self._load_config()
        self.data_fetcher = DataFetcher(self.config)
        self.report_generator = WeeklyReportGenerator(self.config)

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
                print(f"Configuration loaded from {self.config_path}")
                return config
        except FileNotFoundError:
            print(f"Config file not found: {self.config_path}")
            print("Using default configuration")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration"""
        return {
            'data_source': {
                'type': 'json',
                'url': 'http://localhost:3001/api/weekly-reports/data',
                'json_path': 'data/weekly_data.json'
            },
            'output': {
                'directory': './reports',
                'filename_pattern': 'VLines_Weekly_Report_{date}.pptx'
            },
            'schedule': {
                'day': 'monday',
                'time': '09:00'
            },
            'template': {
                'path': './templates/weekly_report_template.pptx'
            }
        }

    def generate_report_job(self):
        """Job that generates the weekly report"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"\n{'='*60}")
            print(f"Starting weekly report generation at {timestamp}")
            print(f"{'='*60}")

            # Fetch data
            print("\n[1/3] Fetching data...")
            data = self.data_fetcher.fetch_data()
            print(f"✓ Data fetched successfully")

            # Generate report
            print("\n[2/3] Generating PowerPoint report...")
            output_path = self.report_generator.generate_report(data)
            print(f"✓ Report generated: {output_path}")

            # Optional: Send notification, upload to cloud, etc.
            print("\n[3/3] Post-processing...")
            self._post_process(output_path)

            print(f"\n{'='*60}")
            print(f"✓ Weekly report generation completed successfully!")
            print(f"{'='*60}\n")

        except Exception as e:
            print(f"\n✗ Error during report generation: {e}")
            # Optional: Send error notification
            self._handle_error(e)

    def _post_process(self, output_path: str):
        """Post-processing after report generation"""
        # Add your post-processing logic here:
        # - Send email with report
        # - Upload to cloud storage
        # - Create backup
        # - Send notification to Slack/Teams
        print(f"Post-processing complete for: {output_path}")

    def _handle_error(self, error: Exception):
        """Handle errors during report generation"""
        # Add error handling logic:
        # - Log to file
        # - Send error notification
        # - Retry mechanism
        print(f"Error logged: {error}")

    def run_now(self):
        """Run report generation immediately (for testing)"""
        print("Running report generation immediately...")
        self.generate_report_job()

    def start_scheduler(self):
        """Start the scheduler to run reports automatically"""
        schedule_config = self.config.get('schedule', {})
        day = schedule_config.get('day', 'monday').lower()
        time_str = schedule_config.get('time', '09:00')

        print(f"\n{'='*60}")
        print(f"VLines Weekly Reports Automation - Scheduler Started")
        print(f"{'='*60}")
        print(f"Schedule: Every {day.capitalize()} at {time_str}")
        print(f"Configuration: {self.config_path}")
        print(f"Output directory: {self.config.get('output', {}).get('directory', './reports')}")
        print(f"{'='*60}\n")

        # Schedule the job
        if day == 'monday':
            schedule.every().monday.at(time_str).do(self.generate_report_job)
        elif day == 'tuesday':
            schedule.every().tuesday.at(time_str).do(self.generate_report_job)
        elif day == 'wednesday':
            schedule.every().wednesday.at(time_str).do(self.generate_report_job)
        elif day == 'thursday':
            schedule.every().thursday.at(time_str).do(self.generate_report_job)
        elif day == 'friday':
            schedule.every().friday.at(time_str).do(self.generate_report_job)
        elif day == 'saturday':
            schedule.every().saturday.at(time_str).do(self.generate_report_job)
        elif day == 'sunday':
            schedule.every().sunday.at(time_str).do(self.generate_report_job)
        else:
            print(f"Warning: Unknown day '{day}', defaulting to Monday")
            schedule.every().monday.at(time_str).do(self.generate_report_job)

        print(f"Next scheduled run: {schedule.next_run()}\n")
        print("Press Ctrl+C to stop the scheduler\n")

        # Keep the scheduler running
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\nScheduler stopped by user")


def main():
    """Main entry point"""
    import sys

    scheduler = ReportScheduler()

    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--now' or sys.argv[1] == '-n':
            # Run immediately
            scheduler.run_now()
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("VLines Weekly Reports Automation")
            print("\nUsage:")
            print("  python scheduler.py           Start the scheduler (runs weekly)")
            print("  python scheduler.py --now     Generate report immediately")
            print("  python scheduler.py --help    Show this help message")
        else:
            print(f"Unknown argument: {sys.argv[1]}")
            print("Use --help for usage information")
    else:
        # Start scheduler
        scheduler.start_scheduler()


if __name__ == "__main__":
    main()
