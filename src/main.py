"""DOCS
"""

__author__ = 'Vishwajeet Ghatage'
__email__ = 'cloudmai.vishwajeet@gmail.com'
__date__ = '09/04/2021'

# Built-in Imports
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

# Custom Imports
import schemas
import models
import crud
from database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/audio')
def create_audio(audio: schemas.Audio, db: Session = Depends(get_db)):
    return crud.create_audio(audio=audio, db=db)


@app.get('/audio/{f_type}')
def read_audios(f_type: str):
    return {'data': [f'list of all files of type {f_type}']}


@app.get('/audio/{f_type}/{f_id}')
def read_audio(f_type: str, f_id: int):
    return {'data': {'Id': f_id, 'Type': f_type}}


# @app.post('/audio')
# def update_audio():
#     pass
#
#
# @app.delete('/audio')
# def delete_audio():
#     pass


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8000)
