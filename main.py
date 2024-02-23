from sqlmodel import Session, select
from typing import List, Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from database import engine
import model    

app = FastAPI()

get_session = Session(bind=engine)

@app.on_event("startup")
def onStartup():
    model.main()
    
@app.get("/")
def read_root():
    return {'message':'Welcome to the quiz API'}

@app.get("/courses", response_model=List[model.Course])
def getCourses(session: Annotated[Session, Depends(Session(engine))]):
    with Session(engine) as session:
        courses = session.exec(select(model.Course)).all()
    return courses



