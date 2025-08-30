export interface RateResponse {
  id: string;
  audience_size: number;
  audience_makeup: number;
  posts_per_week: number;
  engagement_per_audience: number;
  relevant_events?: number;
  relevant_works?: number;
  tone_of_voice: number;
  rating: number;
}
