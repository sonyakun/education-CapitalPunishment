from fastapi import FastAPI

app = FastAPI()


@app.get("/gen/{text1}/")
def read_root(edu: str="教育", cp: str="死刑"):
  n1 = []
  n2 = []
  n3 = []
  for i in range(18):
      n1.append(edu)
  for i in range(10):
      n2.append(cp)
  for i in range(19):
      n3.append(edu)
  return {"result": "".join(n1) + "".join(n2) + "".join(n3)}
