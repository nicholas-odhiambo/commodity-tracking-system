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
        