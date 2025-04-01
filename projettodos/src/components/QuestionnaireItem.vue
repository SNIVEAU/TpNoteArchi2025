<template>
  <div class="card mt-3 p-3">

    <div class="d-flex align-items-center mb-2">
      <input 
        v-if="modifier" 
        type="text" 
        class="form-control me-2" 
        v-model="nomActuel"
      />
      <h2 v-else>{{ questionnaire.name }}</h2>

      <button class="btn btn-primary btn-sm ms-2" @click="toggleEdit">
        {{ modifier ? 'Sauvegarder' : 'Modifier' }}
      </button>
      <button class="btn btn-danger btn-sm ms-2" @click="removeQuestionnaire">
        Supprimer
      </button>
    </div>

    <button class="btn btn-secondary btn-sm" @click="showQuestions">
      {{ afficherLesQuestions ? 'Masquer' : 'Afficher' }} les questions
    </button>

    <ul v-if="afficherLesQuestions">
      <li v-for="question in questionnaire.questions" :key="question.id">
        <QuestionItem 
          :question="question" 
          @removequestion="removeQuestionFromQuestionnaire"
          @putquestion="putQuestion"
        />
      </li>
      <AddQuestion 
        @addQuestionnaire="addQuestionToQuestionnaire"
        :questionnaireId="questionnaire.id"
      />
    </ul>

  </div>
</template>

<script>
import QuestionItem from './QuestionItem.vue';
import AddQuestion from './AddQuestion.vue';

export default {
  props: {
    questionnaire: Object
  },
  components: {
    QuestionItem, 
    AddQuestion
  },
  data() {
    return {
      afficherLesQuestions: false,
      modifier: false,
      nomActuel: this.questionnaire.name
    };
  },
  methods: {
    showQuestions() {
      this.afficherLesQuestions = !this.afficherLesQuestions;
    },
    removeQuestionnaire() {
      this.$emit('remove', { id: this.questionnaire.id });
    },
    toggleEdit() {
      this.modifier = !this.modifier;
      if (!this.modifier) {
        this.$emit('put', this.nomActuel, this.questionnaire.id);
      }
    },
    putQuestion(id, updatedTitle, questionnaire_id) {
      this.$emit('putquestion', id, updatedTitle, questionnaire_id);
    },
    removeQuestionFromQuestionnaire(id) {
      this.$emit('removequestion', id);
      this.questionnaire.questions = this.questionnaire.questions.filter(q => q.id !== id);
    },
    addQuestionToQuestionnaire(nouveauNom, questionnaireId) {
      this.$emit('addquestion', nouveauNom, questionnaireId);
    }
  },
  emits: ['remove', 'putquestion', 'removequestion', 'addquestion', 'put']
};
</script>