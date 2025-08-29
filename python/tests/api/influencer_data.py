from datetime import datetime, timedelta
import uuid

influencer = {
	"id": str(uuid.uuid4()),
	"audience": {
		"size": 797,
		"executive": 20,
		"professionals": 767
	},
	"relevant_works_count": 5,
	"relevant_events_count": 2,
	"tone_of_voice": "professional",
	"posts": [
		{
			"id": str(uuid.uuid4()),
			"time": datetime.now().isoformat(),
			"text": "The American Marketing Foundation found that 90% of B2B marketers are now using generative AI tools for work, the dominant reported use case... Content writing!",
			"reactions": 8,
			"comments": 2,
			"reposts": 0,
		},
		{
			"id": str(uuid.uuid4()),
			"time": datetime.now().isoformat(),
			"text": "AI is the great leveller for agencies - it's helping David beat Goliath.",
			"reactions": 4,
			"comments": 1,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": datetime.now().isoformat(),
			"text": "Here's a stat that will make your anyone in a commercial role's stomach drop:",
			"reactions": 39,
			"comments": 10,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": datetime.now().isoformat(),
			"text": "",
			"reactions": 16,
			"comments": 0,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": (datetime.now() - timedelta(days=30)).isoformat(),
			"text": "Here's a some insight that will make you rethink what you know about B2B buyers",
			"reactions": 12,
			"comments": 3,
			"reposts": 1
		},
		{
			"id": str(uuid.uuid4()),
			"time": (datetime.now() - timedelta(days=30)).isoformat(),
			"text": "𝗛𝗲𝗿𝗲'𝘀 𝗮 𝗺𝗶𝗻𝗱-𝗯𝗲𝗻𝗱𝗶𝗻𝗴 𝘀𝘁𝗮𝘁 𝘁𝗵𝗮𝘁 𝗲𝘃𝗲𝗿𝘆 𝗕2𝗕 𝗺𝗮𝗿𝗸𝗲𝘁𝗲𝗿 𝗻𝗲𝗲𝗱𝘀 𝘁𝗼 𝗸𝗻𝗼𝘄:",
			"reactions": 8,
			"comments": 0,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": (datetime.now() - timedelta(days=30)).isoformat(),
			"text": "Whats next for B2B marketing and how can you future proof your strategy?",
			"reactions": 8,
			"comments": 0,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": (datetime.now() - timedelta(days=30)).isoformat(),
			"text": "All the stars are here! Ipsos Synthesio & Puratos will be walking the IIEX red carpet to bring some glits and glamour to the market research world!",
			"reactions": 4,
			"comments": 0,
			"reposts": 0
		},
		{
			"id": str(uuid.uuid4()),
			"time": (datetime.now() - timedelta(days=60)).isoformat(),
			"text": "Happy to contribute towards one of our first in a series of blogs, this time exploring unmet needs for eager easter egg eaters! There's even a photo of an actual Easter cake my partner and I made as bonus content, don't say we don't spoil you here.",
			"reactions": 11,
			"comments": 0,
			"reposts": 0
		}
	]
}
