
import time
from urllib import response
from ollama import Client

# Models already downloaded on your Mac
AVAILABLE_MODELS = [
    "gemma3:1b",
    "llama3.2:latest"
]


def ask_ai(topic, question, level, model_name):
    client = Client(
        host="http://localhost:11434",
        timeout=120.0
    )

    
    instructions = f"""
    You are TechBit, a friendly technical tutor.

    Your task is to answer one technical question at a
    {level} level.

    Follow these rules:

    1. Start by answering the question directly.
    2. Use simple, clear language.
    3. Include exactly one real-world software example.
    4. Avoid repetition and unnecessary introductions.
    5. Do not explain unrelated concepts.
    6. Keep the entire response under 120 words.
    7. Finish with one short key takeaway.
    8. Do not generate additional sections after
    the key takeaway.

    Adapt the technical depth to the student's level.

    For Beginner:
    Use an everyday analogy and avoid jargon.

    For Intermediate:
    Explain the mechanism and one practical use case.

    For Advanced:
    Include implementation details and one tradeoff.

    Answer the student's question now.
    """


    messages = [
        {
            "role": "system",
            "content": instructions
        },
        {
            "role": "user",
            "content": (
                f"Today's concept: {topic}\n"
                f"Student's question: {question}"
            )
        }
    ]

    start_time = time.perf_counter()

    response = client.chat(
        model=model_name,
        messages=messages,
        options={
            "temperature": 0.4,
            "num_predict": 350
        }
    )

    elapsed_time = time.perf_counter() - start_time

    
    # Ollama durations are reported in nanoseconds
    generation_seconds = (
        response.eval_duration / 1_000_000_000
        if response.eval_duration else 0
    )

    tokens_generated = response.eval_count or 0

    tokens_per_second = (
        tokens_generated / generation_seconds
        if generation_seconds > 0 else 0
    )

    return {
    "answer": response.message.content or "No answer generated.",
    "model": model_name,
    "time": round(elapsed_time, 2),
    "tokens": tokens_generated,
    "tokens_per_second": round(tokens_per_second, 2),
    "stop_reason": response.done_reason
}
