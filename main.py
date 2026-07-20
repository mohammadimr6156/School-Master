import webview
import json
from pathlib import Path

DATA_FILE = Path('data.json')

def get_default_data():
    return {
        'settings': {
            'days': ['شنبه', 'یکشنبه', 'دوشنبه', 'سه‌شنبه', 'چهارشنبه'],
            'periodsCount': 4,
            'hoursPerPeriod': 2
        },
        'grades': ['دهم', 'یازدهم', 'دوازدهم'],
        'majors': ['ریاضی', 'تجربی', 'انسانی', 'کامپیوتر', 'حسابداری', 'عمومی'],
        'locations': [],
        'classes': [],
        'courses': [],
        'teachers': [],
        'allocations': [],
        'timetable': []
    }

class Api:
    def _read_data(self):
        if not DATA_FILE.exists():
            return get_default_data()
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Ensure all keys exist
                default = get_default_data()
                for k, v in default.items():
                    if k not in data:
                        data[k] = v
                return data
        except:
            return get_default_data()

    def _write_data(self, data):
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_all_data(self):
        return self._read_data()

    def save_settings(self, settings_data):
        data = self._read_data()
        if 'settings' in settings_data:
            data['settings'] = settings_data['settings']
        if 'grades' in settings_data:
            data['grades'] = settings_data['grades']
        if 'majors' in settings_data:
            data['majors'] = settings_data['majors']
        self._write_data(data)

    def save_locations(self, locations):
        data = self._read_data()
        data['locations'] = locations
        self._write_data(data)

    def save_classes(self, classes):
        data = self._read_data()
        data['classes'] = classes
        self._write_data(data)

    def save_courses(self, courses):
        data = self._read_data()
        data['courses'] = courses
        self._write_data(data)

    def save_teachers(self, teachers):
        data = self._read_data()
        data['teachers'] = teachers
        self._write_data(data)

    def save_allocations(self, allocations):
        data = self._read_data()
        data['allocations'] = allocations
        self._write_data(data)

    def save_timetable(self, timetable):
        data = self._read_data()
        data['timetable'] = timetable
        self._write_data(data)
        
    def clear_all_data(self):
        self._write_data(get_default_data())


if __name__ == '__main__':
    api = Api()
    
    base_dir = Path(__file__).parent
    html_file = base_dir / 'index.html'
    
    if not html_file.exists():
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write("<h1>Loading...</h1>")
    
    window = webview.create_window(
        title='سیستم برنامه‌ریزی و مدیریت مدرسه',
        url=str(html_file),
        js_api=api,
        width=1200,
        height=800,
        min_size=(800, 600)
    )
    
    webview.start()
