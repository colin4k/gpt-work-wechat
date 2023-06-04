import uvicorn

web_port = 20052

if __name__ == "__main__":
    uvicorn.run("wework_api.api:app", host="0.0.0.0", port=web_port,reload=True)