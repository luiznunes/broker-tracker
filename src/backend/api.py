# coding=utf-8
from fastapi import FastAPI
import registers

app = FastAPI()


@app.get('/api/get/coordinates')
def root():
    return registers.get_registers('/tracker')
