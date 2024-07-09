class Hashobject:
  pass 

def hash_obj(obj) -> int:
  obj1 = Hashobject
  obj2 = Hashobject 
  hashing = int(f"{hash(obj1)}{hash(obj2)}")
  return hashing 
  

