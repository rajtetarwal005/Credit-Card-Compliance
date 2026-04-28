from backend.app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # docker run -p 10000:10000 credit-card-app