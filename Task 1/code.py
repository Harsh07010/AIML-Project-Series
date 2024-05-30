class SimpleChatbot:
    def init(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm here to help you. How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def respond_to_question(self, user_input):
        responses = {
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "what is your name": "I'm your friendly chatbot.",
            "what can you do": "I can chat with you and remember our previous conversations.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "bye": self.farewell()
        }
        return responses.get(user_input.lower(), "I'm sorry, I didn't understand that. Can you please rephrase?")

    def ask_questions(self):
        questions = [
            "What's your name?",
            "How are you feeling today?",
            "What can I help you with?"
        ]
        answers = {}
        for question in questions:
            print(question)
            user_response = input("You: ")
            answers[question] = user_response
        self.context.update(answers)
        return answers

    def recall_context(self):
        if not self.context:
            return "We haven't chatted before. Let's start a new conversation!"
        context_summary = "Here's what we talked about before:\n"
        for question, answer in self.context.items():
            context_summary += f" - {question} You said: {answer}\n"
        return context_summary

    def handle_error(self, user_input):
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def chat(self):
        print(self.greet())
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["bye", "goodbye"]:
                print(self.farewell())
                break
            elif user_input.lower() in ["recall", "context"]:
                print(self.recall_context())
            else:
                response = self.respond_to_question(user_input)
                if response.startswith("I'm sorry"):
                    response = self.handle_error(user_input)
                print("Chatbot: " + response)
            # Ask user questions in the flow
            if user_input.lower() == "ask me questions":
                answers = self.ask_questions()
                print("Chatbot: Thanks for sharing! I'll remember that.")
                print(self.recall_context())

if name == "main":
    bot = SimpleChatbot()
    bot.chat()