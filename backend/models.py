from google.appengine.ext import ndb

class DepartmentModel(ndb.Model):
	name = ndb.StringProperty(required=True, repeated=False)
	

class TownModel(ndb.Model):
	name = ndb.StringProperty(required=True, repeated=False)
	department = ndb.StructuredProperty(DepartmentModel, required=True)
	

class BaseModel(ndb.Model):	
	address = ndb.StringProperty(required=False)
	img = ndb.BlobProperty(required=False)
	description = ndb.TextProperty(required=True)
	price = ndb.IntegerProperty(required=False)
	title = ndb.StringProperty(required=False)
	ratings = ndb.FloatProperty(required=False, default=0.0)
	town = ndb.StructuredProperty(TownModel, required=False)
	

class HotelModel(BaseModel):
	name = ndb.StringProperty(repeated=False)


class ActivityModel(BaseModel):
	name = ndb.StringProperty(repeated=False)
	start = ndb.DateProperty(required=True)
	end = ndb.DateProperty(required=True)
	
	
class RestaurantModel(BaseModel):
	name = ndb.StringProperty(repeated=False)
	
	
class SiteModel(ndb.Model):
	address = ndb.StringProperty(required=False)
	img = ndb.BlobProperty(required=False)
	description = ndb.TextProperty(required=True)
	title = ndb.StringProperty(required=False)
	ratings = ndb.FloatProperty(required=False, default=0.0)
	town = ndb.StructuredProperty(TownModel, required=False)
	
	
class UserModel(ndb.Model):
	name = ndb.StringProperty(required=True)
	img = ndb.GenericProperty(required=False)
	username = ndb.StringProperty(repeated=False)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
