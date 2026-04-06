import json
from utils.hashing import generate_hash
from cloud.s3 import upload_to_s3
from cloud.drive import upload_to_drive

STATE_FILE = "state/state.json"

def load_state():
    try:
        with open(STATE_FILE) as f:
            return json.load(f)
    except:
        return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def sync_files(files):
    state = load_state()

    for file in files:
        name = file["name"]
        path = file["path"]

        file_hash = generate_hash(path)

        if name in state and state[name] == file_hash:
            print(f"Skipping (unchanged): {name}")
            continue

        print(f"Uploading: {name}")

        upload_to_s3(path, name)

        # 🔥 THIS MUST BE UNCOMMENTED
        upload_to_drive(path, name)

        state[name] = file_hash

    save_state(state)