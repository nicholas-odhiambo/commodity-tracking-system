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
    
    #get commodity by name
    def get_by_name(self, name: str):
        return self.db.query(Commodity).filter(Commodity.name == name).first()
    
    #get commodity by id
    def get_by_id(self, commodity_id: int):
        return(
            self.db.query(Commodity).filter(Commodity.id == commodity_id,Commodity.is_active).first()
        )

    #get all commodities
    def get_all(self):
        return self.db.query(Commodity).filter(Commodity.is_active).all() 

    ##update commodity 
    def update(self, commodity: Commodity):
        self.db.commit()
        self.db.refresh(commodity)
        return commodity

