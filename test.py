import json
data = json.load(open('data.json', encoding='utf-8'))
for cls in data['classes']:
    for d in data['settings']['days']:
        for p in range(1, data['settings']['periodsCount']+1):
            tts = [t for t in data['timetable'] if t['day'] == d and t['period'] == p and next((a for a in data['allocations'] if a['id'] == t['allocationId']), {}).get('classId') == cls['id']]
            if tts:
                print(f"Found! {cls['name']} {d} {p}")
