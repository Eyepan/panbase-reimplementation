import uvicorn

from app import app
from config import ADMIN_PORT, API_PORT, LOG_LEVEL, RELOAD
from logger import logger


if __name__ == "__main__":
    logger.info(f"Admin server started on port {ADMIN_PORT}")
    uvicorn.run("app:app" if RELOAD else app, host="0.0.0.0",
                port=API_PORT, log_level=LOG_LEVEL.lower(), reload=RELOAD)  # noqa: because of some weird bug with uvicorn, it rather reloads the dist folder inside admin-ui instead of the python folder, so guess who has to deal with that? me. # noqa: E501
    logger.info(f"Admin server stopped on port {ADMIN_PORT}")
