from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str
    
class QuizSchema(BaseModel):
    name:str
    user:UserSchema
    
class QuestionSchema(BaseModel):
    question: str    
    answer:str 
    wrong1:str
    wrong2:str
    wrong3:str 
    
  