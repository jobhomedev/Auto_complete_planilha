from basics.find_ticket_by_id import Message
from typing import List
from basics.qualification import Qualification

# 961e3554b38a49fcab93d70ab3b0fb21

class Analyzer523 :

    def isValid(
        self,
        messagesClient: List[Message],
        allMessages: List[Message],
    ) -> bool:

        if not (len(messagesClient) == 24):
            return False
    
        if not (messagesClient[1]["sender"] == "bot" and messagesClient[1]["message"].startswith("Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê, seu assistente virtual.\n\nPara obter informações sob")):
            return False
    
        if not (messagesClient[3]["sender"] == "bot" and messagesClient[3]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[5]["sender"] == "bot" and messagesClient[5]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[7]["sender"] == "bot" and messagesClient[7]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[9]["sender"] == "bot" and messagesClient[9]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[11]["sender"] == "bot" and messagesClient[11]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[13]["sender"] == "bot" and messagesClient[13]["message"].startswith("*Digite a opção desejada para*:\n\n1 - Bloqueio\n2 - Desbloqueio\n3 - Segunda via ou cartão adiciona")):
            return False
    
        if not (messagesClient[15]["sender"] == "bot" and messagesClient[15]["message"].startswith("")):
            return False
    
        if not (messagesClient[17]["sender"] == "bot" and messagesClient[17]["message"].startswith("Desculpe não entendi. Retornaremos para o início.\n\n Seja bem-vindo(a) à Nio Digital!\n\nSou o Alê,")):
            return False
    
        if not (messagesClient[19]["sender"] == "bot" and messagesClient[19]["message"].startswith("Ótimo. Em que posso ajudar?\nㅤ *Digite a opção desejada para*:\n\n1 - Limite disponível para utiliza")):
            return False
    
        if not (messagesClient[21]["sender"] == "bot" and messagesClient[21]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        if not (messagesClient[23]["sender"] == "bot" and messagesClient[23]["message"].startswith("Tivemos um problema com o seu atendimento. Vamos lá, vamos começar novamente. *Digite a opção deseja")):
            return False
    
        return True

    def getQualifications(
            self,
            messagesClient: List[Message],
            allMessages: List[Message],
        ) -> Qualification:
        return {
            "selectedOption": '',
            "customerJourney": '',
            "finalizationOfTheContract": '',
        }
    