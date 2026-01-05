import copy

class Square:
    def __init__(self,x:int,y:int)->None:
        self.x = x
        self.y = y

class Prototype:
    def __init__(self)->None:
        self._prototype_obj:dict = {}
    
    def register_object(self,name,obj)->None:
        self._prototype_obj[name] = obj
    
    def unregister_object(self,name)->None:
        del self._prototype_obj[name]

    def clone(self,name,**attr):
        obj = copy.deepcopy(self._prototype_obj.get(name))
        obj.__dict__.update(attr)
        return obj

# Client Code
sq =Square(20,20) 
proto = Prototype()
proto.register_object('square',sq)
rec = proto.clone('square',x=100,y=80)
cube = proto.clone('square',x=100,y=80,z=60)
print("SQUARE : ", sq.__dict__,", RECTANGLE", rec.__dict__,", CUBE: ", cube.__dict__)

        
        