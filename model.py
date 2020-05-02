from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from utils import logging, f


engine = create_engine('mysql://root@127.0.0.1:3306/test?charset=utf8')
Session = sessionmaker(bind=engine)
Session = scoped_session(Session)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return f'<{self.name}>'
    
    @classmethod
    def get_all(cls, i, j):
        session = Session()
        logging.info(f'{i}-{j} get_all\tsession={f(session)} bind={f(session.get_bind())}')
        logging.info(f'{i}-{j} {session.query(User).all()}')

    @classmethod
    def add_user(cls, i, j):
        session = Session()
        logging.info(f'{i}-{j} add_user\tsession={f(session)} bind={f(session.get_bind())}')
        session.add(User(name=f'{i}-{j}'))
        session.commit()

Base.metadata.create_all(engine)
