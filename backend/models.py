from google.appengine.ext import ndb

class BaseModel(ndb.Model):	
	address = ndb.StringProperty(requied=False)
	img = ndb.BlobProperty(required=False)
	description = ndb.TextProperty(required=True)
	price = ndb.IntegerProperty(required=False)
	title = ndb.StringProperty(required=False)
	ratings = ndb.FloatProperty(required=False, default=0.0)
	department = ndb.StringProperty(required=True)
	town = ndb.StringProperty(required=True)
	

class HotelModel(BaseModel):
	name = ndb.StringProperty(requied=True, repeated=False)


class ActivityModel(BaseModel):
	name = ndb.StringProperty(requied=True, repeated=False)
	start = ndb.DateProperty(required=True)
	end = ndb.DateProperty(required=True)
	
	
class RestaurantModel(BaseModel):
	name = ndb.StringProperty(requied=True, repeated=False)
	
	
class UserModel(BaseModel):
	name = ndb.StringProperty(requied=True)
	img = ndb.GenericProperty(required=False)
	username = ndb.StringProperty(required=True, repeated=False)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
