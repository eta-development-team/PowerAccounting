from dbaccess.dbcontext import Base
from dbmodels.dictionaries.dictionary_base import DictionaryBase


class AgreementParameterType(DictionaryBase, Base):
    __tablename__ = 'AgreementParameterType'
