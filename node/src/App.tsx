import { useState } from 'react'
import { v4 as uuidv4 } from "uuid";
import InfluencerForm from './InfluencerForm'
import { ToneOfVoice } from './models/ToneOfVoice';
import { Row, Col, Button, Form, theme, Layout, Typography, Flex } from 'antd';
import type { Influencer } from './models/Influencer';
import type { RateRequest } from './services/RateRequest';
import { RatingService } from './services/RatingService';
import type { RateResponse } from './services/RateResponse';
import RatingCard from './RatingCard';

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

const service = new RatingService();

const { Header, Content, Footer } = Layout;

const { Title } = Typography;

function App() {
  const [influencers, setInfluencers] = useState<Influencer[]>([newInfluencer()]);
  const [loading, setLoading] = useState(false);
  const [ratings, setRatings] = useState<RateResponse[] | undefined>();

  const {
    token: { colorBgLayout },
  } = theme.useToken();

  const calculate = async () => {
    setLoading(true);
    
    try {
      const request: RateRequest = { influencers };
      const response = await service.rate(request);
      setRatings(response);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

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
    <Layout style={{  minHeight: "100vh", minWidth: "100vw" }}>
      <Header style={{ background: colorBgLayout, height: 90 }}>
        <Flex justify="center" align="middle" style={{ height: '100%' }}>
          <Title>Influencer Rating Calculator</Title>
        </Flex>
      </Header>
      
      <Content>
        <Flex justify="center" align="middle">
          <Row style={{ width: 1100 }}>
            <Col span={10}>
              <div style={{ maxWidth: 540, background: colorBgLayout }}>
                <Form layout="vertical">
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
                </Form>
              </div>
            </Col>
            <Col span={4}>
              <Flex justify="center" align="middle" style={{ height: '100%', paddingTop: 25 }}>
                <Button 
                  type="primary"
                  loading={loading} 
                  onClick={calculate}
                >
                  Calculate
                </Button>
              </Flex>
            </Col>
            <Col span={10}>
              <div style={{ maxWidth: 540, background: colorBgLayout }}>
                {ratings && ratings.length > 0 
                  ? (ratings.map((rating, idx) => <RatingCard key={idx} rating={rating} />)) 
                  : (<p>Fill influencers data and click "Calculate"</p>)}
              </div>
            </Col>
          </Row>
        </Flex>
      </Content>

      <Footer style={{ textAlign: 'center' }}>Influencer Rating Calculator ©2025</Footer>
    </Layout>
  )
}

export default App
