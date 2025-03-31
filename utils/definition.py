import os

from dotenv import load_dotenv

dotenv_path = ".env"
load_dotenv(dotenv_path,override=True)

def add_proxy(url : str,username : str, password : str):
    return url.replace("https://","https://"+username+":"+password+"@")

class Settings:
    USERNAME = os.getenv("USERNAME") 
    PASSWORD = os.getenv("PASSWORD")
    IS_PROXY_ADD = os.getenv("IS_PROXY_ADD")
    if IS_PROXY_ADD == "true":
        SOF_QUESTIONS_PAGE = add_proxy(os.getenv("SOF_QUESTIONS_PAGE"),USERNAME,PASSWORD)
    else:
        SOF_QUESTIONS_PAGE = os.getenv("SOF_QUESTIONS_PAGE")

settings = Settings()
