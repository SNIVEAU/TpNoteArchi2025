<script>
    export default {
        props: {
            questionnaire : Object
        },
        data () {
            return {
                Modifier : true
            }
        },
        methods: {
            showQuestions: function(){
                console.log(this.questionnaire.questions)
            },
            supprQuestionnaire: function(){
                this.$emit('remove', { id: this.questionnaire.id });
            },
            modifierQuestionnaire: function(){
                this.$emit('put', { id: this.questionnaire.id });
            },
            ajouterQuestion: function(){
                this.$emit('add', { id: this.questionnaire.id });
            }

        },
        emits : ['remove','put']
    };
</script>

<template>
    <link 
    rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <div>
          <label>
            <input v-if="Modifier" id="todo.text"
              type="checkbox" 
              v-model="todo.checked">
            <input v-else type="text"
            id="edit"
            placeholder='Veuillez changer le nom du questionnaire'
            v-model="todo.text">
            {{ todo.text }}
          </label>
          <input type="button"
            class="btn btn-danger"
            value="Afficher les questions"
            @click="showQuestions">
          <label>
            <input type="button"
            class="btn btn-danger"
            value="Supprimer le questionnaire"
            @click="supprQuestionnaire">
          </label>
        </div>
</template>