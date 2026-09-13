# pyrefly: ignore [missing-import]
from langchain_text_splitters import RecursiveCharacterTextSplitter



def chunk_by_paragraph(text:str, max_chunk_size: int = 2000)->list[str]:
    paragraphs = text.split("\n\n")
    chunks = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size  = max_chunk_size,
        chunk_overlap = 300,
        separators = ["\n" ,". " ," " ,""]
    )

    current_chunk = ""


    for paragraph in paragraphs:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        if len(current_chunk) + len(paragraph) + 2 < max_chunk_size:
            if current_chunk:
                current_chunk+="\n\n" + paragraph
            else: 
                current_chunk = paragraph   
        else : 
            #save the current chunk
            if current_chunk:
                chunks.append(current_chunk) 
            
            # If the paragraph itself is too large, split it
            if len(paragraph) > max_chunk_size:
                chunks.extend(splitter.split_text(paragraph))
                current_chunk = ""
            else:
                current_chunk = paragraph
            
    # add final chunk
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


