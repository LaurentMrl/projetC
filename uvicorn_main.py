from multiprocessing import freeze_support

import uvicorn


def start_server_fastapi(
    host="127.0.0.1", port=8000, num_workers=4, loop="asyncio", reload=True
):
    uvicorn.run(
        "sql_app.main:app",
        host=host,
        port=port,
        workers=num_workers,
        loop=loop,
        reload=reload,
    )


def start_server_web(
    host="127.0.0.1", port=8080, num_workers=4, loop="asyncio", reload=True
):
    uvicorn.run(
        "web.main:app",
        host=host,
        port=port,
        workers=num_workers,
        loop=loop,
        reload=reload,
    )


def start_server_retrieve_csv_and_request_db(
    host="127.0.0.1", port=9000, num_workers=4, loop="asyncio", reload=True
):
    uvicorn.run(
        "data_retrieve.main:app",
        host=host,
        port=port,
        workers=num_workers,
        loop=loop,
        reload=reload,
    )


if __name__ == "__main__":
    freeze_support()  # Needed for pyinstaller for multiprocessing on WindowsOS
    start_server_fastapi(num_workers=1)
    # start_server_web(num_workers=2)
    start_server_retrieve_csv_and_request_db(num_workers=2)
