from dbaccess.dbcontext import Base
from dbmodels.abstract.dictionary_base import DictionaryBase


class AgreementParameterType(DictionaryBase, Base):
    __tablename__ = 'AgreementParameterType'
