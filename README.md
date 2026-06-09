# DevSnippets — Developer Snippet 

A personal API to save, search, and manage your code snippets, commands, and developer notes

## What is this?

Ever forget a git command you used last week? Or a regex pattern you wrote last month?  
DevSnippets is your personal cheat sheet API — save snippets with tags and retrieve them instantly.

## Features

- Save code snippets with title, language, and tags
- Search snippets by tag
- Update and delete snippets
- Auto ID generation
- Duplicate title prevention

## Tech Stack

- **FastAPI** — REST API framework
- **Pydantic** — data validation
- **Python** — backend language
- **JSON** — local storage (Phase 1)

## Project Roadmap

- [x] Phase 1 — Basic CRUD API with JSON storage
- [ ] Phase 2 — PostgreSQL + SQLAlchemy + JWT Auth
- [ ] Phase 3 — Docker + Deployment

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /all_snippets | Get all snippets |
| GET | /view?tags={tag} | Search by tag |
| POST | /create_post | Create a snippet |
| PUT | /update/{id} | Update a snippet |
| DELETE | /delete/{id} | Delete a snippet |

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/adarsh-exp/DevSnippets.git
cd devask
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create empty Snippets.json**
```bash
echo {} > Snippets.json
```

**5. Run the server**
```bash
uvicorn main:app --reload
```

**6. Open Swagger UI**
```
http://127.0.0.1:8000/docs
```

## Example Snippet

```json
{
  "title": "Undo last commit",
  "code": "git reset --soft HEAD~1",
  "language": "bash",
  "tags": ["git", "undo"]
}
```
