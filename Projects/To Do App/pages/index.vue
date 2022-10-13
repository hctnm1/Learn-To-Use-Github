<template>
  <main>
    <h1>Too Doo</h1>
    <p>What needs to be done?</p>

    <div class="create">
      <input type="text" v-model="newTask" placeholder="Your task ..." @keypress.enter="addTask" />
      <button @click="addTask">New</button>
    </div>

    <div class="value">
      <Todo v-for="(task, i) in $store.state.value"
      :key="i"
      :task="task" />
    </div>
  </main>

</template>

<script>
export default {
  data (){
    return {
      newTask: ''
    }
  },
  methods: {
    addTask (){
      if (this.newTask) {
        this.$store.commit('new', this.newTask);
        this.newTask = '';
      }
    }
  }
}
</script>

