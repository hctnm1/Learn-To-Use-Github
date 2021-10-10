// selectors
const todoInput = document.querySelector('.todo-input');
const submitBtn = document.querySelector('.submit-btn');
const todoList = document.querySelector('.todo-list');
const filterOptions = document.querySelector('.filter-todos');

// event listeners
document.addEventListener('DOMContentLoaded', loadTodos);
submitBtn.addEventListener('click', check);
todoList.addEventListener('click', cd);
filterOptions.addEventListener('click', filterTodos);


// functions
function check(event) {
    let str = todoInput.value.trim();
    if (str != '') {
        addTodo(event);
    } else {
        alert('todo cannot be empty!');
        return false;
    }
}

function addTodo(event) {
    // prevent form from submitting and refresh
    event.preventDefault();
    // console.log('click')

    // todo div
    const todoDiv = document.createElement('div');
    todoDiv.classList.add('todo');
    // toggle tick
    const toggleTick = document.createElement('span');
    toggleTick.innerHTML = 'pending_actions';
    toggleTick.classList.add('material-icons-outlined');
    toggleTick.classList.add('tick');
    todoDiv.appendChild(toggleTick);
    // create child li
    const todoContent = document.createElement('li');
    todoContent.innerText = todoInput.value;
    todoContent.classList.add('todo-content');
    todoDiv.appendChild(todoContent);
    // checked
    const checkBtn = document.createElement('button');
    checkBtn.innerHTML = '<span class="material-icons-outlined">done</span>';
    checkBtn.classList.add('check-btn');
    checkBtn.classList.add('btn');
    todoDiv.appendChild(checkBtn);
    // delete
    const deleteBtn = document.createElement('button');
    deleteBtn.innerHTML = '<span class="material-icons-outlined">delete</span>';
    deleteBtn.classList.add('delete-btn');
    deleteBtn.classList.add('btn');
    todoDiv.appendChild(deleteBtn);

    // append todoDiv to todoList
    todoList.appendChild(todoDiv);

    // save to local storage
    saveToLocal(todoInput.value);

    // clear todo input value
    todoInput.value = '';
}

function cd(e) {
    const item = e.target;
    // console.log(item);

    // delete todo   
    if (item.classList[0] === 'delete-btn') {
        const todo = item.parentElement;
        // transition
        todo.classList.add('fall');
        deleteLocal(todo);
        // transition listener
        todo.addEventListener('transitionend', () => {
            todo.remove();
        });
    }

    // check mark
    if (item.classList[0] === 'check-btn') {
        const todo = item.parentElement;
        todo.classList.toggle('done');
        if (todo.firstChild.innerHTML === 'pending_actions') {
            todo.firstChild.innerHTML = 'task_alt';
        } else {
            todo.firstChild.innerHTML = 'pending_actions'
        }
    }

}

function expand() {
    let expand = document.querySelector('.search-input');
    // console.log(expand);
    expand.classList.toggle('search-input-wide');
}

// filter todos
function filterTodos(e) {
    const todos = todoList.childNodes;
    // console.log(todos);
    // console.log(e.target.value);
    todos.forEach((todo) => {
        switch (e.target.value) {
            case "all":
                todo.style.display = "flex";
                break;

            case "completed":
                if (todo.classList.contains("done")) {
                    todo.style.display = "flex";
                } else {
                    todo.style.display = "none";
                }
                break;

            case "incomplete":
                if (todo.classList.contains("done")) {
                    todo.style.display = "none";
                } else {
                    todo.style.display = "flex";
                }
                break;
        }
    });
}

// search todos
const search = () => {
    let keyword = document.getElementById('search-box').value.toUpperCase();
    console.log(keyword);
    let listItem = todoList.getElementsByTagName('div');
    console.log(listItem);
    for (let index = 0; index < listItem.length; index++) {
        let text = listItem[index].children[1].innerText.toUpperCase();
        console.log(text);
        if (text.indexOf(keyword) > -1) {
            listItem[index].style.display = '';
        } else {
            listItem[index].style.display = 'none';
        }
    }
};

// save to local storage
function saveToLocal(todo) {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    }
    else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    todos.push(todo);
    localStorage.setItem("todos", JSON.stringify(todos));
}

// load todos from localstorage
function loadTodos() {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    }
    else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    todos.forEach((todo) => {
        // todo div
        const todoDiv = document.createElement('div');
        todoDiv.classList.add('todo');
        // toggle tick
        const toggleTick = document.createElement('span');
        toggleTick.innerHTML = 'pending_actions';
        toggleTick.classList.add('material-icons-outlined');
        toggleTick.classList.add('tick');
        todoDiv.appendChild(toggleTick);
        // create child li
        const todoContent = document.createElement('li');
        todoContent.innerText = todo;
        todoContent.classList.add('todo-content');
        todoDiv.appendChild(todoContent);
        // checked
        const checkBtn = document.createElement('button');
        checkBtn.innerHTML = '<span class="material-icons-outlined">done</span>';
        checkBtn.classList.add('check-btn');
        checkBtn.classList.add('btn');
        todoDiv.appendChild(checkBtn);
        // delete
        const deleteBtn = document.createElement('button');
        deleteBtn.innerHTML = '<span class="material-icons-outlined">delete</span>';
        deleteBtn.classList.add('delete-btn');
        deleteBtn.classList.add('btn');
        todoDiv.appendChild(deleteBtn);

        // append todoDiv to todoList
        todoList.appendChild(todoDiv);
    })
}

// delete from local storage
function deleteLocal(todo) {
    let todos;
    if (localStorage.getItem("todos") === null) {
        todos = [];
    }
    else {
        todos = JSON.parse(localStorage.getItem("todos"));
    }
    console.log(todo.children[1].innerHTML);
    console.log(todos.indexOf(todo.children[1].innerHTML));

    let eleIdx = todos.indexOf(todo.children[1].innerHTML);
    todos.splice(eleIdx, 1);
    localStorage.setItem("todos", JSON.stringify(todos));
}

// delete all
function deleteAll(){
    if (localStorage.getItem("todos") === null) {
        todos = [];
    }
    else {
        todos = JSON.parse(localStorage.getItem("todos"));
        todos = [];
        localStorage.setItem("todos", JSON.stringify(todos));
        document.location.reload()
    }
}
