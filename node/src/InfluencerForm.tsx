import { Button, Card, Form, Input } from 'antd'
import { CloseOutlined } from "@ant-design/icons";
import './App.css'
import AudienceForm from './AudienceForm'
import PostForm from './PostForm'
import type { Influencer } from './models/Influencer';
import type { Post } from './models/Post';

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
    <Card 
      style={{ maxWidth: 500, marginBottom: 16 }}
      extra={
        <Button
          type="text"
          size="small"
          icon={<CloseOutlined />}
          onClick={onDelete}
        />
      }
    >
      <Form layout="vertical">
        <Form.Item label="Name">
          <Input
            name="name"
            value={influencer.name}
            onChange={(e) => onChange({ ...influencer, name: e.target.value })}
            placeholder="Enter influencer name"
          />
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
      </Form>
    </Card>
  )
}

export default InfluencerForm
