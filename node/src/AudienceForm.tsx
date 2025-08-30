import { Form, InputNumber, Card } from "antd";
import type { Audience } from "./models/Audience";

interface AudienceFormProps {
  audience: Audience;
  onChange: (updated: Audience) => void;
}

function AudienceForm({audience, onChange}: AudienceFormProps) {
  return (
    <Card style={{ maxWidth: 500 }}>
      <Form layout="vertical">
        <Form.Item label="Size">
          <InputNumber
            style={{ width: "100%" }}
            value={audience.size}
            onChange={(value) => onChange({ ...audience, size: value ?? 0 })}
            placeholder="Enter audience size"
          />
        </Form.Item>

        <Form.Item label="Number of Executives">
          <InputNumber
            style={{ width: "100%" }}
            value={audience.executive}
            onChange={(value) => onChange({ ...audience, executive: value ?? 0 })}
            placeholder="Enter number of excutives in the audience"
          />
        </Form.Item>

        <Form.Item label="Number of Professionals">
          <InputNumber
            style={{ width: "100%" }}
            value={audience.professionals}
            onChange={(value) => onChange({ ...audience, professionals: value ?? 0 })}
            placeholder="Enter number of professionals in the audience"
          />
        </Form.Item>
      </Form>
    </Card>
  );
}

export default AudienceForm;
