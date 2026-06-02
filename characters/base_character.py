from sqlalchemy import Column, Integer, String, DateTime, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    """Usuario principal"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return f"<User {self.username}>"

class CharacterProgress(Base):
    """Progreso con cada personaje"""
    __tablename__ = 'character_progress'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_name = Column(String)  # "nova", "luna", "aria", etc
    current_chapter = Column(Integer, default=1)
    affinity = Column(Float, default=0)  # 0-100
    playtime_hours = Column(Float, default=0)
    special_moments = Column(Integer, default=0)
    favorite = Column(String, default=None)  # Personaje favorito del usuario
    last_played = Column(DateTime, default=datetime.now)
    choices_made = Column(JSON, default={})  # Historial de decisiones
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Progress {self.character_name} - Cap {self.current_chapter}>"

class SharedMemories(Base):
    """Recuerdos compartidos entre usuario y personaje"""
    __tablename__ = 'shared_memories'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_name = Column(String)
    chapter = Column(Integer)
    memory_text = Column(String)
    memory_image = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Memory {self.character_name} Cap {self.chapter}>"

class GroupEvents(Base):
    """Eventos donde interactúan múltiples personajes"""
    __tablename__ = 'group_events'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    chapter_group = Column(String)  # "group_interaction_1"
    characters_involved = Column(JSON)  # ["nova", "luna", "aria"]
    status = Column(String, default="pending")  # "active", "completed"
    created_at = Column(DateTime, default=datetime.now)
