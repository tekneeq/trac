import uvicorn

# uvicorn is an ASGI (Asynchronous Server Gateway Interface)

if __name__ == "__main__":
    uvicorn.run("trac:app", host="0.0.0.0", port=8000, reload=True)