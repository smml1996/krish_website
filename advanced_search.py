import time
import json
from collections import deque
from utils import get_remedies

time.sleep(10800)
chapter_name = "MIND"
f = open(f"data/chapter_{chapter_name}.json", "r")
symptoms = json.loads(f.read())
f.close()


f = open(f"data/remedies/chapter_{chapter_name}.json", "r")
remedies_ = json.loads(f.read())["data"]
f.close()
remedies = []
symptoms_done = set()
for remedy in remedies_:
    if remedy["RemediesLocal"] > 0:
        remedies.append(remedy)
        symptoms_done.add(remedy["SymptomId"])

for symptom in symptoms["data"]:
    if (symptom["RemediesCount"] > 0) and (symptom["SymptomId"] not in symptoms_done):
        try:
            remedies_ = get_remedies(symptom["ParentSymptomId"], symptom["SymptomId"])
            if remedies_ is not None:
                remedies_["symptom_"] = symptom
                remedies.append(remedies_)
            else:
                raise Exception("seems rubrics limits has been reached")
            if (len(remedies) % 20 == 0) and (len(remedies) > 0):
                data = {"data": remedies}
                f = open(f"data/remedies/chapter_{chapter_name}.json", "w")
                f.write(json.dumps(data))
                f.close()
            time.sleep(1)
        except Exception as e:
            print(e)
            break

data = {"data": remedies}
f = open(f"data/remedies/chapter_{chapter_name}.json", "w")
f.write(json.dumps(data))
f.close()
    
    