from app import RVCSApp
from config import API_HOST, API_PORT

if __name__ == '__main__':
    RVCSApp().run(host=API_HOST, port=API_PORT)
