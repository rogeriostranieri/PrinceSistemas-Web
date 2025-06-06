# Prince Sistemas

Sistema completo para gestão empresarial, desenvolvido com **Django** (backend), **PostgreSQL** (banco de dados) e **Angular 19 Standalone** (frontend).  
O projeto é multiplataforma, responsivo, moderno e preparado para desktop, mobile e web app.

---

## Principais Recursos

- CRUD completo para Empresas, Laudos/Alvarás, Sócios e Parcelamentos
- Interface moderna, responsiva e minimalista
- Menu lateral expansível e adaptativo
- Geração de documentos (Word, PDF) automatizada
- Comunicação em tempo real via WebSockets
- SweetAlert2 para alertas, confirmações e carregamento
- Formulários com validação em tempo real
- Feedback visual e animações suaves
- Suporte a temas claros e escuros
- API RESTful com documentação automática (Swagger/OpenAPI)
- Armazenamento local para dados offline
- Segurança com autenticação JWT e proteção de rotas
- Suporte a PWA (Progressive Web App)

---

## Tecnologias Utilizadas

- **Backend:** Django 5.2.1, Django REST Framework 3.16.0, Python 3.11+, PostgreSQL 15+
- **Frontend:** Angular 19 Standalone, TypeScript, SCSS, SweetAlert2
- **Documentos:** WeasyPrint, python-docx, docxtpl
- **Comunicação:** Django Channels 4.2.2 (WebSockets)
- **Segurança:** JWT, django-allauth
- **Outros:** Django Filter, PWA, SASS Processor, Gunicorn

---

## Estrutura do Projeto

```
PrinceSistemaPY/
├── backend/
│   ├── apps/
│   │   ├── login/
│   │   ├── empresas/
│   │   ├── parcelamentos/
│   │   ├── laudos/
│   │   ├── socios/
│   │   └── ... (outros apps)
│   ├── manage.py
│   └── PrinceSistemas/
│       ├── settings.py
│       └── urls.py
├── frontend/
│   ├── app/
│   │   ├── src/
│   │   │   ├── app/
│   │   │   │   ├── empresas/
│   │   │   │   ├── laudos/
│   │   │   │   ├── socios/
│   │   │   │   ├── parcelamentos/
│   │   │   │   ├── geral/
│   │   │   │   ├── login/
│   │   │   │   └── ... (outros componentes)
│   │   │   └── styles.scss
│   │   └── angular.json
│   └── package.json
├── BancoDeDados.txt
├── PRINCIPAL.txt
├── requeriments.txt
├── LICENSE
└── README.md
```

---

## Como rodar o projeto

### **Backend (Django)**

1. Crie e ative o ambiente virtual:

```sh
cd PrinceSistemaPY/backend
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```sh
pip install -r requeriments.txt
```

3. Configure o banco de dados PostgreSQL conforme o exemplo em `PRINCIPAL.txt` e `BancoDeDados.txt`.

4. Execute as migrações:

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py check
```

5. Inicie o servidor:

```sh
python manage.py runserver
```

---

### **Frontend (Angular)**

1. Instale as dependências:

```sh
cd PrinceSistemaPY/frontend/app
npm install
```

2. Inicie o servidor de desenvolvimento:

```sh
ng serve
```

3. Acesse em [http://localhost:4200](http://localhost:4200)

---

## Banco de Dados

- **Banco:** PostgreSQL  
- **Nome:** PrinceDB  
- **Tabelas:** Empresas, Laudos, Sócios, Parcelamentos  
- **Exemplo de conexão:**  
  Veja detalhes e exemplos de queries em `BancoDeDados.txt`.

---

## Funcionalidades Avançadas

- **Geração de Documentos:** Criação automática de contratos, relatórios e formulários em Word e PDF
- **Comunicação em Tempo Real:** Notificações e atualizações via WebSockets
- **API Documentada:** Interface Swagger/OpenAPI para testes e documentação da API
- **PWA:** Funciona offline e pode ser instalado como aplicativo
- **Autenticação Social:** Login via redes sociais com `django-allauth`
- **Validação Avançada:** Verificação de dados em tempo real no frontend e backend

---

## Comandos úteis

- **Atualizar o repositório no GitHub:**

```sh
git add .
git commit -m "Descreva aqui o que mudou"
git push
```

- **Atualizar dependências Python:**

```sh
pip install -r requeriments.txt --upgrade
```

- **Instalar SweetAlert2 no frontend:**

```sh
npm install sweetalert2
```

---

## Licença

Este projeto está licenciado sob a [Apache License 2.0](LICENSE).

---

**Desenvolvido por Rogerio Stranieri – 2025**