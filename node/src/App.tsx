import { useState } from 'react'
import { v4 as uuidv4 } from "uuid";
import './App.css'
import InfluencerForm from './InfluencerForm'
import { ToneOfVoice } from './models/ToneOfVoice';
import { Button, Card, Form } from 'antd';
import type { Influencer } from './models/Influencer';

const newPost = () => ({
  id: uuidv4(),
  time: new Date(),
  text: "",
  reactions: 0,
  comments: 0,
  reposts: 0,
});

const newAudience = () => ({
  size: 0,
  executive: 0,
  professionals: 0
});

const newInfluencer = () => ({
  id: uuidv4(),
  name: "",
  audience: newAudience(),
  relevant_works_count: 0,
  relevant_events_count: 0,
  tone_of_voice: ToneOfVoice.CONVERSATIONAL,
  posts: [newPost()],
});

function App() {
  const [influencers, setInfluencers] = useState<Influencer[]>([newInfluencer()]);

  const addPost = (index: number) => {
    const updatedInfluencers = [...influencers];
    updatedInfluencers[index] = {
      ...updatedInfluencers[index],
      posts: [...updatedInfluencers[index].posts, newPost()],
    };
    setInfluencers(updatedInfluencers);
  };

  const updateInfluencer = (index: number, updatedInfluencer: Influencer) => {
    const updatedInfluencers = [...influencers];
    updatedInfluencers[index] = updatedInfluencer;
    setInfluencers(updatedInfluencers);
  };

  return (
    <>
      <h1>Influencer Rating Calculator</h1>
      
      <Card style={{ maxWidth: 540 }}>
        <Form layout="vertical">
          <Form.Item label="Influencers">
            {influencers.map((influencer, idx) =>
              <InfluencerForm key={idx} 
                influencer={influencer} 
                addPost={() => addPost(idx)}
                onChange={(updated) => updateInfluencer(idx, updated)}
                onDelete={() => setInfluencers(influencers.filter((_, i) => i !== idx))}
              />
            )}
            <Button type="primary" onClick={()=> setInfluencers([...influencers, newInfluencer()])}>
              Add Influencer
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </>
  )
}

export default App
