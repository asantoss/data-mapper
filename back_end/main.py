from typing import Union
import pandas as pd
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
import json
from fastapi.responses import StreamingResponse


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5173",
    "https://asantoss.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/file")
def read_file(file: UploadFile):
    contents = file.file.read()
    data = BytesIO(contents)
    df = pd.read_csv(data)
    df = df.fillna('')
    data.close()
    file.file.close()
    return {"columns": list(df.columns), "rows": list(df.head(5).to_dict('records'))}


@app.post("/file/process")
def proccess_file(file: UploadFile, data: str = Form()):
    contents = file.file.read()
    body = json.loads(data)
    cols_to_drop = [col["name"] for col in body["columns"] if col["deleted"]]
    cols_to_dedupe = [col["name"]
                      for col in body["columns"] if col["drop_dupes"]]
    cols_to_rename = {col['name']: col["value"]
                      for col in body["columns"] if col["name"] != col["value"]}
    file_contents = BytesIO(contents)
    df = pd.read_csv(file_contents)
    df = df.fillna('')
    try:
        for col in cols_to_dedupe:
            df.drop_duplicates(col, keep="first", inplace=True)
    except NameError:
        print(NameError)
    df.drop(columns=cols_to_drop, inplace=True)
    df.rename(columns=cols_to_rename, inplace=True)
    file_contents.close()
    file.file.close()
    output = df.to_csv(index=False)
    return StreamingResponse(
        iter([output]),
        media_type='text/csv',
        headers={"Content-Disposition":
                 f'attachment;filename={file.filename}_mapped.csv'})


@app.get("/")
def read_root():
    return {"Hello": "World"}
