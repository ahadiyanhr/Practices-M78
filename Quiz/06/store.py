class Store:
    __stores = {}
    
    def __init__(self, shopname, sub_store_list: list, store_goods_dict=dict) -> None:
        self.sub_stores = sub_store_list
        self._name = shopname
        self.goods = store_goods_dict
        Store.__stores[shopname] = self
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, shopname):
        if shopname in Store.__stores.keys():
            raise ValueError(f"Store with name of {shopname} already exists.")
        self._name = shopname 
        
    def add_store(self, store):
        self.sub_stores.append(store)

    def add_goods(self, goods, count):
        self.goods[goods] = count
    @property
    def goods_count(self):
        return sum(self.goods.values())
    
    def __len__(self):
        sums = self.goods_count
        for storesub in self.sub_stores:
            sums+= storesub.goods_count
        return sums
    
    def __del__(self):
        raise NotImplementedError("Stores can not be deleted")
    def __delete__(self):
        raise NotImplementedError("Stores cannot be deleted")

    def __eq__(self, other):
        raise NotImplementedError("This operation can not execute!")

    def __gt__(self, other):
        raise NotImplementedError("This operation can not execute!")

    def __lt__(self, other):
        raise NotImplementedError("This operation can not execute!")

    def __ge__(self, other):
        raise NotImplementedError("This operation can not execute!")

    def __le__(self, other):
        raise NotImplementedError("This operation can not execute!")