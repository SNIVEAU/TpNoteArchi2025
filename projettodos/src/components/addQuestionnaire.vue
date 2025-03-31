<script>
export default {
  data() {
    return {
      nouveauNom: "", 
    };
  },
  methods: {
    addQuestionnaire() {
      if (this.nouveauNom.trim() !== "") {
        this.$emit("addQuestionnaire", this.nouveauNom);
        this.nouveauNom = ""; 
      } else {
        alert("Veuillez entrer un questionnaire valide."); 
      }
    },
  },
};
</script>

<template>
  <div class="input-group mb-3">
    <input
      v-model="nouveauNom"
      placeholder="Ajouter un nouveau Questionnaire"
      type="text"
      class="form-control"
    />
    <button @click="addQuestionnaire" class="btn btn-primary">
      Ajouter
    </button>
  </div>
</template>
