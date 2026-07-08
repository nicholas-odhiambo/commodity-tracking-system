from app.db.models.commodity import Commodity
from app.repositories.commodity_repository import CommodityRepository
from typing import Optional

class CommodityService:
    def __init__(self, repo: CommodityRepository ):
        self.repo = repo 

    def create_commodity(self, name: str, unit_of_measure: str, description: Optional[str] = None):
        existing = self.repo.get_by_name(name)
        if existing:
            raise ValueError("Commodity Already exists")
        
        #create commodity 
        commodity = Commodity(
            name = name,
            unit_of_measure = unit_of_measure,
            description = description
        )
        
        #save to db 
        return self.repo.create(commodity)

    ## get commodity by id
    def get_commodity(self, commodity_id: int):
        commodity = self.repo.get_by_id(commodity_id)
        if commodity is None:
            raise ValueError("Commodity not found")
        return commodity

    #get all comdities 
    def get_commodities(self):
        return self.repo.get_all()

    ## update a commodity 
    def update_commodity(self, commodity_id: int, name: str, unit_of_measure: str, 
                         description: str | None, is_active: bool  ):
        commodity = self.repo.get_by_id(commodity_id)
        if commodity is None:
            raise ValueError("Commodity not found")
        
        existing = self.repo.get_by_name(name)
        if existing is not None and existing.id != commodity.id:
            raise ValueError("A commodity with this name already exists")
        
        commodity.name = name 
        commodity.unit_of_measure = unit_of_measure
        commodity.description = description
        commodity.is_active = is_active

        return self.repo.update(commodity)

    ##delete commodity
    def delete_commodity(self, commodity_id: int):
        commodity = self.repo.get_by_id(commodity_id)
        if commodity is None: 
                raise ValueError("Commodity not found")
        
        if commodity.is_active is False:
            raise ValueError("Commodity already deleted")
        
        commodity.is_active = True

        return self.repo.update(commodity)  
        