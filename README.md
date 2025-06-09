# AtosCapital-Squad-10
Desenvolver um aplicativo web interativo para exibição de dashboards de vendas, integrando funcionalidades de notificação e consulta via WhatsApp e utilizando IA generativa para fornecer insights avançados.

# 📊 Dashboard Inteligente de Filiais com IA e WhatsApp

Este projeto consiste em um sistema web interativo para visualização de dados de vendas por filial, com previsão de vendas via IA e integração com WhatsApp para envio de notificações automatizadas.

## 🚀 Visão Geral

Cada filial possui seu próprio painel de controle com três dashboards principais:

1. **Dashboard Geral da Filial**  
   - Faturamento do dia anterior  
   - Comparativo com o mesmo dia do mês anterior  
   - Filtro de data interativo  

2. **Dashboard de Previsão de Vendas (IA)**  
   - Previsão com base em modelos de machine learning  
   - Gráficos comparativos semanais  

3. **Dashboard de Metas e KPIs**  
   - Acompanhamento de metas fixas de crescimento (5%)  
   - Visualização de indicadores de performance por período  

Além disso, os relatórios podem ser baixados em PDF e enviados automaticamente via WhatsApp.

---

## 🛠️ Stack de Desenvolvimento

### 🔹 Frontend (Dashboard Web)
- **Linguagem:** Python  
- **Framework:** [Streamlit](https://streamlit.io/)  
- **Gráficos:** Plotly, Matplotlib ou Seaborn  
- **Estilização:** CSS customizado + temas nativos do Streamlit

**Motivo:** Permite construção ágil de dashboards interativos sem necessidade de um frontend separado, com visual moderno e fácil integração com Python.

---

### 🔹 Backend (API e Processamento)
- **Linguagem:** Python  
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Banco de Dados:** MySQL  

**Motivo:** FastAPI oferece excelente desempenho para APIs e suporte a WebSockets, facilitando integrações em tempo real. MySQL é ideal para escalar dados de vendas e históricos.

---

### 🔹 IA Generativa (Previsão de Vendas)
- **Framework:** [PyTorch](https://pytorch.org/)  

**Motivo:** Flexível e robusto para construção e treinamento de modelos de redes neurais personalizadas, com foco em previsões de vendas por padrão de comportamento.

---

### 🔹 Integração com WhatsApp
- **Ferramentas:** N8N + Evolution API

**Motivo:** Permite automação completa de notificações, alertas e respostas interativas diretamente no WhatsApp, sem configuração complexa de servidores.

---

## ☁️ Infraestrutura & Deploy

### 🧱 Hospedagem
- **Backend:** AWS 
- **Frontend:** Streamlit Sharing 

### 🐳 Conteinerização
- **Docker:** Padronização do ambiente, fácil escalabilidade e replicação

### 🔁 CI/CD
- **GitHub Actions:** Automação de testes, builds e deploy contínuo a cada push no repositório principal

---

## 📡 Endpoints da API

| Método | Rota                                  | Descrição                                 |
|--------|----------------------------------------|-------------------------------------------|
| GET    | `/dashboard/filial/{cnpj}/vendas`     | Retorna dados de vendas da filial         |
| GET    | `/dashboard/filial/{cnpj}/previsao`   | Retorna previsão de vendas com IA         |
| GET    | `/dashboard/filial/{cnpj}/metas`      | Retorna os indicadores e metas fixas      |

---

## 📄 Geração de Relatórios

Cada dashboard possui a opção de exportação dos dados visualizados em **formato PDF**. 
---

## 🧪 Como Executar o Projeto

### Requisitos
- Python 3.10+
- Docker e Docker Compose 
- MySQL 8+
- Conta com Evolution API

### Backend
```bash
cd backend
uvicorn main:app --reload
