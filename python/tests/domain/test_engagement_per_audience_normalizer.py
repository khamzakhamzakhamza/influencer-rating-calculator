from datetime import datetime, timedelta, timezone
import uuid
import pytest
from src.domain.audience import Audience
from src.domain.calculator.metric_normalizers.engagement_per_audience_normalizer import EngagementPerAudienceNormalizer
from src.domain.post import Post

@pytest.mark.parametrize("audience_size, reactions, comments, reposts, expected", [
    (100, 100, 5, 5, 1),
    (5001, 1000, 150, 50, 0.363),
    (10001, 1500, 200, 70, 0.804),
    (25001, 3000, 500, 60, 0.791),
    (100_001, 1500, 400, 10, 0.239),
])
def test_normalize_when_give_valid_values_should_normalize(audience_size, reactions, comments, reposts, expected):
    # Arrange
    normalizer = EngagementPerAudienceNormalizer()
    audience = Audience(size=audience_size, executive=10, professionals=80)
    days = [0,2,9]
    posts = [ post_factory(d, reactions = reactions, comments = comments, reposts = reposts) for d in days ]

    # Act
    normalized_value = normalizer.normalize(audience, posts)

    # Assert
    assert normalized_value == expected
    
def test_normalize_when_posts_older_than_three_month_should_ignore():
    # Arrange
    normalizer = EngagementPerAudienceNormalizer()
    audience = Audience(size=100, executive=10, professionals=80)
    days = [0,2,100]
    posts = [ post_factory(d,  reactions = 10, comments = 5, reposts = 0) for d in days ]

    # Act
    normalized_value = normalizer.normalize(audience, posts)

    # Assert
    assert normalized_value == 0.309

def test_normalize_when_audience_size_zero_should_normalize():
    # Arrange
    normalizer = EngagementPerAudienceNormalizer()
    audience = Audience(size=0, executive=0, professionals=0)
    days = [0,2]
    posts = [ post_factory(d,  reactions = 10, comments = 5, reposts = 0) for d in days ]

    # Act
    normalized_value = normalizer.normalize(audience, posts)

    # Assert
    assert normalized_value == 1

def test_normalize_when_exec_plus_prof_exceeds_size_should_throw():
    # Arrange
    normalizer = EngagementPerAudienceNormalizer()
    audience = Audience(size=0, executive=10, professionals=80)
    days = [0]
    posts = [ post_factory(d,  reactions = 10, comments = 5, reposts = 0) for d in days ]

    # Act / Assert
    with pytest.raises(ValueError, match="Invalid audience makeup"):
        normalizer.normalize(audience, posts)


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
