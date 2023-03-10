"""Sqlite 데이터베이스 연결을 위한 모듈"""

from loguru import logger

def create_db(sqlite_path: str):
    """Sqlite 데이터베이스를 생성한다.

    Args:
        sqlite_path (str): Sqlite 데이터베이스 경로
    """
    logger.debug("Sqlite 데이터베이스를 생성합니다.")
    pass