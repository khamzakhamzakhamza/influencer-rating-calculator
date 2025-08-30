import type { RateRequest } from "./rateRequest";
import type { RateResponse } from "./RateResponse";

//todo: Make cofigurable
const url = "http://localhost:8080/";

export class RatingService {
  async rate(request: RateRequest): Promise<RateResponse> {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: RateResponse = await response.json();
      console.log("Response:", data);
      
      return data; 
    } catch (error) {
      console.error("Error fetching data:", error);
      throw error;
    }
  }
}