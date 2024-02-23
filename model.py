from typing import List, Optional
from sqlmodel import Field, SQLModel, Session, select, Relationship
from database import engine

class Program(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    description: str
    course: List["Course"] = Relationship(back_populates="program")
    
class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    instructor_id: int = Field(foreign_key="instructor.id")
    program_id: int = Field(foreign_key="program.id")
    program: "Program" = Relationship(back_populates="program.name")
    instructor: "Instructor" = Relationship(back_populates="instructor.name")
    
class Instructor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    course_id: int = Field(foreign_key="course.id")
    course: List["Course"] = Relationship(back_populates="instructor")
    
class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    course_id: int = Field(foreign_key="course.id")
    course: List["Course"] = Relationship(back_populates="student")
    program_id: int = Field(foreign_key="program.id")
    program: List["Program"] = Relationship(back_populates="student")
    
class Topics(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    course_id: int = Field(foreign_key="course.id")
    course: List["Course"] = Relationship(back_populates="course.name")
    topics_id: int = Field(foreign_key="topics.id")
    topics: List["Topics"] = Relationship(back_populates="topics")
    
class Quiz(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    topics_id: int = Field(foreign_key="topics.id")
    topics: List["Topics"] = Relationship(back_populates="quiz")
    timeInMinutes: int = Field(index=True, nullable=False)
    description:str
    
class QuizDashboard(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    quiz: List["Quiz"] = Relationship(back_populates="quizdashboard")
    student_id: int = Field(foreign_key="student.id")
    student: List["Student"] = Relationship(back_populates="quizdashboard")
    score: int = Field(index=True, nullable=False)
    timeTaken: int = Field(index=True, nullable=False)
    quizTaken: bool = Field(index=True, nullable=False)
    dateTaken: str = Field(index=True, nullable=False)
    
class QuestionTypes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False)
    
class Questions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question: str = Field(index=True, nullable=False)
    answer: str = Field(index=True, nullable=False)
    topics_id: int = Field(foreign_key="topics.id")
    topics: List["Topics"] = Relationship(back_populates="topics")
    questionTypes_id: int = Field(foreign_key="questiontypes.id")
    questionTypes: List["QuestionTypes"] = Relationship(back_populates="questiontypes")
    mcq_options_id: int = Field(foreign_key="mcqoptions.id")
    mcq_options: List["McqOptions"] = Relationship(back_populates="mcqoptions")
 
class McqOptions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    potential_answers: str = Field(index=True, nullable=False)
    question_id: int = Field(foreign_key="questions.id")
    
class AnswerMCQs(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    answer: str = Field(index=True, nullable=False)
    question_id: int = Field(foreign_key="questions.id")
    
class AnswerDISC(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    answer:str = Field(index=True, nullable=False)
    question_id: int = Field(foreign_key="questions.id")
    
class QuizQuestions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    quiz: List["Quiz"] = Relationship(back_populates="quizquestions")
    question_id: int = Field(foreign_key="questions.id")
    question: List["Questions"] = Relationship(back_populates="quizquestions")
    
class ScoreSheet(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quiz_id: int = Field(foreign_key="quiz.id")
    quiz: List["Quiz"] = Relationship(back_populates="answersheet")
    student_id: int = Field(foreign_key="student.id")
    student: List["Student"] = Relationship(back_populates="answersheet")
    quiz_dashboard_id: int = Field(foreign_key="quizdashboard.id")
    quizdashboard: List["QuizDashboard"] = Relationship(back_populates="answersheet")
    score: int = Field(index=True, nullable=False)
    questions_correct: int = Field(index=True, nullable=False)
    
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def main():
    create_db_and_tables()
    print("Database and tables created successfully!")
    
if __name__ == "__main__":
    main()