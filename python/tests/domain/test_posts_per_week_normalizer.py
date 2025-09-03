from datetime import datetime, timedelta, timezone
import uuid
import pytest
from src.domain.audience import Audience
from src.domain.calculator.metric_normalizers.posts_per_week_normalizer import PostsPerWeekNormalizer
from src.domain.post import Post

@pytest.mark.parametrize("audience_size, expected", [
    (100, 0.553),
    (5001, 0.794),
    (10001, 0.712),
    (25001, 0.694),
    (100_001, 0.319),
])
def test_normalize_when_give_valid_values_should_normalize(audience_size, expected):
    # Arrange
    normalizer = PostsPerWeekNormalizer()
    audience = Audience(size=audience_size, executive=10, professionals=80)
    days = [0,2,9,14,16,22,24,27,28,37,42,45,47,52,55,62,67,72,74,77,84,2,9,14,16,22,24,27,28,37,42,45,47,52,55,62,67,72,74,77,84]
    posts = [ post_factory(d) for d in days ]

    # Act
    normalized_value = normalizer.normalize(audience, posts)

    # Assert
    assert normalized_value == expected
    
def test_normalize_when_posts_older_than_three_month_should_ignore():
    # Arrange
    normalizer = PostsPerWeekNormalizer()
    audience = Audience(size=100, executive=10, professionals=80)
    days = [0,2,9,14,16,22,24,27,28,37,42,45,47,52,55,62,67,72,74,77,84,90,95,100]
    posts = [ post_factory(d) for d in days ]

    # Act
    normalized_value = normalizer.normalize(audience, posts)

    # Assert
    assert normalized_value == 0.78

def post_factory(days_ago=0, **kwargs) -> Post:
    now = datetime.now(timezone.utc)
    
    return Post(
        id = kwargs.get("id", str(uuid.uuid4())),
        time = now - timedelta(days=days_ago),
        text = kwargs.get("text", ""),
        views = kwargs.get("views", None),
        reactions = kwargs.get("reactions", 0),
        comments = kwargs.get("comments", 0),
        reposts = kwargs.get("reposts", 0),
    )
