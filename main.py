def main():
    print("Hello from fast-store!")


if __name__ == "__main__":
    main()

    # python -m uvicorn main:app --app-dir services\user-service --host 127.0.0.1 --port 8001 --reload