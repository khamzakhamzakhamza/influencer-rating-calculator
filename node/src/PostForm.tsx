import type { Post } from "./models/Post";
import { Form, Input, InputNumber, Card, DatePicker, Button } from "antd";
import { CloseOutlined } from "@ant-design/icons";
import dayjs from "dayjs";

interface PostFormProps {
  post: Post;
  onChange: (updated: Post) => void;
  onDelete: () => void;
}

function PostForm({ post, onChange, onDelete }: PostFormProps) {
  return (
    <Card style={{ maxWidth: 500, marginBottom: 16}}>
      <div style={{ width: '100%', height: 30 }}>
        <Button
          style={{ float: "right" }}
          type="text"
          size="small"
          icon={<CloseOutlined />}
          onClick={onDelete}
        />
      </div>

      <Form.Item label="Text">
        <Input.TextArea
          name="text"
          value={post.text}
          onChange={(e) => onChange({ ...post, text: e.target.value })}
          placeholder="Enter post text"
        />
      </Form.Item>

      <Form.Item label="Reactions">
        <InputNumber
          style={{ width: "100%" }}
          value={post.reactions}
          onChange={(value) => onChange({ ...post, reactions: value ?? 0 })}
          placeholder="Enter number of reactions"
        />
      </Form.Item>

      <Form.Item label="Comments">
        <InputNumber
          style={{ width: "100%" }}
          value={post.comments}
          onChange={(value) => onChange({ ...post, comments: value ?? 0 })}
          placeholder="Enter number of comments"
        />
      </Form.Item>

      <Form.Item label="Reposts">
        <InputNumber
          style={{ width: "100%" }}
          value={post.reposts}
          onChange={(value) => onChange({ ...post, reposts: value ?? 0 })}
          placeholder="Enter number of reposts"
        />
      </Form.Item>

      <Form.Item label="Date">
        <DatePicker
          showTime
          style={{ width: "100%" }}
          value={dayjs(post.time)}
          onChange={(date) => {
            onChange({ ...post, time: date ? date.toDate() : new Date() });
          }}
          placeholder="Select post date & time"
        />
      </Form.Item>
    </Card>
  );
}

export default PostForm;
