<script>
import QuestionItem from './QuestionItem.vue';
    export default {
        props: {
            questionnaire : Object
        },
        data () {
            return {
                Modifier : true,
                afficherLesQuestions : false,
            }
        },
        components:{
            QuestionItem
        },
        methods: {
            showQuestions: function(){
                this.afficherLesQuestions = !this.afficherLesQuestions;
                console.log("coucou");
            },
            removeQuestionnaire: function(){
                this.$emit('remove', { id: this.questionnaire.id });
            },
            editQuestionnaire: function(){
                this.$emit('put', { id: this.questionnaire.id });
            },
            addQuestionToQuestionnaire: function(){
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
          <li> {{ questionnaire.name }} </li>
          <ul v-if="questionnaire.questions && questionnaire.questions.length && this.afficherLesQuestions">
            <!-- <li v-for="q in questionnaire.questions" :key="q.id">{{ q.title }}</li> -->
            <li v-for="question in questionnaire.questions" :key="question.id">
                <QuestionItem 
                    :question="question" 
                    @remove="removeQuestion"
                    @putquestion="putQuestion"
                ></QuestionItem>
            </li>
          </ul>
           <input type="button"
            class="btn btn-danger"
            value="Afficher les questions"
            @click="showQuestions">
          <label>
            <input type="button"
            class="btn btn-danger"
            value="Supprimer le questionnaire"
            @click="removeQuestionnaire">
          </label>
        </div>
</template>