import { Card, Descriptions } from "antd";
import type { RateResponse } from "./services/RateResponse";

interface RatingCardProps {
  rating: RateResponse;
}

function RatingCard({rating}: RatingCardProps) {
  return (
    
    <Card style={{ maxWidth: 540, marginBottom: 16 }}>
      <Descriptions column={1}>
        <Descriptions.Item label="Id">{rating.id}</Descriptions.Item>
        <Descriptions.Item label="Name">{rating.name}</Descriptions.Item>
        <Descriptions.Item label="Audience Size">{rating.audience_size}</Descriptions.Item>
        <Descriptions.Item label="Audience Makeup">{rating.audience_makeup}</Descriptions.Item>
        <Descriptions.Item label="Posts Per Week">{rating.posts_per_week}</Descriptions.Item>
        <Descriptions.Item label="Engagement Per Audience">{rating.engagement_per_audience}</Descriptions.Item>
        <Descriptions.Item label="Tone Of Voice">{rating.tone_of_voice}</Descriptions.Item>
        <Descriptions.Item label="Overall"><b>{rating.rating}</b></Descriptions.Item>
      </Descriptions>
    </Card>
  );
}

export default RatingCard;
