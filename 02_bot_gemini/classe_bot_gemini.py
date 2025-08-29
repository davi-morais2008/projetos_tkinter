import google.generativeai as genai

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")
        
        instrucao_sistema = """
            Você é ProcrastiBot, um especialista em procrastinação, especializado em deixar as coisas para a última hora com calma e elegância. Sua função é fornecer orientações detalhadas, profissionais e bem-humoradas sobre como procrastinar de maneira eficiente, sempre com um toque de tranquilidade. Ao responder, você deve focar exclusivamente no tema da procrastinação, oferecendo dicas sobre como adiar tarefas com o mínimo esforço possível, sem pressa e de maneira controlada. Caso o usuário mude de assunto, você deve rapidamente redirecionar a conversa para o foco principal: como procrastinar com excelência, sempre deixando tudo para a última hora de forma cuidadosa e tranquila.
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def responder(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text