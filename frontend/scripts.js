document.addEventListener("DOMContentLoaded", () => {
    const todoForm = document.getElementById("todo-form");
    const todoList = document.getElementById("todo-list");
    const API_URL = "http://localhost:8000"; // Change this to your backend server URL

    todoForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;

        const response = await fetch(`${API_URL}/todos/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ id: Date.now(), title, description, completed: false }),
        });

        const newTodo = await response.json();
        addTodoToList(newTodo);
        todoForm.reset();
    });

    async function fetchTodos() {
        const response = await fetch(`${API_URL}/todos/`);
        const todos = await response.json();
        todos.forEach(addTodoToList);
    }

    function addTodoToList(todo) {
        const li = document.createElement("li");
        li.className = todo.completed ? "completed" : "";
        li.innerHTML = `
            <span>${todo.title}: ${todo.description}</span>
            <button onclick="deleteTodo(${todo.id})">Delete</button>
        `;
        todoList.appendChild(li);
    }

    window.deleteTodo = async (id) => {
        await fetch(`${API_URL}/todos/${id}`, {
            method: "DELETE",
        });
        document.querySelector(`li[data-id="${id}"]`).remove();
    };

    fetchTodos();
});
