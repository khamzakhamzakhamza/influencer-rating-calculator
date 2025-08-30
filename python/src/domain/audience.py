from pydantic import BaseModel

class Audience(BaseModel):
	size: int
	executive: int
	professionals: int
