import type { Audience } from "./Audience";
import type { Post } from "./Post";
import { ToneOfVoice } from "./ToneOfVoice";

export interface Influencer {
  id: string;
  name: string;
  audience: Audience;
  relevant_works_count: number;
  relevant_events_count: number;
  tone_of_voice: typeof ToneOfVoice[keyof typeof ToneOfVoice];
  posts: Post[];
}
