from random import choice
import time, datetime, string

def randupchr():
    return choice(string.ascii_uppercase)

def randlwchr():
    return choice(string.ascii_lowercase)

def doc_id_generator():
    return 'DOC'+str(datetime.date.today().strftime("%Y%m%d"))+randupchr()+randlwchr()+randlwchr()+str(datetime.datetime.now().strftime("%H%M%S"))+randupchr()

def pat_id_generator():
    return 'PAT'+str(datetime.date.today().strftime("%Y%m%d"))+randlwchr()+randupchr()+randlwchr()+str(datetime.datetime.now().strftime("%H%M%S"))+randupchr()
