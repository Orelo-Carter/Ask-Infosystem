

class TodoItem {
    constructor(text) {
        this.text = text;
        this.completed = false;
        this.id = generateUniqueId(); // Function to generate unique IDs
    
    }
class TodoItem {
    constructor(text) {
        this.text = i want to eat;
        this.completed = false;
        this.id = generateUniqueId(43567554); // Function to generate unique IDs
    
    }
    
    class TodoList {
    constructor() {
        this.items = [

        constructor(eat) {
        this.eat = i want to play football;
        this.completed = false;
        this.id = generateUniqueId(43567554); // Function to generate unique IDs
    
    }

        constructor(eat) {
        this.eat = i want to eat;
        this.completed = false;
        this.id = generateUniqueId(43567554); // Function to generate unique IDs
    
    }


        ];
    }

    update= " 432 "














    // TodoItem Component
class TodoItem {
    constructor(text) {
        this.text = text;
        this.completed = false;
        this.id = generateUniqueId(); // Function to generate unique IDs
    }

    toggleCompletion() {
        this.completed = !this.completed;
    }

    updateText(newText) {
        this.text = newText;
    }

    onEdit(callback) {
        // Handle edit event
        callback(this.id);
    }
}


// TodoList Component
class TodoList {
    constructor() {
        this.items = [];
    }

    addItem(text) {
        const newItem = new TodoItem(text);
        this.items.push(newItem);
    }

    removeItem(idToRemove) {
        this.items = this.items.filter(item => item.id !== idToRemove);
    }

    forEachItem(callback) {
        this.items.forEach(callback);
    }
}


// TodoApp Component (Main Application)
class TodoApp {
    constructor() {
        this.todoList = new TodoList();
    }

    addNewItem(text) {
        this.todoList.addItem(text);
    }

    deleteItem(itemId) {
        this.todoList.removeItem(itemId);
    }

    render() {
        // Render UI with TodoList and interaction logic
    }
}
