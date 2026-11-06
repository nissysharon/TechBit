from datetime import date

# Fixed ordered catalog: the same date yields the same concept for every user.
WORDS = [
    {
        'term': 'Latency',
        'definition': 'The time between requesting something and receiving the result.',
        'analogy': 'You order coffee. Latency is how long it takes before the coffee arrives.',
        'example': 'An API with 200 ms latency responds in about two-tenths of a second.',
        'resources': [
            {'title': 'Cloudflare — What is latency?', 'url': 'https://www.cloudflare.com/learning/performance/glossary/what-is-latency/'},
        ],
    },
    {
        'term': 'Idempotency',
        'definition': 'An operation is idempotent when repeating it has the same intended effect as performing it once.',
        'analogy': 'Pressing an elevator button twice still requests the same elevator stop.',
        'example': 'Setting a user preference to dark mode repeatedly leaves it set to dark mode.',
        'resources': [
            {'title': 'MDN — HTTP request methods', 'url': 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods'},
        ],
    },
    {
        'term': 'Embedding',
        'definition': 'A numerical representation that helps software compare the meaning or features of data.',
        'analogy': 'Items with similar meanings are placed near each other on an imaginary map.',
        'example': 'A search system can find related articles without relying on exact matching words.',
        'resources': [
            {'title': 'OpenAI — Embeddings guide', 'url': 'https://platform.openai.com/docs/guides/embeddings'},
        ],
    },
    {
        'term': 'Rate Limiting',
        'definition': 'Restricting how many requests a client can make within a given period.',
        'analogy': 'A venue admits only a fixed number of visitors every minute.',
        'example': 'An API might allow 60 requests per minute for each account.',
        'resources': [
            {'title': 'Cloudflare — Rate limiting', 'url': 'https://www.cloudflare.com/learning/bots/what-is-rate-limiting/'},
        ],
    },
    {
        'term': 'Retrieval-Augmented Generation (RAG)',
        'definition': 'A technique that supplies retrieved information to a generative model when answering a question.',
        'analogy': 'An assistant consults relevant pages of a manual before answering.',
        'example': 'A documentation chatbot searches product manuals before responding.',
        'resources': [
            {'title': 'IBM — What is RAG?', 'url': 'https://www.ibm.com/think/topics/retrieval-augmented-generation'},
        ],
    },
    
    {
        "term": "Caching",
        "definition": "Storing frequently used data temporarily so it can be accessed faster.",
        "analogy": "Keeping your favorite book on your desk instead of going to the library every time.",
        "example": "A website caches frequently requested content to reduce response time.",
        "resources": [
            {
                "title": "Cloudflare — What is caching?",
                "url": "https://www.cloudflare.com/learning/cdn/what-is-caching/"
            }
        ],
    },

    {
        "term": "Load Balancing",
        "definition": "Distributing incoming network traffic across multiple servers to ensure no single server is overwhelmed.",
        "analogy": "Directing cars to different lanes on a highway to prevent traffic jams.",
        "example": "A web application uses a load balancer to distribute user requests across multiple servers for better performance.",
        "resources": [
            {
                "title": "AWS — What is load balancing?",
                "url": "https://aws.amazon.com/elasticloadbalancing/"               
            }

        ],
    },

    {
        "term": "Continuous Integration (CI)",
        "definition": "A development practice where developers frequently merge their code changes into a shared repository, which is then automatically tested and built.",
        "analogy": "Like a team of chefs constantly adding ingredients to a shared pot, ensuring the dish is always tested for taste.",
        "example": "A software team uses a CI tool to automatically run tests and build their application whenever new code      is pushed to the repository.",                                                          
        "resources": [
            {
                "title": "Atlassian — What is continuous integration?",
                "url": "https://www.atlassian.com/continuous-delivery/continuous-integration"

        } 
        ]
    },      
]

START_DATE = date(2026, 1, 1)


def todays_word(on_date: date) -> dict:
    days_since_start = (on_date - START_DATE).days
    return WORDS[days_since_start % len(WORDS)]
