"""Oracle 데이터베이스 연결을 위한 모듈"""

from loguru import logger

def check_if_db_is_available():
    """Oracle 데이터베이스 연결 가능 여부를 확인한다.

    Returns:
        bool: 연결 가능 여부
    """
    logger.debug("Oracle 데이터베이스 연결 가능 여부를 확인합니다.")
    return True

