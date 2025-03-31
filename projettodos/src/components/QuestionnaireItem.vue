<script>
import QuestionItem from './QuestionItem.vue';

export default {
    props: {
        questionnaire: Object
    },
    data() {
        return {
            Modifier: true,
            afficherLesQuestions: false,
        };
    },
    components: {
        QuestionItem
    },
    methods: {
        showQuestions() {
            this.afficherLesQuestions = !this.afficherLesQuestions;
        },

        removeQuestionnaire() {
            this.$emit('remove', { id: this.questionnaire.id });
        },

        editQuestionnaire() {
            this.$emit('put', { id: this.questionnaire.id });
        },

        addQuestionToQuestionnaire() {
            this.$emit('add', { id: this.questionnaire.id });
        },

        putQuestion(id, updatedTitle, questionnaire_id) {
            console.log("putQuestion reçu avec:", id, updatedTitle, questionnaire_id);
            this.$emit('putquestion', id, updatedTitle, questionnaire_id);
        },

        removeQuestionFromQuestionnaire(id) {
            console.log("Suppression de la question avec l'ID:", id);
            this.$emit('removequestion', id);
        }
    },

    emits: ['remove', 'put', 'removequestion', 'putquestion']
};
</script>

<template>
    <link 
    rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
    crossorigin="anonymous">

    <div>
        
        <li>{{ questionnaire.name }}</li>
        <ul v-if="questionnaire.questions && questionnaire.questions.length && afficherLesQuestions">
            <li v-for="question in questionnaire.questions" :key="question.id">
                <QuestionItem 
                    :question="question" 
                    @removequestion="removeQuestionFromQuestionnaire"
                    @putquestion="putQuestion"
                />
            </li>
        </ul>
        
        <input type="button"
            class="btn btn-primary"
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
