<script>
export default {
  props: {
    questionnaireId: Number
  },
  data() {
    return {
      nouveauNom: "", 
    };
  },
  methods: {
    addQuestionnaire() {
      if (this.nouveauNom.trim() !== "") {
        this.$emit("addQuestionnaire", this.nouveauNom, this.questionnaireId);
        this.nouveauNom = ""; 
      } else {
        alert("Veuillez entrer une question valide."); 
      }
    },
  },
};
</script>


<template>
  <div class="input-group mb-3">
    <input
      v-model="nouveauNom"
      placeholder="Ajouter une nouvelle question"
      type="text"
      class="form-control"
    />
    <button @click="addQuestionnaire" class="btn btn-primary">
      Ajouter la question
    </button>
  </div>
</template>
