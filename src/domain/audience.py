from pydantic import BaseModel

class Audience(BaseModel):
	size: int
	executive: float
	professionals: float
	other: float