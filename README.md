Flask + React To-Do Manager
A full-stack To-Do Manager application built using Flask (backend) and React (frontend). This project demonstrates a basic RESTful API with file-based storage using tasks.json, and a user interface built with React to interact with the API.
________________________________________
 Project Overview
•	Backend: Flask API with file-based JSON storage.
•	Frontend: React app calling Flask API.
•	Tech Stack: Python, Flask, JavaScript, React, Vite.
•	Storage: tasks.json (local file-based storage).
•	Purpose: Simple CRUD application to understand Flask-React integration.
________________________________________
 Project Structure
todo-project/
│
├── flask_todo_api/
│   ├── app.py
│   ├── tasks.json
│   ├── requirements.txt
│   └── venv/ (optional)
│
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── components/
    │       └── TodoApp.jsx
    └── public/
________________________________________
 Backend Setup (Flask)
 Create and activate virtual environment (optional)
cd backend
python -m venv venv
Activate environment: - Windows: venv\Scripts\activate - Mac/Linux: source venv/bin/activate
 Install dependencies
pip install flask flask-cors
 Create tasks.json
Create the file in the backend folder with the following content:
[]
 Run the Flask backend
cd backend
python app.py
Access API at: http://127.0.0.1:5000
________________________________________
 API Endpoints
Method	Endpoint	Description
GET	/api/health	Health status
GET	/	Welcome message
GET	/tasks	Fetch all tasks
GET	/tasks/<id>	Fetch task by ID
POST	/tasks	Create new task
PUT	/tasks/<id>	Update task
DELETE	/tasks/<id>	Delete task
Example API Usage
curl -X POST http://127.0.0.1:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title":"New Task", "description":"Test"}'
________________________________________
 Frontend Setup (React)
 Create React app using Vite
cd todo-project
npm create vite@latest frontend
# Select: React > JavaScript
 Install dependencies and run
cd frontend
npm install
npm run dev
The frontend will run at: http://localhost:5173
________________________________________
 Connecting React with Flask
In TodoApp.jsx, set the Flask backend URL:
const API_URL = "http://127.0.0.1:5000";
Ensure CORS is enabled in Flask:
from flask_cors import CORS
CORS(app)
________________________________________
 Troubleshooting
 Common Errors
Error	Reason	Fix
CORS policy: blocked	Different origin between frontend/backend	Enable flask-cors
Failed to fetch	Backend not running	Start Flask backend
package.json not found	Running npm install in wrong directory	Navigate to frontend/
.vue files created	Selected Vue during Vite setup	Recreate project with React
________________________________________
 Future Improvements
•	Switch to SQLite or PostgreSQL
•	Add authentication (login system)
•	Deploy backend on Render / Railway
•	Deploy React on Netlify / Vercel
•	Implement UI enhancements with Tailwind
________________________________________
 Contributions
Feel free to fork this project and suggest improvements via pull requests.
________________________________________
 License
This project is created for educational purposes and is open to use.
________________________________________
 Summary
•	Flask backend manages tasks via file-based storage
•	React frontend interacts with backend using REST API
•	Perfect for beginners to understand full-stack integration
