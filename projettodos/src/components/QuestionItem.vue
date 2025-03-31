<script>
export default {
  props: {
    question: Object
  },
  emits: ['removequestion', 'putquestion'],
  data() {
    return {
      modif: false, 
      titreactuel: this.question.title 
    };
  },
  methods: {
    removeQuestion() {
      this.$emit('removequestion', this.question.id);
    },
    ModeEdit() {
      this.modif = !this.modif;
      if (!this.modif) {
        this.$emit('putquestion', this.question.id, this.titreactuel, this.question.questionnaire_id);
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
  <div class="d-flex justify-content-between align-items-center">
    <input 
      :type="modif ? 'text' : 'hidden'" 
      class="form-control me-2" 
      v-model="titreactuel"
    />
    <span v-if="!modif">{{ question.title }}</span>
    <button 
      class="btn btn-primary btn-sm me-2" 
      @click="ModeEdit"
    >
      {{ modif ? 'Sauvegarder' : 'Modifier' }}
    </button>
    <button 
      class="btn btn-danger btn-sm" 
      @click="removeQuestion"
    >
      Supprimer
    </button>
  </div>
</template>
