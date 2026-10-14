#Fastapi is the framework use to create api using python
#install fastapi and "fastapi[standard]" packages/modules
#now creat your own api

from fastapi import FastAPI
from sys_utils import system_utils

app = FastAPI(title="system utils api")

@app.get("/health")
def hello():
    return{"message" : "this is yuki"}

@app.get("/metrics")
def metrics():
    return system_utils()
    


