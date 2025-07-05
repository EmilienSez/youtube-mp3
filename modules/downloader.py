import json
from pathlib import Path
from yt_dlp import YoutubeDL

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "assets/data"
DOWNLOAD_DIR = BASE_DIR / "assets/mp3"
print(type(DATA_DIR))

OPTIONS_YT_DLP = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

def add_content_list(text):
    with open(DATA_DIR / "liste.json", "r") as f:
        data = json.load(f)
        data.append(text)
    with open(DATA_DIR / "liste.json", "w") as f:
        json.dump(data, f)

def remove_content_list(text):
    with open(DATA_DIR / "liste.json", "r") as f:
        data = json.load(f)
        data.remove(text)
    with open(DATA_DIR / "liste.json", "w") as f:
        json.dump(data, f)

def get_content_list():
    with open(DATA_DIR / "liste.json", "r") as f:
        data = json.load(f)
    return list(data)

def delete_content_list():
    with open(DATA_DIR / "liste.json", "w") as f:
        json.dump([], f)

def create_dir():
    i = 0
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    while True :
        try : 
            i += 1
            (DOWNLOAD_DIR/f"Téléchargement {i}").mkdir(exist_ok=False)
            OPTIONS_YT_DLP['outtmpl'] =  f"{DOWNLOAD_DIR}/Téléchargement {i}/{'%(title)s.%(ext)s'}"
            print(OPTIONS_YT_DLP['outtmpl'])
            
        except FileExistsError:
            continue
        break

def download_link(liste):
    for url in liste:
        try : 
            with YoutubeDL(OPTIONS_YT_DLP) as ydl:
                ydl.download([url])
        except Exception as e:
            print(e + " - " + url)

if __name__ == "__main__" : 
    pass