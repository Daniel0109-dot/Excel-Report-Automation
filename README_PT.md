**Automação de Relatórios Administrativos em Excel**

**Visão Geral**

Este projeto automatiza o processamento de planilhas Excel administrativas aplicando regras de negócio predefinidas, normalizando dados e gerando saídas estruturadas segmentadas por critérios organizacionais (como diretorias ou departamentos).
A automação foi projetada para substituir trabalho manual repetitivo comum em rotinas administrativas e de RH, melhorando a consistência, reduzindo erros e economizando tempo operacional.
Embora originalmente inspirado em necessidades corporativas reais, o projeto foi adaptado e generalizado para ser compartilhado com segurança como exemplo de portfólio.

**Problema**

Equipes administrativas frequentemente trabalham com múltiplos arquivos Excel gerados de diferentes fontes, formatos ou sistemas. Problemas comuns incluem:

- Nomes de colunas e formatos de dados inconsistentes

- Filtragem e mesclagem manual de planilhas

- Aplicação repetitiva das mesmas regras de negócio

- Fluxos de trabalho copiar-e-colar propensos a erros

Estas tarefas são demoradas, difíceis de auditar e não escalam bem com o aumento do volume de dados.

**Solução**

Este projeto fornece uma automação baseada em Python que:

- Lê arquivos Excel de diretórios predefinidos

- Normaliza campos textuais e de data

- Aplica regras de negócio para classificar e filtrar registros

- Consolida dados em uma planilha estruturada "semelhante a um banco de dados"

- Gera arquivos de saída organizados por lógica de negócio (ex: por diretoria)

O objetivo não é substituir sistemas BI completos, mas oferecer uma camada de automação leve, transparente e facilmente adaptável.

**Funcionalidades**

- Detecta e carrega automaticamente o arquivo Excel mais recente do diretório de entrada

- Padroniza e normaliza nomes de colunas para processamento consistente

- Infere atributos de negócio ausentes com base em regras predefinidas

- Filtra e organiza campos de dados essenciais

- Agrupa registros de acordo com lógica de negócio e mapeamentos de responsabilidade

- Gera relatórios Excel estruturados com nomes de arquivos seguros e legíveis

- Usa convenções de nomeação baseadas em data para melhor organização de arquivos

**Tecnologias Utilizadas**

Para executar este projeto localmente, você precisará de:

- **Python 3.10 ou superior**

- Excel (.xlsx) - Formato de entrada/saída

E o projeto depende das seguintes bibliotecas Python:

- pandas - Manipulação de dados

- openpyxl - Manipulação de arquivos Excel

Estas dependências podem ser instaladas usando 'pip'.

**Pré-requisitos**

- Python 3.10 ou superior

- Uso básico de linha de comando

- Arquivos Excel seguindo um padrão estrutural conhecido

**Instalação**

1. Clone este repositório:

git clone https://github.com/Daniel0109-dot/Excel-Report-Automation.git

2. Navegue até o diretório do projeto:

cd Excel-Report-Automation

3. Instale as dependências necessárias:

pip install -r requirements.txt

**Uso**

1. Coloque os arquivos Excel de entrada dentro do diretório input/.

2. Execute o script principal:

python main.py

3. Encontre os relatórios gerados em output/generated_reports/

**Estrutura do Projeto**
```text
Excel Report Automation/
|
|---input/
|   |---- example_files/
|
|---output/
|   |---- generated_reports/
|
|---src/
|   |---- __init__.py
|   |---- config.py
|   |---- file_loader.py
|   |---- text_utils.py
|   |---- data_cleaning.py
|   |---- business_rules.py
|   |---- report_generator.py
|
|--- main.py
|--- requirements.txt
|--- README.md
|--- README_PT.md
|--- .gitignore
|--- LICENSE

```

**Decisões de Design**

- Arquitetura modular: Cada etapa do processo (carregamento, limpeza, regras, saída) é isolada para melhorar legibilidade e manutenibilidade.

- Regras de negócio explícitas: Regras são escritas em código em vez de estarem ocultas em fórmulas Excel, tornando-as mais fáceis de auditar e alterar.

- Comportamento determinístico: Nenhum modelo probabilístico é usado; a mesma entrada sempre produz a mesma saída.

- Saídas legíveis: Os arquivos gerados priorizam clareza em vez de compressão ou performance.

**Limitações Conhecidas**

- Espera-se que os arquivos Excel de entrada sigam um padrão estrutural conhecido

- As regras de negócio são estáticas e codificadas diretamente (sem configuração externa ainda)

- Nenhuma validação automática de esquema é realizada

- O tratamento de erros é intencionalmente simples para manter a lógica transparente

**Melhorias Futuras**

- Configuração externa de regras via JSON ou YAML

- Registros de execução e logging estruturado

- Validação automatizada de esquema

- Integração opcional com Power Automate ou armazenamento em nuvem

**Licença**

Este projeto está licenciado sob a Licença MIT.
Você é livre para usar, modificar e distribuir este software com a atribuição adequada.

**Aviso Legal**

Este projeto é uma versão generalizada e anonimizada de automações administrativas reais. Nenhum dado proprietário, processo interno ou informação confidencial está incluído.

**Autor**

Desenvolvido como parte de um portfólio profissional focado em automação de processos e análise de dados administrativos.
