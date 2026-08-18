# Acessibilidade: Conversão de Imagem para Voz

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Azure Vision](https://img.shields.io/badge/Azure%20Vision-Computer%20Vision-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/products/ai-services/ai-vision)
[![Azure Speech](https://img.shields.io/badge/Azure%20Speech-Text%20to%20Speech-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/products/ai-services/ai-speech)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-Automation-2E8B57)](https://pyautogui.readthedocs.io/)

Projeto de acessibilidade que analisa uma imagem, gera uma descrição textual do seu conteúdo e converte essa descrição em áudio.

A solução utiliza o Azure Vision para interpretar a imagem, o Azure Speech Text to Speech para sintetizar o texto e o PyAutoGUI para automatizar determinadas interações no computador.

> Projeto desenvolvido para fins educacionais, com foco em Inteligência Artificial, acessibilidade e automação.

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Problema e solução](#problema-e-solução)
- [Objetivos](#objetivos)
- [Como funciona](#como-funciona)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Pré-requisitos](#pré-requisitos)
- [Configuração do Azure](#configuração-do-azure)
- [Instalação](#instalação)
- [Como executar](#como-executar)
- [Exemplo de fluxo](#exemplo-de-fluxo)
- [Resultados esperados](#resultados-esperados)
- [Limitações](#limitações)
- [Segurança](#segurança)
- [Aprendizados](#aprendizados)
- [Próximos passos](#próximos-passos)
- [Referências](#referências)
- [Autor](#autor)
- [Licença](#licença)

## Sobre o projeto

Pessoas com deficiência visual podem encontrar dificuldades para compreender imagens presentes em ambientes digitais ou físicos. Este projeto explora uma solução baseada em Inteligência Artificial para transformar informações visuais em uma descrição que pode ser ouvida.

O sistema recebe uma imagem, envia o conteúdo para um serviço de visão computacional e obtém uma descrição textual. Em seguida, o texto é enviado ao serviço Azure Speech, que gera o áudio correspondente.

O PyAutoGUI é utilizado para automatizar ações no computador, como interação com janelas, seleção de arquivos ou execução de etapas do fluxo.

## Problema e solução

### Problema

Imagens sem descrição alternativa podem dificultar o acesso à informação por pessoas que dependem de recursos de áudio ou leitores de tela.

### Solução

O projeto utiliza serviços de Inteligência Artificial para:

- Analisar o conteúdo de uma imagem.
- Identificar elementos visuais relevantes.
- Gerar uma descrição em texto.
- Converter a descrição em áudio.
- Automatizar etapas da interação com o computador.

## Objetivos

- Explorar o uso do Azure Vision em um projeto aplicado.
- Utilizar o Azure Speech para síntese de voz.
- Criar uma experiência voltada à acessibilidade.
- Integrar APIs de Inteligência Artificial em Python.
- Automatizar interações com o sistema operacional.
- Praticar organização e documentação de um projeto de IA.
- Demonstrar como visão computacional e áudio podem trabalhar em conjunto.

## Como funciona

O fluxo principal do sistema é:

1. O usuário seleciona ou disponibiliza uma imagem.
2. O programa identifica o arquivo de imagem.
3. A imagem é enviada ao Azure Vision.
4. O serviço analisa a imagem.
5. O programa recebe uma descrição textual.
6. O texto é enviado ao Azure Speech.
7. O serviço gera um áudio com a descrição.
8. O usuário pode ouvir o resultado.

Fluxo simplificado:

```text
Imagem
  |
  v
Azure Vision
  |
Descrição em texto
  |
  v
Azure Speech Text to Speech
  |
  v
Áudio
```

O PyAutoGUI participa da automação de ações definidas pelo projeto, como movimentação do mouse, cliques e interação com elementos da interface.

## Tecnologias utilizadas

- Python.
- Azure AI Vision.
- Azure AI Speech.
- Text to Speech.
- PyAutoGUI.
- APIs REST ou SDKs do Azure, conforme a implementação.
- Manipulação de arquivos e imagens.
- Git e GitHub.

## Estrutura do repositório

```text
Projeto-de-Acessibilidade-Imagem-para-Voz/
├── README.md
├── main.py
├── mouse.py
└── Imagens/
```

### `main.py`

Arquivo principal responsável pelo fluxo de análise da imagem, geração da descrição e conversão do texto em áudio.

### `mouse.py`

Módulo relacionado à automação de ações do mouse ou da interface utilizando PyAutoGUI.

### `Imagens/`

Pasta destinada às imagens utilizadas para teste ou demonstração do projeto.

> Evite armazenar imagens pessoais, sensíveis ou que não possam ser redistribuídas publicamente.

## Pré-requisitos

- Python 3.9 ou superior.
- Uma conta Microsoft Azure.
- Um recurso do Azure AI Vision.
- Um recurso do Azure AI Speech.
- Chave e endpoint dos serviços.
- Sistema operacional compatível com PyAutoGUI.
- Microfone ou dispositivo de áudio, caso necessário para os testes.

## Configuração do Azure

Crie os recursos necessários no portal do Azure:

- Recurso Azure AI Vision.
- Recurso Azure AI Speech.

Depois, obtenha:

- Chave de acesso do Vision.
- Endpoint do Vision.
- Chave de acesso do Speech.
- Região do Speech.

Não coloque essas informações diretamente no código ou no README.

### Variáveis de ambiente

No Linux ou macOS:

```bash
export AZURE_VISION_KEY="sua-chave-do-vision"
export AZURE_VISION_ENDPOINT="seu-endpoint-do-vision"
export AZURE_SPEECH_KEY="sua-chave-do-speech"
export AZURE_SPEECH_REGION="sua-regiao"
```

No PowerShell:

```powershell
$env:AZURE_VISION_KEY="sua-chave-do-vision"
$env:AZURE_VISION_ENDPOINT="seu-endpoint-do-vision"
$env:AZURE_SPEECH_KEY="sua-chave-do-speech"
$env:AZURE_SPEECH_REGION="sua-regiao"
```

No Python:

```python
import os

vision_key = os.getenv("AZURE_VISION_KEY")
vision_endpoint = os.getenv("AZURE_VISION_ENDPOINT")

speech_key = os.getenv("AZURE_SPEECH_KEY")
speech_region = os.getenv("AZURE_SPEECH_REGION")
```

Valide as variáveis antes de executar:

```python
variaveis = [
    "AZURE_VISION_KEY",
    "AZURE_VISION_ENDPOINT",
    "AZURE_SPEECH_KEY",
    "AZURE_SPEECH_REGION"
]

for nome in variaveis:
    if not os.getenv(nome):
        raise RuntimeError(f"Variável não configurada: {nome}")
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/GabrielCustodio1/Projeto-de-Acessibilidade-Imagem-para-Voz.git
cd Projeto-de-Acessibilidade-Imagem-para-Voz
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install azure-cognitiveservices-vision-computervision
pip install azure-cognitiveservices-speech
pip install pyautogui
pip install pillow
```

Se o projeto utilizar outras bibliotecas, adicione-as ao arquivo `requirements.txt`.

Exemplo de `requirements.txt`:

```text
azure-cognitiveservices-vision-computervision
azure-cognitiveservices-speech
pyautogui
pillow
python-dotenv
```

Instale tudo com:

```bash
pip install -r requirements.txt
```

## Como executar

Coloque uma imagem de teste na pasta:

```text
Imagens/
```

Depois execute:

```bash
python main.py
```

O funcionamento exato pode variar conforme a implementação atual dos arquivos `main.py` e `mouse.py`.

Antes de executar, confirme:

- As credenciais do Azure estão configuradas.
- O endpoint está correto.
- A imagem existe.
- O caminho da imagem está correto.
- O dispositivo de áudio está funcionando.
- O PyAutoGUI possui permissão para interagir com a interface.

## Exemplo de fluxo

Exemplo conceitual:

```python
imagem = "Imagens/exemplo.jpg"

descricao = analisar_imagem(imagem)

gerar_audio(descricao)
```

O resultado esperado é uma descrição textual semelhante a:

```text
A imagem mostra um ambiente externo com uma pessoa próxima a uma árvore.
```

Em seguida, o texto é convertido em áudio para ser reproduzido pelo sistema.

> A descrição acima é apenas um exemplo ilustrativo. O resultado real depende da imagem analisada e da resposta do Azure Vision.

## Resultados esperados

Ao executar o projeto corretamente, espera-se que:

- Uma imagem seja selecionada ou carregada.
- O Azure Vision processe a imagem.
- Uma descrição textual seja retornada.
- O Azure Speech gere uma resposta em áudio.
- O usuário consiga ouvir uma interpretação do conteúdo visual.

Para documentar resultados reais, inclua:

- Imagem utilizada no teste.
- Texto retornado pelo Vision.
- Idioma e voz utilizados.
- Tempo aproximado de processamento.
- Possíveis erros ou limitações observados.

## Limitações

Este projeto é um protótipo educacional e não substitui uma avaliação humana ou um recurso profissional de acessibilidade.

Possíveis limitações:

- A descrição pode conter erros ou omitir detalhes importantes.
- O resultado depende da qualidade e do conteúdo da imagem.
- A API exige conexão com a internet.
- Os serviços do Azure podem gerar custos conforme o uso.
- O PyAutoGUI depende da resolução e da posição dos elementos na tela.
- Alterações na interface podem quebrar a automação.
- O áudio gerado pode não descrever corretamente textos pequenos ou objetos parcialmente ocultos.
- Imagens sensíveis podem apresentar riscos de privacidade quando enviadas a serviços externos.

## Segurança

Nunca publique chaves, endpoints privados ou tokens no GitHub.

Não faça:

```python
VISION_KEY = "chave-real-aqui"
```

Prefira variáveis de ambiente ou um arquivo `.env` não versionado.

Exemplo de `.env` local:

```text
AZURE_VISION_KEY=sua-chave
AZURE_VISION_ENDPOINT=seu-endpoint
AZURE_SPEECH_KEY=sua-chave
AZURE_SPEECH_REGION=sua-regiao
```

Adicione `.env` ao `.gitignore`:

```text
.env
.venv/
__pycache__/
*.wav
```

Caso uma chave seja publicada acidentalmente, revogue-a e gere uma nova no portal do Azure.

## Aprendizados

Durante o desenvolvimento, foram praticados:

- Integração de APIs de Inteligência Artificial.
- Uso de visão computacional em um caso de acessibilidade.
- Conversão de texto em fala.
- Manipulação de imagens em Python.
- Automação de interface com PyAutoGUI.
- Configuração de serviços no Azure.
- Gerenciamento de credenciais.
- Tratamento de arquivos.
- Organização de módulos Python.
- Documentação de projetos no GitHub.

## Próximos passos

- Criar uma interface gráfica mais acessível.
- Adicionar suporte a seleção de imagens por teclado.
- Implementar leitura de texto presente na imagem.
- Adicionar reconhecimento de objetos e ambientes.
- Permitir escolha do idioma do áudio.
- Permitir seleção da voz e velocidade da fala.
- Criar histórico das imagens processadas.
- Adicionar tratamento de erros mais detalhado.
- Substituir automações frágeis de mouse por uma interface estruturada.
- Criar testes automatizados.
- Adicionar uma API ou aplicação web.
- Implementar cache para evitar chamadas repetidas.
- Adicionar métricas de tempo e custo das requisições.
- Melhorar a descrição para priorizar informações relevantes à navegação.
- Validar o sistema com usuários e especialistas em acessibilidade.

## Referências

- [Azure AI Vision](https://azure.microsoft.com/products/ai-services/ai-vision)
- [Azure AI Speech](https://azure.microsoft.com/products/ai-services/ai-speech)
- [Documentação do Azure Vision](https://learn.microsoft.com/azure/ai-services/computer-vision/)
- [Documentação do Azure Speech](https://learn.microsoft.com/azure/ai-services/speech-service/)
- [Documentação do PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Python](https://www.python.org/)
- [Artigo da DIO sobre documentação de projetos no GitHub](https://web.dio.me/articles/seu-github-conta-uma-historia-ou-apenas-armazena-codigos-2e0b660d6e54?back=/home)

## Autor

Desenvolvido por **Gabriel Custódio**.

- GitHub: [GabrielCustodio1](https://github.com/GabrielCustodio1)
- Repositório: [Projeto-de-Acessibilidade-Imagem-para-Voz](https://github.com/GabrielCustodio1/Projeto-de-Acessibilidade-Imagem-para-Voz)

## Licença

Este projeto foi desenvolvido para fins educacionais.

Antes de utilizar o projeto em produção, verifique:

- Os termos de uso dos serviços Azure.
- Os custos das APIs.
- As licenças das bibliotecas utilizadas.
- A privacidade das imagens processadas.
- Os requisitos de acessibilidade aplicáveis.
