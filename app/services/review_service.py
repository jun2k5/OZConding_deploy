"""
서비스 계층 (Service Layer)
- 라우트에서 직접 DB 조작하지 않고
- 이 모듈을 거쳐서 DB CRUD 실행
"""

from app import SessionLocal
from app.models import Review


def get_all_reviews():
    """모든 리뷰 조회"""
    # TODO: DB 세션을 열고 모든 리뷰를 조회하세요
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()
#    send_reviews = [{"id": r.id, "title" : r.title, "content": r.content, "rating": r.rating} for r in reviews]
#    return send_reviews
    return reviews
    #return reviews, 200



def create_review(title, content, rating):
    """리뷰 생성"""
    # TODO: Review 객체를 생성하고 DB에 추가한 뒤 commit 하세요
    db = SessionLocal()
    new_review = Review(title=title, content=content, rating=rating)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    db.close()

    return new_review.id, 201


def get_review_by_id(review_id):
    """ID로 리뷰 조회"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 조회하세요
    db = SessionLocal()
    review = db.query(Review).get(review_id)

    if not review:
        db.close()
        return None
    db.close()

    return review



def update_review(review_id, title, content, rating):
    """리뷰 수정"""
    # TODO: review_id 에 해당하는 리뷰를 조회 후, 필드를 수정하고 commit 하세요
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if not review:
        db.close()
        return None

    # return {"msg":"Review not Found"}, 404

    review.title = title
    review.content = content
    review.rating = rating
    db.commit()
    db.refresh(review)

    db.close()

    return {"msg":"Successfully updated review"}, 201


def delete_review(review_id):
    """리뷰 삭제"""
    # TODO: review_id 에 해당하는 리뷰를 DB에서 삭제하고 commit 하세요
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if not review:
        db.close()
        return None
    
    db.delete(review)
    db.commit()

    db.close()

    return {"msg":"Successfully deleted review"}, 204


