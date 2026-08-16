const fs = require('fs');
const db = JSON.parse(fs.readFileSync('data.json', 'utf8'));

db.classes.forEach(cls => {
    db.settings.days.forEach(d => {
        for(let p=1; p<=db.settings.periodsCount; p++) {
            const tts = db.timetable.filter(t => t.day == d && t.period == p && db.allocations.find(a=>a.id===t.allocationId)?.classId === cls.id);
            if(tts.length > 0) {
                console.log(`Matched! Class: ${cls.name}, Day: ${d}, Period: ${p}, Items: ${tts.length}`);
            }
        }
    });
});
