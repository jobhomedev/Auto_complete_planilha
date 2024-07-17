from basics.helper_xlsx import HelperXlsx, INTERACTION_ID, OPCAO_SELECIONADA, JORNADA_DO_CLIENTE_NO_CHATBOT, FINALIZACAO_DO_CONTATO
from basics.get_file_name import get_file_name
from basics.find_ticket_by_id import find_ticket_by_id
from basics.getAnalyzers import getAnalyzers

fileName:str = get_file_name()

# Instancia a classe para lidar com o xlsx
helperXlsx = HelperXlsx()

# Ler os dados do arquivo xlsx
file = helperXlsx.read(fileName)

# Pular a primeira linha
for index, line in enumerate(file):
    
    if index == 0:
        continue
    
    # Forma de obter(e definir os dados do ticket)
    messages = find_ticket_by_id(line[INTERACTION_ID])

    # pula os vazios
    if not line[INTERACTION_ID]:
        continue

    # instancia o analisador
    analyzers = getAnalyzers()
    
    for analyzer in analyzers:

        # Pula caso a estrutura não seja valida
        if not analyzer.isValid(messages):
            continue
    
        # Pega as qualificações
        qualifications = analyzer.getQualifications(messages)

        # Insere as qualificações no ticket
        file[index][OPCAO_SELECIONADA] = qualifications['selectedOption']
        file[index][JORNADA_DO_CLIENTE_NO_CHATBOT] = qualifications['customerJourney']
        file[index][FINALIZACAO_DO_CONTATO] = qualifications['finalizationOfTheContract']
        
        # Salva o arquivo
        helperXlsx.write('./output/file.xlsx', file)

# Salva o arquivo
helperXlsx.write('./output/file.xlsx', file)
