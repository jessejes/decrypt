from models import Credential
from models import RequestCredential

from database import session

def create_credential(req: RequestCredential):

    _credential = Credential(1, req.title, req.email, req.password, req.url, req.comment)

    session.add(_credential)
    session.commit()