<script>
    export default {
        props: {
            todo : Object
        },
        data () {
            return {
                Modifier : true
            }
        },
        methods: {
            suppr: function() {
            this.$emit('remove', { id: this.todo.id });
            },
            modif: function() {
                // const newText = document.getElementById('modiftodo').value;
                // this.$emit('put', { id: this.todo.id, newtext: newText });
                if (!this.Modifier){
                    const newtext = document.getElementById("edit").value;
                    console.log(newtext)
                    this.$emit('put', { id: this.todo.id, newtext: newtext });

                }
                this.Modifier = !this.Modifier

            }
        },
        emits : ['remove','put']
    };
</script>

<template>
    <link 
    rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" 
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" 
    crossorigin="anonymous"
  >
<div class="checkbox">
          <label>
            <input v-if="Modifier" id="todo.text"
              type="checkbox" 
              v-model="todo.checked"
              
            > 

            <input v-else type="text"
            id="edit"
            placeholder='Veuillez changer le nom de la tache'
            v-model="todo.text">
            {{ todo.text }}

          </label>
          <input type="button"
            class="btn btn-danger"
            value="Supprimer"
            @click="suppr">
          <label>
            <input type="button"
            class="btn btn-danger"
            value="Modifier"
            @click="modif">
          </label>label
        </div>
</template>