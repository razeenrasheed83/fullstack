from fastapi import APIRouter,status
from src.utilities.dbutils import DButils
from src.models.registration import Registration
from passlib.context import CryptContext


router = APIRouter(
    tags=["Authorisation"]
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


@router.post('/signup', status_code=status.HTTP_201_CREATED)
def userSignup(request: Registration):
    try:
        db = DButils()
        columns = ['username', 'email', 'contact', 'password', 'course_id', 'user_role_id']
        columns2 = ['username', 'email', 'contact', 'password', 'course_id', 'user_role_id']
        hashed_password = pwd_context.hash(request.password)
        values = (
            request.username,
            request.email,
            request.contact,
            hashed_password,
            request.course_id,
            request.user_role
        )
        if request.user_role == 1:
            db.insert_query('students', columns, values)
        else:
            db.insert_query('teachers', columns2, values)



        # db.insert_query('students', columns, values)
        return {"message": "User signed up successfully"}
        # return
    except Exception as e:
        raise e
