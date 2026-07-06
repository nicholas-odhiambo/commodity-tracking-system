from app.db.base import Base
from app.db.session import engine
from app.db.models.commodity import Commodity 

Base.metadata.create_all(bind=engine)