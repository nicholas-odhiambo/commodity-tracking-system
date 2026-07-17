from app.db.base import Base
from app.db.session import engine
from app.db.models.commodity import Commodity 
from app.db.models.supplier import Supplier
from app.db.models.warehouse import Warehouse
from app.db.models.customer import Customer

Base.metadata.create_all(bind=engine)