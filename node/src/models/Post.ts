export interface Post {
  id: string;
  time: Date;
  text: string;
  views?: number;
  reactions: number;
  comments: number;
  reposts: number;
}
