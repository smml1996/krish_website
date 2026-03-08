import time
import json
from collections import deque
from utils import get_symptoms

root_file = open("data/root.json")
root_data = json.loads(root_file.read())

root_data = root_data["Data"]["RbSymptoms"]

for root_symptom in root_data:
    visited_ids = set()
    q = deque()
    assert root_symptom["SymptomId"] not in visited_ids
    visited_ids.add(root_symptom["SymptomId"])
    q.append(root_symptom)
    chapter = root_symptom["Element"]
    all_symptoms = []
    while len(q) > 0:
        print("chapter: ", chapter, " --- ", len(q))
        current = q.pop()
        all_symptoms.append(current)
        succ_symptoms = get_symptoms(current["ParentSymptomId"], current["SymptomId"])
        if succ_symptoms is not None:
            for s_symptom in succ_symptoms:
                assert isinstance(s_symptom["SymptomId"], int)
                if not (s_symptom["SymptomId"] in visited_ids):
                    visited_ids.add(s_symptom["SymptomId"])
                    q.append(s_symptom)
        time.sleep(1)
        if (len(all_symptoms) % 20 == 0) and (len(all_symptoms) > 0):
            data = {"data": all_symptoms}
            f = open(f"data/chapter_{chapter}.json", "w")
            f.write(json.dumps(data))
            f.close()
    
    data = {"data": all_symptoms}
    f = open(f"data/chapter_{chapter}.json", "w")
    f.write(json.dumps(data))
    f.close()
    
    