from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='10.128.0.3', port=8000)
