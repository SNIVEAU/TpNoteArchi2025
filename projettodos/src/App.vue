<script>
import TodoItem from './components/TodoItem.vue';
import QuestionnaireItem from './components/QuestionnaireItem.vue';
let data = {
  questionnaires: [],
  questions: [],
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
    TodoItem,
    QuestionnaireItem
  },
  mounted() {
    this.fetchQuestionnaire();
    this.fetchQuestion();
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
    fetchQuestionnaire: function () {
      fetch('http://127.0.0.1:5000/todo/api/v1.0/questionnaires')
        .then(response => response.json())
        .then(data => {
          this.questionnaires = data;
          console.log(this.questionnaires);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    fetchQuestion: function () {
      fetch('http://127.0.0.1:5000/todo/api/v1.0/questions')
        .then(response => response.json())
        .then(data => {
          this.questions = data;
          console.log(this.questions);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
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
        <QuestionnaireItem 
          v-for="q in questionnaires"
          :key="q.id"
          :questionnaire="q"
          @remove="removeQuestionnaire"
          @put="editQuestionnaire"
          @add="addQuestionToQuestionnaire"
        />
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
