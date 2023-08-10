from typing import List, Optional

from pinecone_text.sparse import SparseVector
from pydantic import BaseModel

from context_engine.models.data_models import Document, Query

# TODO 1: consider moving this to pinecone-text
# TODO 2: consider renaming to "Vector" or "DenseVector"
# TODO 3: consider supporting `np.ndarray`
VectorValues = List[float]


class KBDocChunk(Document):
    values: Optional[VectorValues] = None
    sparse_values: Optional[SparseVector] = None


class KBDocChunkWithScore(KBDocChunk):
    score: float


class KBQuery(Query):
    values: Optional[VectorValues] = None
    sparse_values: Optional[SparseVector] = None


class DocumentWithScore(Document):
    score: float


class KBQueryResult(BaseModel):
    query: str
    documents: List[DocumentWithScore]