"""
Data Fetcher Module
Handles fetching data from various sources (API, JSON, Database)
"""

import requests
import json
from typing import Dict, Any
from datetime import datetime


class DataFetcher:
    """Fetches data for weekly reports from various sources"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.data_source_type = config.get('data_source', {}).get('type', 'json')
        self.data_source_url = config.get('data_source', {}).get('url', '')

    def fetch_data(self) -> Dict[str, Any]:
        """
        Fetch data based on configured source type

        Returns:
            Dictionary containing all report data
        """
        if self.data_source_type == 'api':
            return self._fetch_from_api()
        elif self.data_source_type == 'json':
            return self._fetch_from_json()
        elif self.data_source_type == 'database':
            return self._fetch_from_database()
        else:
            return self._get_sample_data()

    def _fetch_from_api(self) -> Dict[str, Any]:
        """Fetch data from REST API"""
        try:
            response = requests.get(
                self.data_source_url,
                timeout=30,
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from API: {e}")
            print("Falling back to sample data...")
            return self._get_sample_data()

    def _fetch_from_json(self) -> Dict[str, Any]:
        """Fetch data from local JSON file"""
        try:
            json_path = self.config.get('data_source', {}).get('json_path', 'data/weekly_data.json')
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file: {e}")
            print("Falling back to sample data...")
            return self._get_sample_data()

    def _fetch_from_database(self) -> Dict[str, Any]:
        """Fetch data from database"""
        # TODO: Implement database connection
        # Example: PostgreSQL, MySQL, etc.
        print("Database fetching not yet implemented. Using sample data.")
        return self._get_sample_data()

    def _get_sample_data(self) -> Dict[str, Any]:
        """
        Return sample data matching the structure from your React components
        This is based on the data found in TCKT, OPS, KinhDoanh components
        """
        return {
            "metadata": {
                "week": self._get_current_week(),
                "generated_at": datetime.now().isoformat(),
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
                    },
                    "cash_flow": {
                        "current_month": 173612532,
                        "previous_month": 135636758
                    }
                },
                "explanations": {
                    "payment_changes": [
                        "Phát sinh TĂNG so với T05: Khoản thanh toán 2 bên Biển Đông và MTT (hơn 30 tỷ VNĐ)",
                        "Phát sinh TĂNG so với T05: Sửa chữa vệ sinh lưu cont khối EQC (gần 5 tỷ VNĐ)",
                        "Phát sinh GIẢM so với T05: Khoản dầu trong nước giảm so với T05 hơn 11 tỷ VNĐ"
                    ],
                    "revenue_changes": [
                        "Tổng quan chung GIẢM so với T.05",
                        "Cước đại lý quốc tế giảm 22 tỷ VNĐ",
                        "Cước nội địa giảm 6,5 tỷ VNĐ"
                    ]
                }
            },
            "ops": {
                "ship_schedule": [
                    {
                        "ship_name": "MTT LimBang",
                        "voyage": "25LG021 S/N",
                        "route": "PCX",
                        "position": "Etd CCU 14/8",
                        "speed_sb_nb": "11.6",
                        "weather": "3E",
                        "days_notes": "",
                        "status": "Dự kiến neo chờ boretide 5 ngày",
                        "actual_ports": ""
                    },
                    {
                        "ship_name": "BD Mariner",
                        "voyage": "MB2525 S/N",
                        "route": "CMS",
                        "position": "Đang voy 26N",
                        "speed_sb_nb": "11.1",
                        "weather": "11.4",
                        "days_notes": "9 ngày 18h",
                        "status": "Adhoc Đà Nẵng",
                        "actual_ports": "Tcit và GML kẹt (cập TT, cmit)"
                    },
                    {
                        "ship_name": "BD Star",
                        "voyage": "BS2527 S/N",
                        "route": "NSS",
                        "position": "đang voy 28S",
                        "speed_sb_nb": "11.2",
                        "weather": "12.1",
                        "days_notes": "7 ngày 9.5h",
                        "status": "",
                        "actual_ports": "VDV"
                    }
                ],
                "performance": {
                    "profomar_vs_actual": {
                        "ships": ["MB2525SN", "BS2527SN", "NB2523SN"],
                        "profomar_days": [8, 7, 7],
                        "actual_days": [9.7, 7.4, 7]
                    }
                }
            },
            "kinh_doanh": {
                "market_overview": {
                    "hph_hcm_route": {
                        "vlines_share": 11.0,
                        "others_share": 89.0
                    },
                    "hcm_hph_route": {
                        "vlines_share": 11.6,
                        "others_share": 88.4
                    }
                },
                "domestic_performance": {
                    "weeks": ["VN125/25", "BL125/25", "BS125/25", "VJ125/25",
                             "VN225/25", "BL225/25", "BS225/25", "VJ225/25",
                             "VN325/25", "BL325/25", "BS325/25", "VJ325/25"],
                    "allocated": [460, 620, 460, 620, 460, 620, 460, 620, 460, 620, 460, 620],
                    "actual": [520, 662, 462, 560, 460, 620, 460, 620, 420, 600, 720, 680],
                    "percentage": [113, 107, 100, 90, 100, 100, 100, 110, 92, 105, 116, 110]
                },
                "top_customers": {
                    "hph_hcm": ["Honda", "Minh Đức", "Acecook", "Leeman", "Calofic"],
                    "hcm_hph": ["Acecook", "Dương", "Pantos", "Chánh", "Việt Nhật", "Panasonic"],
                    "hcm_dan": ["Calofic", "Chánh", "Pantos", "Acecook", "Dương"]
                },
                "market_notes": [
                    "GMD tàu Pacific Express dự kiến lên đà tại Phà Rừng từ đầu tháng 8/25",
                    "Dự kiến tình hình thị trường đầu hph trong nửa đầu tháng 8 vẫn tốt"
                ]
            },
            "eqc": {
                "overview": {
                    "revenue": 25000000,
                    "cost": 18000000,
                    "profit_margin": 28.0
                }
            },
            "thuong_vu": {
                "production_volume": {
                    "total_teus": 12500,
                    "revenue": 450000000
                }
            },
            "tong_quan_tau": {
                "fuel_consumption": {
                    "fo_actual": [8.98, 10.63, 9.7],
                    "fo_standard": [8.5, 8.5, 7.5],
                    "do_actual": [8.98, 10.63, 9.7],
                    "do_standard": [8.5, 8.5, 7.5]
                }
            }
        }

    def _get_current_week(self) -> str:
        """Get current week number in format 'YYYY-WXX'"""
        now = datetime.now()
        week_num = now.isocalendar()[1]
        return f"{now.year}-W{week_num:02d}"


if __name__ == "__main__":
    # Test the data fetcher
    test_config = {
        'data_source': {
            'type': 'json',
            'json_path': 'data/weekly_data.json'
        }
    }

    fetcher = DataFetcher(test_config)
    data = fetcher.fetch_data()

    print("Sample data structure:")
    print(json.dumps(data, indent=2, ensure_ascii=False))
