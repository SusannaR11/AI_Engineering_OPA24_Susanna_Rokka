from pydantic_ai.agent import AgentRunResult
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()


class JokeBot:               #class with chatbot and injections from google gemini
    def __init__(self):
        self.chat_agent = Agent( # define agent with a system prompt 'prompt engineering' or as in this case 'zero-shot prompting' - no examples given for the agent to learn from.
            "google-gla:gemini-2.5-flash-preview-05-20",
            system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add emojis in your language",
        )

        self.result = None

# one-shot -> Follow this structure. Example
# Q: {user question} 'What is the meaning of life?'
# A: The meaning of life is 42 and programming.

    def chat(self, prompt: str) -> AgentRunResult:

        message_history = self.result.all_messages() if self.result else None
        self.result = self.chat_agent.run_sync(prompt, message_history=message_history) # memory for the chatbot
        # message_history saves and self.result contains all chat

        return {"user": prompt, "bot": self.result.output}


if __name__ == "__main__":
    bot = JokeBot()
    result = bot.chat("Hej svej")
    result = bot.chat("Hej svej igen")
    print(result)
    print(bot.result.all_messages())