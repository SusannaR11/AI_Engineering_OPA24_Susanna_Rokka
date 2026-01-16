from backend.constants import VECTOR_DATABASE_PATH, DATA_PATH
import lancedb
from backend.data_models import Article
import time
from pathlib import Path
from lancedb.pydantic import LanceModel
from lancedb import Field
from lancedb.embeddings import get_registry
from pathlib import Path
from lancedb.table import LanceTable

embedding_model = get_registry().get("gemini-text").create(name="gemini-embedding-001")

# schema for a LanceTable
class Article(LanceModel):
    doc_id: set
    filepath: str
    filename: str= Field(description="stem of the file, i.e. without suffix")
    content: str
    embedding: Vector(3072) = embedding_model.VectorField()

#create vector db
def setup_vector_db(path):
    #Path(path).mkdir(exist_ok=True)
    vector_db = lancedb.connect(uri=path)
    vector_db.create_table("articles", schema=Article, exist_ok=True)

    return vector_db

# populate vector db - ensure 
def ingest_docs_to_vector_db(table: LanceTable):
    for file in DATA_PATH.glob("*.txt"):
        with open(file, "r") as f:
            content = f.read()

            doc_id = file.stem # or some hash/ number
            table.delete(f"doc_id = '{doc_id}'") # make idempotent

            table.add(
                [
                    {
                        "doc_id": doc_id,
                        "filepath": str(file),
                        "filename": file.stem,
                        "content": content,
                    }
                ]
            )

            print(table.to_pandas().shape)
            print(table.to_pandas()["filename"])
            time.sleep(30)


if __name__ == "__main__":
    vector_db = setup_vector_db(VECTOR_DATABASE_PATH)

    ingest_docs_to_vector_db(vector_db["articles"])