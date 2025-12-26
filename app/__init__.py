# app/__init__.py

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session
from .config import Config

# TODO: DB 연결 엔진을 생성하세요 (create_engine)

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS
)

# TODO: 세션(SessionLocal) 객체를 만드세요 (scoped_session)
SessionLocal = sessionmaker(bind=engine)

# TODO: Base 클래스를 만드세요 (declarative_base)
Base = declarative_base()


def create_app():
    """Flask 앱 생성 및 초기화"""
    app = Flask(__name__)

    # TODO: 모델을 import 하세요 (예: from . import models)
    from .models import Review

    # TODO: DB 테이블을 생성하세요 (Base.metadata.create_all)
    Base.metadata.create_all(bind=engine)

    # TODO: 라우트 블루프린트를 등록하세요 (review_routes 불러와서 app.register_blueprint)
    from .routes.review_routes import review_bp

    app.register_blueprint(review_bp)

    #요청이 끝날 때마다 세션 닫기
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.close_all()
        #SessionLocal.remove()

    return app