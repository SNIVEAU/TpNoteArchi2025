<template>
  <div class="d-flex justify-content-between align-items-center border p-2">
    <input 
      v-if="modif" 
      type="text" 
      class="form-control me-2" 
      v-model="titreactuel"
    />
    <span v-else>{{ question.title }}</span>

    <button class="btn btn-primary btn-sm me-2" @click="ModeEdit">
      {{ modif ? 'Sauvegarder' : 'Modifier' }}
    </button>

    <button class="btn btn-danger btn-sm" @click="removeQuestion">
      Supprimer
    </button>
  </div>
</template>

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
