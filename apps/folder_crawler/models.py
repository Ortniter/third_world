from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.db import Base


class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String, index=True)
    files = relationship('File', back_populates='folder')


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    path = Column(String, index=True)
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folder = relationship('Folder', back_populates='files')
