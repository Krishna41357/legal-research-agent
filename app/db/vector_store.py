from db.connection import get_connection
# pyrefly: ignore [missing-import]
from pgvector.psycopg import register_vector

def store_documents(documents, embeddings):
    if(len(documents) != len(embeddings)):
        raise ValueError(
            f"Mismatch: {len(documents)} documents but "
            f"{len(embeddings)} embeddings"
        )
    
    connection = get_connection()
    register_vector(connection)

    try:
        with connection.cursor() as cursor:
            for document, embedding in zip(documents, embeddings):
                cursor.execute(
                    """
                    INSERT INTO legal_chunks(content, metadata, embedding)
                    VALUES(%s, %s, %s)
                    """,
                    (
                        document.page_content,
                        document.metadata,
                        embedding
                    ),
                )

        connection.commit()
    finally:
        connection.close()
        print(f"Stored {len(documents)} vectors in Postgres.")


def search_similar_chunks(query_embedding , top_k: int = 5):
    connection = get_connection()
    try:
        register_vector(connection)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                    SELECT content , metadata,
                    1-(embedding <=> %s::vector) AS similarity
                    FROM legal_chunks
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s
                """,
                (query_embedding , query_embedding , top_k),
            )

            return cursor.fetchall() # it is fetch all rows
    finally:
        connection.close()