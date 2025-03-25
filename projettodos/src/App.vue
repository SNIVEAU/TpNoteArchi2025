<script>
import TodoItem from './components/TodoItem.vue';
let data = {
  todos: [
    { text: 'Faire les courses', checked: true,id:1 },
    { text: 'Apprendre REST', checked: false ,id:2}
  ],
  title: 'Mes tâches',
  newItem: ''
};
export default {
  data() {
    return data;
  },
  components:{
    TodoItem
  },
  methods: {
    addItem: function () {
      let text = this.newItem.trim();
      let id=0;
      this.todos.forEach(todo => {
        if (todo.id>id){
          id=todo.id
        }
      });
      if (text) {
        this.todos.push({
          text: text,
          checked: false,
          id:id+1
        });
        this.newItem = '';
      }
    },
    removeItem: function(id) {
      console.log(id)
      for (let index = 0; index < this.todos.length; index++) {
        if (this.todos[index].id==id.id){
          this.todos.splice(index, 1);
        }
      }
    },
    edittodo: function(id,newtext) {
      for (let index = 0; index < this.todos.length; index++) {
        if (this.todos[index].text==id.id){
          this.todos[index].text = newtext
        }
      }
    }
  }
};
</script>
<template>
  <link 
    rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
    crossorigin="anonymous"
  >
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <li 
        v-for="todo in todos" 
        v-bind:class="{ 'alert alert-success': todo.checked }"
      >
        <!-- <div class="checkbox">
          <label>
            <input 
              type="checkbox" 
              v-model="todo.checked"
            > 
            {{ todo.text }}
          </label>
        </div> -->
        <TodoItem @remove="removeItem" @put="edittodo" :todo="todo"></TodoItem>
      </li>
    </ol>
    <div class="input-group">
      <input 
        v-model="newItem"
        @keyup.enter="addItem"
        placeholder="Ajouter une tache à la liste"
        type="text"
        class="form-control"
      >
      <span class="input-group-btn">
        <button 
          @click="addItem"
          class="btn btn-default"
          type="button"
        >
          Ajouter
        </button>
      </span>
    </div>
  </div>
</template>
<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
