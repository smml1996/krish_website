import time
import json
from collections import deque
from utils import get_remedies, get_symptoms

visited_ids = set()
q = deque()

root_file = open("data/root.json")
root_data = json.loads(root_file.read())

root_data = root_data["Data"]["RbSymptoms"]
all_remedies = []

val = 0
for root_symptom in root_data:
    assert root_symptom["SymptomId"] not in visited_ids
    val = root_symptom["SymptomId"]
    visited_ids.add(root_symptom["SymptomId"])
    q.append(root_symptom)
    break
 
print("root symptom:", visited_ids)   
while len(q) > 0:
    print("current queue size: ", len(q))
    current = q.pop()
    assert(isinstance(current["RemediesCount"], int))
    if current["RemediesCount"] > 0:
        remedies = get_remedies(current["ParentSymptomId"], current["SymptomId"])
        if remedies is not None:
            remedies["symptom_"] = current
            all_remedies.append(remedies)
        
    
    succ_symptoms = get_symptoms(current["ParentSymptomId"], current["SymptomId"])
    time.sleep(1)
    if succ_symptoms is not None:
        for s_symptom in succ_symptoms:
            assert isinstance(s_symptom["SymptomId"], int)
            if not (s_symptom["SymptomId"] in visited_ids):
                visited_ids.add(s_symptom["SymptomId"])
                q.append(s_symptom)
    if (len(all_remedies) % 20 == 0) and (len(all_remedies) > 0):
        data = {"data": all_remedies}
        f = open(f"chapter_{val}.json", "w")
        f.write(json.dumps(data))
        f.close()
    
data = {"data": all_remedies}
f = open(f"chapter_{val}.json", "w")
f.write(json.dumps(data))
f.close()



