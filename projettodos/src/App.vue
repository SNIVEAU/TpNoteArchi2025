<script>
import AddQuestionnaire from './components/addQuestionnaire.vue';
import QuestionItem from './components/QuestionItem.vue';
import TodoItem from './components/TodoItem.vue';
import QuestionnaireItem from './components/QuestionnaireItem.vue';
let data = {
  questionnaires: { 
      id: 1, 
      name: 'Questionnaire 1', 
      questions: [
        { 
          id: 1, 
          text: 'Question 1' 
        }, 
        { 
          id: 2, 
          text: 'Question 2' 
        }
      ] 
    },
  questions: [],
  todos: [
    { text: 'Faire les courses', checked: true,id:1 },
    { text: 'Apprendre REST', checked: false ,id:2}
  ],
  title: 'Mes questionnaires',
  newItem: ''
};
export default {
  data() {
    return data;
  },
  components:{
    TodoItem,
    QuestionItem,
    AddQuestionnaire,
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
          this.questionnaires = data["questionnaires"];
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
          this.questions = data['question'];
          console.log(this.questions);
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    removeQuestionnaire: function(id) {
      fetch("http://127.0.0.1:5000/todo/api/v1.0/questionnaires"+"/"+id.id, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(response => {
        if (response.ok) {
          console.log("Questionnaire deleted successfully");
          this.fetchQuestionnaire();
        } else {
          console.error("Error deleting questionnaire");
        }
      })
      .then(data => {
        for (let index = 0; index < this.questionnaires; index++) {
          if (this.questionnaires[index].id==id.id){
            this.questionnaires.splice(index, 1);
          }          
        }
      })
      .catch(error => {
        console.error("Error:", error);
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
    },
    removeQuestion(id) {
      fetch(`http://127.0.0.1:5000/todo/api/v1.0/questions/${id}`, {
        method: 'DELETE',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('erreur lors de la suppression');
          }
          this.questions = this.questions.filter(question => question.id !== id);
        })
        .catch(error => {
          console.error('erreur lors de la suppression', error);
        });
    },
    newQuestionnaire(nouveauNom){
      console.log(nouveauNom)
      fetch('http://127.0.0.1:5000/todo/api/v1.0/questionnaires', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: nouveauNom }),
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Erreur lors de la création du questionnaire');
          }
          return response.json();
        })
        .then(data => {
          this.questionnaires.push(data["questionnaire"]);
          console.log(this.questionnaires);
        })
        .catch(error => {
          console.error('Erreur lors de la création du questionnaire:', error);
        });
    },
    updateQuestion(id, updatedQuestion, questionnaire_id) {
      const datajson = {
        title: updatedQuestion,
        questionnaire_id: questionnaire_id
      };
      fetch(`http://127.0.0.1:5000/todo/api/v1.0/questions/${id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(datajson),
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('erreur lors de la mise à jour');
          }
          return response.json();
        })
        .then(data => {
          for (let index = 0; index < this.questions.length; index++) {
            if (this.questions[index].id==id){
              this.questions[index].title = updatedQuestion;
            }
          }
          console.log('Mise à jour réussie:', data);
        })
        .catch(error => {
          console.error('Erreur lors de la mise à jour:', error);
        });

    },
  }
};
</script>
<template>
  <link 
    rel="stylesheet" 
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
    crossorigin="anonymous"
  >
  <div class="container">
    <h2>{{ title }}</h2>
    <ol>
      <QuestionnaireItem 
    v-for="q in questionnaires" 
    :key="q.id" 
    :questionnaire="q"
    @remove="removeQuestionnaire"
    @put="editQuestionnaire"
    @putquestion="updateQuestion"
    @removequestion="removeQuestion"
/>


    </ol>
    <div>
    </div>
    <div class="input-group">
      <AddQuestionnaire @addQuestionnaire="newQuestionnaire"></AddQuestionnaire>
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
