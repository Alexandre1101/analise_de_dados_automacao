# 📊 Automação de Relatórios de Vendas

Este projeto automatiza o fluxo de processamento de dados de vendas, geração de relatórios detalhados em Excel e PDF, e envio automático por e-mail. É uma solução completa de BI (Business Intelligence) simplificada para monitoramento de performance semanal.

## 🚀 Funcionalidades

- **Processamento de Dados**: Limpeza de dados nulos, remoção de duplicatas e padronização de textos (regiões e categorias).
- **Análise de Métricas**: Cálculo automático de faturamento total, produtos mais vendidos, melhores categorias, regiões e performance de vendedores.
- **Relatórios em Excel**: Geração de um arquivo `.xlsx` com múltiplas abas organizadas por métricas.
- **Notificação Automática**: Envio do relatório gerado diretamente para o e-mail do gestor utilizando SMTP seguro.
- **Relatórios em PDF Profissionais**: Geração de um relatório executivo em PDF, com layout limpo, tabelas formatadas e padrão monetário brasileiro (R$).
- **Notificação Automática**: Envio dos relatórios gerados (Excel e PDF) diretamente para o e-mail do gestor utilizando SMTP seguro.

## 🛠️ Tecnologias Utilizadas

- Python 3.13+
- Pandas para manipulação de dados.
- OpenPyXL para suporte a arquivos Excel.
- Pathlib para gestão robusta de caminhos de arquivos.
- Smtplib para integração com servidores de e-mail.
- ReportLab para geração de documentos PDF de alta qualidade.

## 📋 Pré-requisitos

Este projeto utiliza o uv como gerenciador de pacotes. Certifique-se de tê-lo instalado ou utilize o `pip` com o arquivo de dependências.

## ⚙️ Configuração

Antes de rodar o script, você precisa configurar as variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto com as seguintes chaves:

```text
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_de_app_do_gmail
EMAIL_RECEIVER=email_do_destinatario@gmail.com
```

> **Nota:** Se estiver usando Gmail, você deve gerar uma "Senha de App" nas configurações de segurança da sua conta Google para que o script possa enviar e-mails.

## 📂 Estrutura do Projeto

```text
projeto_automacao/
├── data/               # Banco de dados (CSV)
├── output/             # Relatórios gerados (Excel)
├── src/                # Código fonte
│   ├── main.py         # Orquestrador do fluxo
│   ├── data_processing.py # Lógica de ETL e métricas
│   ├── report.py       # Geração do Excel
│   └── email_sender.py # Lógica de envio de e-mail
└── README.md
```

## 🏃 Como Executar

1. Instale as dependências:
   ```bash
   uv sync
   ```
2. Execute o script principal:
   ```bash
   python src/main.py
   ```