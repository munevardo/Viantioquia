from google.appengine.ext import ndb

class UserModel(ndb.Model):
	name = ndb.StringProperty(required=True)
	img = ndb.GenericProperty(required=False)
	username = ndb.StringProperty(repeated=False)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	

class DepartmentModel(ndb.Model):
	name = ndb.StringProperty(required=True, repeated=False)
	

class TownModel(ndb.Model):
	name = ndb.StringProperty(required=True, repeated=False)
	department = ndb.StructuredProperty(DepartmentModel, required=True)


class MailModel(ndb.Model):
	email = ndb.StringProperty(repeated=True)
	town = ndb.StructuredProperty(TownModel, repeated=True)	
	
	
class TariffModel(ndb.Model):
	price = ndb.IntegerProperty(required=True)
	name = ndb.StringProperty(required=True)
	description = ndb.TextProperty(required=True)
	
	
class RatingModel(ndb.Model):
	vote = ndb.FloatProperty(required=True)
	comment = ndb.TextProperty(required=True)
	user = ndb.StructuredProperty(UserModel, repeated=True)
	

class BaseModel(ndb.Model):	
	address = ndb.StringProperty(required=False)
	img = ndb.BlobProperty(required=False)
	description = ndb.TextProperty(required=True)
	price = ndb.IntegerProperty(required=False)
	title = ndb.StringProperty(required=False)
	ratings = ndb.FloatProperty(required=False, default=0.0)
	town = ndb.StructuredProperty(TownModel, required=False)
	tariff = ndb.StructuredProperty(TariffModel, repeated=True)
	ratings = ndb.StructuredProperty(RatingModel, required=False)
	

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
	ratings = ndb.StructuredProperty(RatingModel, required=False)
