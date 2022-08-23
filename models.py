from support.imports import *
import errors


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        BaseService.session.add(self)
        try:
            BaseService.session.commit()
        except exc.IntegrityError:
            raise errors.BadRequest


class User(Base, BaseModelMixin):

    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password = Column(String(128))
    ad = relationship('Ad', backref='User')

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def set_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str):
        raw_password = f'{raw_password}{config.SALT}'
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "email": self.email
        }


class Ad(Base, BaseModelMixin):

    __tablename__ = 'Ad'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), index=True, unique=True, nullable=False)
    description = Column(Text, index=True)
    creator_id = Column(Integer(), ForeignKey('User.id'))
    created_on = Column(DateTime(), default=datetime.utcnow)

    def __str__(self):
        return '<Ad {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            "description": self.description,
            'creator_id': self.creator_id,
            'created_on': self.created_on

        }
