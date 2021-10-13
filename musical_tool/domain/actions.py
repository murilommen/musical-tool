from sqlalchemy.orm import Session

from musical_tool.domain import models


def create_music(db: Session, music_name: str):
    music = db.query(models.Music).filter(models.Music.music_name == music_name)

    if not music.first():        
        new_music = models.Music(music_name=music_name)
        db.add(new_music)
        db.commit()
        db.refresh(new_music)
        return new_music
    else:
        return None


def register_analysis(db: Session):
    # Parse input object

    # If music doesn't exist, call create_music function
    # vars: music_name

    # Register analysis

    # Register timestamps
    pass


def register_timestamps(db: Session):
    pass



