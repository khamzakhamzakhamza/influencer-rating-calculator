import { Button, Card, Form, Input, Select } from 'antd'
import { CloseOutlined } from "@ant-design/icons";
import './App.css'
import AudienceForm from './AudienceForm'
import PostForm from './PostForm'
import type { Influencer } from './models/Influencer';
import type { Post } from './models/Post';
import { ToneOfVoice } from './models/ToneOfVoice';

const { Option } = Select;

interface InfluencerFormProps {
  influencer: Influencer;
  addPost: () => void;
  onChange: (updated: Influencer) => void;
  onDelete: () => void;
}

function InfluencerForm({influencer, addPost, onChange, onDelete}: InfluencerFormProps) {
  const updatePost = (index: number, updatedPost: Post) => {
    const updatedPosts = [...influencer.posts];
    updatedPosts[index] = updatedPost;
    onChange({ ...influencer, posts: updatedPosts });
  };

  return (
    <Card style={{ maxWidth: 500, marginBottom: 16 }}>
      <div style={{ width: '100%', height: 30 }}>
        <Button
          style={{ float: "right" }}
          type="text"
          size="small"
          icon={<CloseOutlined />}
          onClick={onDelete}
        />
      </div>

      <Form.Item label="Id">
        <Input
          name="id"
          value={influencer.id}
          onChange={(e) => onChange({ ...influencer, id: e.target.value })}
          placeholder="Enter influencer id"
        />
      </Form.Item>

      <Form.Item label="Name">
        <Input
          name="name"
          value={influencer.name}
          onChange={(e) => onChange({ ...influencer, name: e.target.value })}
          placeholder="Enter influencer name"
        />
      </Form.Item>

      <Form.Item label="Tone of Voice">
        <Select
          value={influencer.tone_of_voice}
          style={{ width: "100%" }}
          onChange={(value) => onChange({ ...influencer, tone_of_voice: value })}
        >
          <Option value={ToneOfVoice.CONVERSATIONAL}>Conversational</Option>
          <Option value={ToneOfVoice.PROFESSIONAL}>Professional</Option>
          <Option value={ToneOfVoice.EDUCATIONAL}>Educational</Option>
          <Option value={ToneOfVoice.SCIENTIFIC}>Scientific</Option>
          <Option value={ToneOfVoice.MOTIVATIONAL}>Motivational</Option>
          <Option value={ToneOfVoice.COMEDIC}>Comedic</Option>
          <Option value={ToneOfVoice.PROVOCATIVE}>Provocative</Option>
        </Select>
      </Form.Item>
      
      <Form.Item label="Audience">
        <AudienceForm 
          audience={influencer.audience}
          onChange={(updated) => onChange({ ...influencer, audience: updated })}
        />
      </Form.Item>

      <Form.Item label="Posts">
        {influencer.posts.map((post, idx) => 
          <PostForm key={post.id}
            post={post}
            onChange={(updated) => updatePost(idx, updated)}
            onDelete={() => {
              const updatedPosts = influencer.posts.filter((_, i) => i !== idx);
              onChange({ ...influencer, posts: updatedPosts });
            }}
          />
        )}
        <Button type="primary" onClick={addPost}>
          Add Post
        </Button>
      </Form.Item>
    </Card>
  )
}

export default InfluencerForm
