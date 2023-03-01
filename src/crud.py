import models
import schemas

from sqlalchemy.orm import Session
from datetime import datetime


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()
#
#
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_audio(audio: schemas.Audio, db: Session):
    new_audio = None
    if audio.type == 'song':
        new_audio = models.Song(id=audio.id,
                                name=audio.name,
                                duration=audio.duration,
                                time=datetime.now())

    elif audio.type == 'podcast':
        if not audio.host or not audio.participants:
            return {'ERROR'}

        participants = ','.join(audio.participants)
        new_audio = models.Podcast(id=audio.id,
                                   name=audio.name,
                                   duration=audio.duration,
                                   time=datetime.now(),
                                   host=audio.host,
                                   participants=participants)

    elif audio.type == 'audiobook':
        if not audio.author or not audio.narrator:
            return {'ERROR'}

        new_audio = models.AudioBook(id=audio.id,
                                     name=audio.name,
                                     duration=audio.duration,
                                     time=datetime.now(),
                                     author=audio.author,
                                     narrator=audio.narrator)
    else:
        pass
    db.add(new_audio)
    db.commit()
    return {f'new audio of type {audio.type} is added'}
