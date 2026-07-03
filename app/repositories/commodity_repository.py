from sqlalchemy.orm import Session

from app.db.models.commodity import Commodity

class CommodityRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, commodity: Commodity):
        self.db.add(commodity)
        self.db.commit()
        self.db.refresh(commodity)
        return commodity
    
    def get_by_name(self, name: str):
        return self.db.query(Commodity).filter(Commodity.name == name).first()

