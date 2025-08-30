import type { Influencer } from "../models/Influencer";

export interface RateRequest {
  topic?: string;
  influencers: Influencer[];
}
